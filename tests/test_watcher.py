"""Tests for the ASO watcher diff + state-update logic."""

from __future__ import annotations

import json
from pathlib import Path

import pytest

from aso_skill.state import StateStore
from aso_skill.watcher import (
    DEFAULT_RATING_DELTA_THRESHOLD,
    format_issue_body,
    load_config,
    run_watch,
)


class _FakeITunesAPI:
    """Drop-in iTunesAPI replacement for tests. No network."""

    def __init__(self, responses=None):
        self.responses = responses or {}
        self.calls = []

    def get_app_by_id(self, app_id):
        self.calls.append(app_id)
        return self.responses.get(str(app_id))


def _write_config(tmp_path, app_name, competitors, **extra):
    payload = {"app_name": app_name, "competitors": competitors, **extra}
    config_path = tmp_path / "watch.json"
    config_path.write_text(json.dumps(payload), encoding="utf-8")
    return config_path


def test_load_config_rejects_missing_app_name(tmp_path):
    bad = tmp_path / "bad.json"
    bad.write_text(json.dumps({"competitors": [{"name": "x", "app_id": "1"}]}))
    with pytest.raises(ValueError, match="app_name"):
        load_config(bad)


def test_load_config_rejects_empty_competitors(tmp_path):
    bad = tmp_path / "bad.json"
    bad.write_text(json.dumps({"app_name": "TestApp", "competitors": []}))
    with pytest.raises(ValueError, match="competitor"):
        load_config(bad)


def test_load_config_rejects_malformed_competitor(tmp_path):
    bad = tmp_path / "bad.json"
    bad.write_text(json.dumps({"app_name": "TestApp", "competitors": [{"name": "x"}]}))
    with pytest.raises(ValueError, match="app_id"):
        load_config(bad)


def test_first_run_reports_each_competitor_as_new(tmp_path):
    config = _write_config(
        tmp_path,
        "TestApp",
        [{"name": "Todoist", "app_id": "572688855"}],
    )
    api = _FakeITunesAPI(
        {
            "572688855": {
                "trackName": "Todoist",
                "primaryGenreName": "Productivity",
                "version": "1.0.0",
                "sellerName": "Doist",
                "formattedPrice": "Free",
                "averageUserRating": 4.8,
            }
        }
    )
    result = run_watch(config, base_dir=tmp_path, api=api, update_state=True)
    assert result["checked"] == 1
    assert len(result["changes"]) == 1
    assert result["changes"][0]["field"] == "__new__"
    assert result["state_saved"] is True


def test_second_run_with_no_change_returns_empty(tmp_path):
    config = _write_config(
        tmp_path,
        "TestApp",
        [{"name": "Todoist", "app_id": "572688855"}],
    )
    response = {
        "trackName": "Todoist",
        "primaryGenreName": "Productivity",
        "version": "1.0.0",
        "sellerName": "Doist",
        "formattedPrice": "Free",
        "averageUserRating": 4.8,
    }
    api = _FakeITunesAPI({"572688855": response})
    run_watch(config, base_dir=tmp_path, api=api, update_state=True)
    second = run_watch(config, base_dir=tmp_path, api=api, update_state=True)
    assert second["changes"] == []


def test_title_change_detected(tmp_path):
    config = _write_config(
        tmp_path,
        "TestApp",
        [{"name": "Todoist", "app_id": "572688855"}],
    )
    api = _FakeITunesAPI(
        {
            "572688855": {
                "trackName": "Todoist",
                "primaryGenreName": "Productivity",
                "version": "1.0.0",
                "sellerName": "Doist",
                "formattedPrice": "Free",
                "averageUserRating": 4.8,
            }
        }
    )
    run_watch(config, base_dir=tmp_path, api=api, update_state=True)

    api.responses["572688855"]["trackName"] = "Todoist - Premium"
    result = run_watch(config, base_dir=tmp_path, api=api, update_state=True)
    title_changes = [c for c in result["changes"] if c["field"] == "trackName"]
    assert len(title_changes) == 1
    assert title_changes[0]["before"] == "Todoist"
    assert title_changes[0]["after"] == "Todoist - Premium"


def test_small_rating_delta_below_threshold_ignored(tmp_path):
    config = _write_config(
        tmp_path,
        "TestApp",
        [{"name": "Any.do", "app_id": "497328576"}],
        rating_delta_threshold=0.1,
    )
    api = _FakeITunesAPI(
        {
            "497328576": {
                "trackName": "Any.do",
                "version": "1.0",
                "averageUserRating": 4.5,
            }
        }
    )
    run_watch(config, base_dir=tmp_path, api=api, update_state=True)

    api.responses["497328576"]["averageUserRating"] = 4.55  # delta 0.05 < threshold
    result = run_watch(config, base_dir=tmp_path, api=api, update_state=True)
    assert result["changes"] == []


def test_large_rating_delta_above_threshold_reported(tmp_path):
    config = _write_config(
        tmp_path,
        "TestApp",
        [{"name": "Any.do", "app_id": "497328576"}],
        rating_delta_threshold=0.1,
    )
    api = _FakeITunesAPI(
        {
            "497328576": {
                "trackName": "Any.do",
                "version": "1.0",
                "averageUserRating": 4.5,
            }
        }
    )
    run_watch(config, base_dir=tmp_path, api=api, update_state=True)

    api.responses["497328576"]["averageUserRating"] = 4.7  # delta 0.20 > threshold
    result = run_watch(config, base_dir=tmp_path, api=api, update_state=True)
    rating_changes = [c for c in result["changes"] if c["field"] == "averageUserRating"]
    assert len(rating_changes) == 1
    assert rating_changes[0]["delta"] == 0.2


def test_failed_fetch_recorded_and_previous_state_preserved(tmp_path):
    config = _write_config(
        tmp_path,
        "TestApp",
        [{"name": "Ghost", "app_id": "0"}],
    )
    api = _FakeITunesAPI({"0": {"trackName": "Ghost", "version": "1.0", "averageUserRating": 4.0}})
    run_watch(config, base_dir=tmp_path, api=api, update_state=True)

    api.responses["0"] = None  # simulate "not found"
    result = run_watch(config, base_dir=tmp_path, api=api, update_state=True)
    fetch_failures = [c for c in result["changes"] if c["field"] == "__fetch_failed__"]
    assert len(fetch_failures) == 1

    # Previous snapshot should still be present in state after the failed run.
    store = StateStore("TestApp", base_dir=tmp_path)
    saved = store.load()
    assert saved["competitors"] is not None
    assert any(c.get("name") == "Ghost" for c in saved["competitors"])


def test_update_state_false_does_not_persist(tmp_path):
    config = _write_config(
        tmp_path,
        "TestApp",
        [{"name": "Todoist", "app_id": "572688855"}],
    )
    api = _FakeITunesAPI(
        {"572688855": {"trackName": "Todoist", "version": "1.0", "averageUserRating": 4.8}}
    )
    result = run_watch(config, base_dir=tmp_path, api=api, update_state=False)
    assert result["state_saved"] is False
    assert not Path(result["state_path"]).exists()


def test_format_issue_body_includes_summary(tmp_path):
    result = {
        "app_name": "TestApp",
        "checked": 2,
        "changes": [
            {
                "competitor": "Todoist",
                "app_id": "1",
                "field": "trackName",
                "before": "A",
                "after": "B",
            }
        ],
    }
    body = format_issue_body(result)
    assert "ASO Watch" in body
    assert "TestApp" in body
    assert "trackName" in body
    assert "Todoist" in body


def test_default_threshold_is_one_tenth():
    assert DEFAULT_RATING_DELTA_THRESHOLD == 0.1
