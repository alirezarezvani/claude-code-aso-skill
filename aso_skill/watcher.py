"""ASO Watcher — diff competitor metadata across time.

Designed to be run on a daily schedule (e.g. via GitHub Action). On each
run it:

  1. Reads a JSON config that lists which competitor apps to track.
  2. Fetches current metadata for each via the iTunes API (cached).
  3. Loads the last-known competitor state from the per-app StateStore.
  4. Returns the list of "material" changes (and optionally persists the
     new state).

What counts as material is deliberately conservative — title, subtitle,
seller, current version, price, and rating delta above a configurable
threshold. Description and `userRatingCount` are skipped because they
churn daily without meaningful signal.

The watcher is a pure-Python module; the CLI surface lives in
``aso_skill/cli.py`` (``aso watch ...``) and the recurring schedule lives
in a downstream GitHub Action workflow.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

from .itunes import iTunesAPI
from .state import StateStore

DEFAULT_RATING_DELTA_THRESHOLD = 0.1

_TRACKED_FIELDS: Tuple[str, ...] = (
    "trackName",
    "primaryGenreName",
    "version",
    "sellerName",
    "formattedPrice",
    "averageUserRating",
)

_TEXT_FIELDS = {f for f in _TRACKED_FIELDS if f != "averageUserRating"}


def _snapshot(metadata: Dict[str, Any]) -> Dict[str, Any]:
    """Reduce a full iTunes app blob down to the fields we track."""
    return {field: metadata.get(field) for field in _TRACKED_FIELDS}


def _diff_one_competitor(
    name: str,
    app_id: str,
    previous: Optional[Dict[str, Any]],
    current: Dict[str, Any],
    rating_delta_threshold: float,
) -> List[Dict[str, Any]]:
    """Return the list of material changes for a single competitor."""
    if previous is None:
        return [
            {
                "competitor": name,
                "app_id": app_id,
                "field": "__new__",
                "before": None,
                "after": current,
                "note": "first time tracking this competitor",
            }
        ]
    changes: List[Dict[str, Any]] = []
    for field in _TEXT_FIELDS:
        before = previous.get(field)
        after = current.get(field)
        if before != after:
            changes.append(
                {
                    "competitor": name,
                    "app_id": app_id,
                    "field": field,
                    "before": before,
                    "after": after,
                }
            )
    before_rating = previous.get("averageUserRating")
    after_rating = current.get("averageUserRating")
    if before_rating is not None and after_rating is not None:
        if abs(float(after_rating) - float(before_rating)) >= rating_delta_threshold:
            changes.append(
                {
                    "competitor": name,
                    "app_id": app_id,
                    "field": "averageUserRating",
                    "before": before_rating,
                    "after": after_rating,
                    "delta": round(float(after_rating) - float(before_rating), 2),
                }
            )
    elif before_rating != after_rating:
        # One side is None and the other isn't — surface it.
        changes.append(
            {
                "competitor": name,
                "app_id": app_id,
                "field": "averageUserRating",
                "before": before_rating,
                "after": after_rating,
            }
        )
    return changes


def load_config(path: Path) -> Dict[str, Any]:
    """Load a watcher JSON config. Validates required fields."""
    raw = json.loads(Path(path).read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError("watcher config must be a JSON object")
    app_name = raw.get("app_name")
    if not app_name or not str(app_name).strip():
        raise ValueError("watcher config is missing required field: app_name")
    competitors = raw.get("competitors") or []
    if not isinstance(competitors, list) or not competitors:
        raise ValueError("watcher config must list at least one competitor")
    for entry in competitors:
        if not isinstance(entry, dict):
            raise ValueError("each competitor must be an object with name + app_id")
        if not entry.get("name") or not entry.get("app_id"):
            raise ValueError(f"competitor missing name or app_id: {entry!r}")
    return raw


def run_watch(
    config_path: Path,
    base_dir: Optional[Path] = None,
    api: Optional[iTunesAPI] = None,
    update_state: bool = False,
    rating_delta_threshold: float = DEFAULT_RATING_DELTA_THRESHOLD,
) -> Dict[str, Any]:
    """Run one watcher pass. Returns a result dict with the change list.

    Parameters
    ----------
    config_path : path to a JSON file (see ``load_config`` for the schema).
    base_dir    : where the StateStore lives. Defaults to ``Path("outputs")``.
    api         : an iTunesAPI instance to fetch competitor data. Injectable
                  for tests.
    update_state : if True, persist the new competitor snapshot back to the
                  StateStore. Workflows should pass True on the scheduled
                  run; ad-hoc CLI invocations may leave it False to preview.
    rating_delta_threshold : minimum absolute change in rating that counts
                             as material. Defaults to 0.1.

    Returns
    -------
    A dict with:
        ``app_name``    — from the config
        ``checked``     — number of competitors fetched
        ``changes``     — list of change records (empty if nothing material)
        ``state_path``  — path of the StateStore file used
        ``state_saved`` — bool, whether update_state actually wrote new state
    """
    config = load_config(config_path)
    app_name = config["app_name"]
    competitors = config["competitors"]
    threshold = float(config.get("rating_delta_threshold", rating_delta_threshold))

    api = api or iTunesAPI(country=str(config.get("country", "us")))
    store = StateStore(app_name, base_dir=base_dir)
    state = store.load()
    previous_by_id = {
        str(entry.get("app_id")): entry
        for entry in (state.get("competitors") or [])
        if isinstance(entry, dict)
    }

    new_snapshots: List[Dict[str, Any]] = []
    all_changes: List[Dict[str, Any]] = []

    for entry in competitors:
        name = entry["name"]
        app_id = str(entry["app_id"])
        live = api.get_app_by_id(app_id)
        if not live:
            all_changes.append(
                {
                    "competitor": name,
                    "app_id": app_id,
                    "field": "__fetch_failed__",
                    "before": previous_by_id.get(app_id),
                    "after": None,
                    "note": "iTunes returned no data for this app_id",
                }
            )
            # Preserve previous snapshot when fetch fails — don't drop it.
            if app_id in previous_by_id:
                new_snapshots.append(previous_by_id[app_id])
            continue

        snap = _snapshot(live)
        snap["name"] = name
        snap["app_id"] = app_id
        new_snapshots.append(snap)

        previous = previous_by_id.get(app_id)
        previous_for_diff = {k: previous.get(k) for k in _TRACKED_FIELDS} if previous else None
        all_changes.extend(_diff_one_competitor(name, app_id, previous_for_diff, snap, threshold))

    state_saved = False
    if update_state:
        store.update(competitors=new_snapshots)
        state_saved = True

    return {
        "app_name": app_name,
        "checked": len(competitors),
        "changes": all_changes,
        "state_path": str(store.path),
        "state_saved": state_saved,
    }


def format_issue_body(result: Dict[str, Any]) -> str:
    """Render the watcher result as a markdown issue body."""
    lines = [
        f"## ASO Watch: {len(result['changes'])} change(s) for `{result['app_name']}`",
        "",
        f"_Checked {result['checked']} competitor(s)._",
        "",
        "| Competitor | Field | Before | After |",
        "|---|---|---|---|",
    ]
    for change in result["changes"]:
        before = "—" if change["before"] is None else f"`{change['before']}`"
        after = "—" if change["after"] is None else f"`{change['after']}`"
        if change["field"] == "__new__":
            before = "_(new)_"
            after = "tracking started"
        lines.append(f"| {change['competitor']} | `{change['field']}` | {before} | {after} |")
    lines.extend(["", "_Generated by aso_skill.watcher._"])
    return "\n".join(lines)
