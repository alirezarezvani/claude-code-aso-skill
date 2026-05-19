"""Tests for the MCP server tool handlers.

The MCP SDK is an optional dependency (`pip install 'aso-skill[mcp]'`).
We skip the whole module when it's missing rather than failing the
test suite for users on a stdlib-only install.

These tests exercise the tool handler functions directly -- no event
loop, no Client, no subprocess. The wiring to FastMCP (decorators,
schema generation, stdio transport) is the SDK's concern and is
covered by its own test suite.
"""

from __future__ import annotations

import pytest

pytest.importorskip("mcp", reason="MCP SDK not installed; skip server tests")

from aso_skill import mcp_server  # noqa: E402


SCORE_METADATA = {
    "title_keyword_count": 2,
    "title_length": 28,
    "description_length": 2200,
    "description_quality": 0.8,
    "keyword_density": 4.5,
}
SCORE_RATINGS = {"average_rating": 4.6, "total_ratings": 8500, "recent_ratings_30d": 350}
SCORE_KEYWORDS = {"top_10": 6, "top_50": 18, "top_100": 30, "improving_keywords": 8}
SCORE_CONVERSION = {
    "impression_to_install": 0.06,
    "downloads_last_30_days": 12000,
    "downloads_trend": "up",
}


def test_server_has_expected_name():
    assert mcp_server.mcp.name == "aso-skill"


def test_main_is_callable():
    assert callable(mcp_server.main)


def test_aso_score_returns_overall_score():
    result = mcp_server.aso_score(SCORE_METADATA, SCORE_RATINGS, SCORE_KEYWORDS, SCORE_CONVERSION)
    assert 0 <= result["overall_score"] <= 100
    assert "score_breakdown" in result


def test_aso_validate_valid_apple_title():
    result = mcp_server.aso_validate("apple", "title", "TaskFlow")
    assert result["is_valid"] is True


def test_aso_validate_overlong_apple_title():
    result = mcp_server.aso_validate("apple", "title", "X" * 50)
    assert result["is_valid"] is False
    assert any("exceeds limit" in e for e in result["errors"])


def test_aso_validate_google_short_description():
    result = mcp_server.aso_validate("google", "short_description", "X" * 80)
    assert result["is_valid"] is True


def test_aso_analyze_keywords_returns_dict():
    keywords = [
        {"keyword": "task manager", "search_volume": 50000, "competition": 75, "relevance": 90},
        {"keyword": "ai task planner", "search_volume": 2500, "competition": 25, "relevance": 95},
    ]
    result = mcp_server.aso_analyze_keywords(keywords)
    assert isinstance(result, dict)
    assert len(result) > 0


def test_aso_plan_ab_test_returns_design():
    result = mcp_server.aso_plan_ab_test(
        test_type="icon",
        variant_a={"description": "current icon"},
        variant_b={"description": "new icon with brighter colors"},
        hypothesis="brighter icon will increase tap-through rate",
        baseline_conversion=0.05,
    )
    assert "test_design" in result or "sample_size_requirements" in result


def test_aso_optimize_apple_returns_metadata():
    result = mcp_server.aso_optimize(
        platform="apple",
        app_info={"name": "TaskFlow"},
        target_keywords=["task manager", "productivity"],
    )
    assert result["platform"] == "apple"
    assert "title" in result


def test_aso_itunes_app_returns_error_dict_when_not_found(monkeypatch):
    """No network -- monkeypatch get_app_by_id to return None."""
    monkeypatch.setattr(
        mcp_server.iTunesAPI,
        "get_app_by_id",
        lambda self, app_id: None,
    )
    result = mcp_server.aso_itunes_app("0")
    assert "error" in result


def test_aso_itunes_search_returns_results_field(monkeypatch):
    """No network -- monkeypatch search_apps with a fake response."""
    monkeypatch.setattr(
        mcp_server.iTunesAPI,
        "search_apps",
        lambda self, term, limit=10, entity="software": {
            "resultCount": 1,
            "results": [{"trackName": term.title()}],
        },
    )
    result = mcp_server.aso_itunes_search("todoist", limit=1)
    assert result["resultCount"] == 1
    assert result["results"][0]["trackName"] == "Todoist"


def test_all_tools_registered_on_server():
    """Smoke-check that every handler we defined is reachable via FastMCP."""
    expected = {
        "aso_score",
        "aso_optimize",
        "aso_validate",
        "aso_analyze_keywords",
        "aso_plan_ab_test",
        "aso_itunes_search",
        "aso_itunes_app",
    }
    # FastMCP stores tools in a private dict; using its public iteration
    # surface is the stable API.
    import asyncio

    tools = asyncio.run(mcp_server.mcp.list_tools())
    registered = {t.name for t in tools}
    missing = expected - registered
    assert not missing, f"missing tools: {missing}"
