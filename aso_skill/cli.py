"""Command-line interface for the ASO skill.

Usage:
    aso score --input metrics.json
    aso optimize --input app.json [--output out.json]
    aso validate --platform apple --field title --value "TaskFlow"
    aso keywords --input keywords.json
    aso ab-test --input test.json
    aso checklist --input app.json
    aso itunes search --term todoist [--limit 10] [--no-cache]
    aso itunes app --id 572688855

All ``--input`` paths accept ``-`` for stdin. JSON output goes to stdout (or
``--output PATH``). Exit codes: 0 ok, 1 validation failure, 2 usage error.
"""

from __future__ import annotations

import argparse
import json
import sys
from typing import Any, Callable, List, Optional


def _read_input(path: Optional[str]) -> Any:
    if path is None or path == "-":
        raw = sys.stdin.read()
        if not raw.strip():
            sys.exit("Error: no JSON provided on stdin")
        return json.loads(raw)
    with open(path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def _write_output(result: Any, path: Optional[str]) -> None:
    serialised = json.dumps(result, indent=2, default=str)
    if path is None or path == "-":
        sys.stdout.write(serialised + "\n")
    else:
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(serialised + "\n")


def _cmd_score(args: argparse.Namespace) -> int:
    from .scorer import calculate_aso_score

    payload = _read_input(args.input)
    if not isinstance(payload, dict):
        sys.stderr.write("Error: score input must be a JSON object\n")
        return 2
    _write_output(calculate_aso_score(**payload), args.output)
    return 0


def _cmd_optimize(args: argparse.Namespace) -> int:
    from .metadata import optimize_app_metadata

    payload = _read_input(args.input)
    if not isinstance(payload, dict):
        sys.stderr.write("Error: optimize input must be a JSON object\n")
        return 2
    if args.platform:
        payload["platform"] = args.platform
    _write_output(optimize_app_metadata(**payload), args.output)
    return 0


def _cmd_validate(args: argparse.Namespace) -> int:
    from .metadata import MetadataOptimizer

    optimizer = MetadataOptimizer(args.platform)
    field = args.field
    value = args.value
    if value is None:
        value = sys.stdin.read().rstrip("\n")
    result = optimizer.validate_character_limits({field: value})
    _write_output(result, args.output)
    if result.get("is_valid") is False:
        return 1
    return 0


def _cmd_keywords(args: argparse.Namespace) -> int:
    from .keywords import analyze_keyword_set

    payload = _read_input(args.input)
    if isinstance(payload, list):
        payload = {"keywords_data": payload}
    if not isinstance(payload, dict):
        sys.stderr.write("Error: keywords input must be a JSON list or object\n")
        return 2
    _write_output(analyze_keyword_set(**payload), args.output)
    return 0


def _cmd_ab_test(args: argparse.Namespace) -> int:
    from .ab_test import plan_ab_test

    payload = _read_input(args.input)
    if not isinstance(payload, dict):
        sys.stderr.write("Error: ab-test input must be a JSON object\n")
        return 2
    _write_output(plan_ab_test(**payload), args.output)
    return 0


def _cmd_checklist(args: argparse.Namespace) -> int:
    from .checklist import generate_launch_checklist

    payload = _read_input(args.input)
    if not isinstance(payload, dict):
        sys.stderr.write("Error: checklist input must be a JSON object\n")
        return 2
    if args.platform:
        payload["platform"] = args.platform
    _write_output(generate_launch_checklist(**payload), args.output)
    return 0


def _cmd_itunes(args: argparse.Namespace) -> int:
    import os

    from .itunes import iTunesAPI
    from .itunes_cache import ITunesCache

    if args.no_cache:
        os.environ["ASO_ITUNES_NO_CACHE"] = "1"
    if args.clear_cache:
        removed = ITunesCache().clear()
        sys.stderr.write(f"Cleared {removed} cache file(s)\n")
        return 0
    api = iTunesAPI(country=args.country)
    if args.itunes_command == "search":
        result = api.search_apps(args.term, limit=args.limit)
    elif args.itunes_command == "app":
        result = api.get_app_by_id(args.id) or {"error": f"app {args.id} not found"}
    else:
        sys.stderr.write("Error: itunes requires a subcommand (search | app)\n")
        return 2
    _write_output(result, args.output)
    return 0


def _cmd_watch(args: argparse.Namespace) -> int:
    """Run one ASO watcher pass against a config file."""
    from pathlib import Path

    from .watcher import format_issue_body, run_watch

    config_path = Path(args.config)
    if not config_path.is_file():
        sys.stderr.write(f"Error: watcher config not found: {config_path}\n")
        return 2

    result = run_watch(
        config_path=config_path,
        update_state=args.update_state,
    )

    if args.format == "issue-body":
        body = format_issue_body(result)
        if args.output:
            Path(args.output).write_text(body + "\n", encoding="utf-8")
        else:
            sys.stdout.write(body + "\n")
    else:
        _write_output(result, args.output)

    return 1 if result["changes"] else 0


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="aso", description="App Store Optimization toolkit")
    parser.add_argument("--version", action="version", version=_version())
    sub = parser.add_subparsers(dest="command", required=True)

    p_score = sub.add_parser("score", help="Calculate ASO health score (0-100)")
    p_score.add_argument("--input", "-i", default="-", help="JSON file path (or - for stdin)")
    p_score.add_argument("--output", "-o", default=None, help="Output path (default: stdout)")
    p_score.set_defaults(func=_cmd_score)

    p_opt = sub.add_parser("optimize", help="Generate optimized metadata for a platform")
    p_opt.add_argument("--input", "-i", default="-")
    p_opt.add_argument("--output", "-o", default=None)
    p_opt.add_argument("--platform", choices=["apple", "google"], default=None)
    p_opt.set_defaults(func=_cmd_optimize)

    p_val = sub.add_parser("validate", help="Validate a metadata field against character limits")
    p_val.add_argument("--platform", choices=["apple", "google"], required=True)
    p_val.add_argument(
        "--field",
        choices=[
            "title",
            "subtitle",
            "description",
            "keywords",
            "short_description",
            "promotional_text",
        ],
        required=True,
    )
    p_val.add_argument("--value", default=None, help="Field value (omit to read from stdin)")
    p_val.add_argument("--output", "-o", default=None)
    p_val.set_defaults(func=_cmd_validate)

    p_kw = sub.add_parser("keywords", help="Analyze a keyword set")
    p_kw.add_argument("--input", "-i", default="-")
    p_kw.add_argument("--output", "-o", default=None)
    p_kw.set_defaults(func=_cmd_keywords)

    p_ab = sub.add_parser("ab-test", help="Plan an A/B test")
    p_ab.add_argument("--input", "-i", default="-")
    p_ab.add_argument("--output", "-o", default=None)
    p_ab.set_defaults(func=_cmd_ab_test)

    p_cl = sub.add_parser("checklist", help="Generate pre-launch checklist")
    p_cl.add_argument("--input", "-i", default="-")
    p_cl.add_argument("--output", "-o", default=None)
    p_cl.add_argument("--platform", choices=["apple", "google", "both"], default=None)
    p_cl.set_defaults(func=_cmd_checklist)

    p_it = sub.add_parser("itunes", help="Query iTunes Search API (cached)")
    p_it.add_argument("--country", default="us")
    p_it.add_argument("--no-cache", action="store_true")
    p_it.add_argument("--clear-cache", action="store_true")
    p_it.add_argument("--output", "-o", default=None)
    it_sub = p_it.add_subparsers(dest="itunes_command")
    p_it_search = it_sub.add_parser("search", help="Search apps by term")
    p_it_search.add_argument("--term", required=True)
    p_it_search.add_argument("--limit", type=int, default=10)
    p_it_app = it_sub.add_parser("app", help="Get app by ID")
    p_it_app.add_argument("--id", required=True)
    p_it.set_defaults(func=_cmd_itunes)

    p_wa = sub.add_parser(
        "watch",
        help="Diff competitor metadata against last-known state",
    )
    p_wa.add_argument("--config", required=True, help="Path to watcher JSON config")
    p_wa.add_argument(
        "--update-state",
        action="store_true",
        help="Persist the new competitor snapshot back to the StateStore",
    )
    p_wa.add_argument(
        "--format",
        choices=["json", "issue-body"],
        default="json",
        help="Output format. 'issue-body' renders markdown suitable for a GitHub issue.",
    )
    p_wa.add_argument("--output", "-o", default=None)
    p_wa.set_defaults(func=_cmd_watch)

    return parser


def _version() -> str:
    try:
        from . import __version__

        return f"aso {__version__}"
    except ImportError:
        return "aso (unknown version)"


def main(argv: Optional[List[str]] = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)
    func: Callable[[argparse.Namespace], int] = args.func
    try:
        return func(args)
    except json.JSONDecodeError as exc:
        sys.stderr.write(f"Error: invalid JSON input: {exc}\n")
        return 2
    except FileNotFoundError as exc:
        sys.stderr.write(f"Error: {exc}\n")
        return 2
    except TypeError as exc:
        sys.stderr.write(f"Error: bad input shape: {exc}\n")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
