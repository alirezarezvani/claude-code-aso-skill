"""MCP server exposing the ASO analyzers as tools.

Install the optional dependency::

    pip install 'aso-skill[mcp]'

Then run::

    aso-mcp        # via the console-script entry point
    # or
    python -m aso_skill.mcp_server

For Claude Desktop, drop this into ``claude_desktop_config.json``::

    {"mcpServers": {"aso-skill": {"command": "aso-mcp"}}}

The server speaks MCP over stdio (default transport). Tools wrap the
existing convenience functions in :mod:`aso_skill`, so any caller that
can speak MCP -- Claude Desktop, Cursor, Continue, custom clients -- can
score apps, validate metadata, and search iTunes without depending on
Claude Code itself.
"""

from __future__ import annotations

from typing import Any, Dict, List

from mcp.server.fastmcp import FastMCP

from . import (
    MetadataOptimizer,
    analyze_keyword_set,
    calculate_aso_score,
    iTunesAPI,
    optimize_app_metadata,
    plan_ab_test,
)

mcp = FastMCP("aso-skill")


@mcp.tool()
def aso_score(
    metadata: Dict[str, Any],
    ratings: Dict[str, Any],
    keyword_performance: Dict[str, Any],
    conversion: Dict[str, Any],
) -> Dict[str, Any]:
    """Compute an ASO health score (0-100) across four dimensions.

    Inputs are dicts matching the schemas the underlying scorer expects:

    metadata: ``{title_keyword_count, title_length, description_length,
        description_quality (0-1), keyword_density}``

    ratings: ``{average_rating, total_ratings, recent_ratings_30d}``

    keyword_performance: ``{top_10, top_50, top_100, improving_keywords}``

    conversion: ``{impression_to_install, downloads_last_30_days,
        downloads_trend (one of 'up' | 'stable' | 'down')}``

    Returns the overall score plus a per-component breakdown
    (metadata_quality, ratings_reviews, keyword_performance,
    conversion_metrics) and prioritized recommendations.
    """
    return calculate_aso_score(metadata, ratings, keyword_performance, conversion)


@mcp.tool()
def aso_optimize(
    platform: str, app_info: Dict[str, Any], target_keywords: List[str]
) -> Dict[str, Any]:
    """Generate optimized title, description, and (Apple only) keyword field.

    ``platform`` must be ``"apple"`` or ``"google"``. ``app_info`` needs at
    least ``{"name": "..."}`` plus optional ``category``, ``features``, etc.
    ``target_keywords`` is the prioritized keyword list to weave into the
    metadata. Output is validated against the platform's character limits.
    """
    return optimize_app_metadata(platform, app_info, target_keywords)


@mcp.tool()
def aso_validate(platform: str, field: str, value: str) -> Dict[str, Any]:
    """Validate a single metadata field against platform character limits.

    ``platform``: ``"apple"`` or ``"google"``.
    ``field``: ``"title"``, ``"subtitle"``, ``"description"``, ``"keywords"``,
    ``"short_description"``, ``"promotional_text"``, etc. (the exact set
    depends on platform).
    ``value``: the text to check.

    Returns a report with ``is_valid``, ``errors``, ``warnings``, and a
    per-field status block containing ``length``, ``limit``, ``remaining``,
    and ``usage_percentage``.
    """
    optimizer = MetadataOptimizer(platform)
    return optimizer.validate_character_limits({field: value})


@mcp.tool()
def aso_analyze_keywords(keywords_data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Rank a set of keywords by ASO potential.

    Each entry in ``keywords_data`` is ``{keyword, search_volume,
    competition (0-100), relevance (0-100)}``. The analyzer scores each
    keyword on potential, flags long-tail opportunities (low competition,
    high relevance), and returns a prioritized ranking plus a written
    summary.
    """
    return analyze_keyword_set(keywords_data)


@mcp.tool()
def aso_plan_ab_test(
    test_type: str,
    variant_a: Dict[str, Any],
    variant_b: Dict[str, Any],
    hypothesis: str,
    baseline_conversion: float,
) -> Dict[str, Any]:
    """Design an A/B test with a statistically-rigorous sample size.

    ``test_type``: an identifier like ``"icon"``, ``"screenshots"``,
    ``"title"`` -- used to look up a reasonable minimum-detectable-effect.
    ``variant_a`` / ``variant_b``: free-form dicts describing what each
    variant changes. ``hypothesis``: one-sentence prediction.
    ``baseline_conversion``: current conversion rate as a decimal (e.g.
    0.05 for 5%).

    Returns the test design plus a sample-size calculation with duration
    estimates at typical traffic levels.
    """
    return plan_ab_test(test_type, variant_a, variant_b, hypothesis, baseline_conversion)


@mcp.tool()
def aso_itunes_search(term: str, limit: int = 10, country: str = "us") -> Dict[str, Any]:
    """Search the iTunes App Store for apps matching a keyword.

    Uses the cached iTunes wrapper -- repeated calls within 24h hit a
    local cache instead of the API. Returns the raw iTunes response with
    ``resultCount`` and a ``results`` list. Each result includes
    ``trackName``, ``primaryGenreName``, ``averageUserRating``,
    ``userRatingCount``, ``version``, ``trackViewUrl`` and the standard
    iTunes metadata blob.
    """
    api = iTunesAPI(country=country)
    return api.search_apps(term, limit=limit)


@mcp.tool()
def aso_itunes_app(app_id: str, country: str = "us") -> Dict[str, Any]:
    """Fetch a single iTunes app by its App Store ID.

    Useful when you already know the app and want its current metadata
    (rating, version, description, screenshots) for comparison or
    competitor analysis. Returns ``{"error": "..."}`` if no app is found
    for the given id in the requested country.
    """
    api = iTunesAPI(country=country)
    result = api.get_app_by_id(app_id)
    return result if result else {"error": f"app {app_id} not found"}


def main() -> None:
    """Console-script entry point. Runs the server over stdio."""
    mcp.run()


if __name__ == "__main__":
    main()
