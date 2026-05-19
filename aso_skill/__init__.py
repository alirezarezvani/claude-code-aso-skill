"""App Store Optimization skill — public Python API.

This package is the canonical source for the eight analytic modules. The legacy
paths under ``app-store-optimization/`` and ``.claude/skills/aso/`` are symlinks
into this package so existing agent prompts (and ZIP-installed copies) keep
working unchanged.
"""

from .ab_test import ABTestPlanner, plan_ab_test
from .checklist import LaunchChecklistGenerator, generate_launch_checklist
from .competitors import CompetitorAnalyzer, analyze_competitor_set
from .itunes import iTunesAPI, fetch_competitor_data
from .itunes_cache import ITunesCache, cached_urlopen
from .keywords import KeywordAnalyzer, analyze_keyword_set
from .localization import LocalizationHelper, plan_localization_strategy
from .metadata import MetadataOptimizer, optimize_app_metadata
from .reviews import ReviewAnalyzer, analyze_reviews
from .scorer import ASOScorer, calculate_aso_score
from .state import StateStore
from .watcher import format_issue_body, load_config, run_watch

__version__ = "1.1.0"

__all__ = [
    "ABTestPlanner",
    "ASOScorer",
    "CompetitorAnalyzer",
    "ITunesCache",
    "KeywordAnalyzer",
    "LaunchChecklistGenerator",
    "LocalizationHelper",
    "MetadataOptimizer",
    "ReviewAnalyzer",
    "StateStore",
    "analyze_competitor_set",
    "analyze_keyword_set",
    "analyze_reviews",
    "cached_urlopen",
    "calculate_aso_score",
    "fetch_competitor_data",
    "format_issue_body",
    "generate_launch_checklist",
    "load_config",
    "iTunesAPI",
    "optimize_app_metadata",
    "plan_ab_test",
    "plan_localization_strategy",
    "run_watch",
    "__version__",
]
