# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a **Claude Code skill repository** containing the "app-store-optimization" skill. This skill provides comprehensive ASO capabilities for mobile app developers and marketers to optimize app presence on Apple App Store and Google Play Store.

## Skill Installation

### User-Level Installation (Available in All Projects)
```bash
cp -r app-store-optimization ~/.claude/skills/
```

### Project-Level Installation
```bash
cp -r app-store-optimization /path/to/project/.claude/skills/
```

### Verification
```bash
ls ~/.claude/skills/app-store-optimization/
# Should show: SKILL.md, 8 Python modules, sample files, documentation
```

## Architecture

### Core Modules (8 Python Scripts)

**keyword_analyzer.py** (13KB)
- Analyzes keywords for search volume, competition, relevance
- Key: `analyze_keyword()`, `compare_keywords()`, `find_long_tail_opportunities()`

**metadata_optimizer.py** (20KB)
- Optimizes titles, descriptions, keyword fields with platform-specific limits
- Key: `optimize_title()`, `optimize_description()`, `validate_character_limits()`

**competitor_analyzer.py** (21KB)
- Analyzes competitor ASO strategies, identifies gaps
- Key: `analyze_competitor()`, `compare_competitors()`, `identify_gaps()`

**aso_scorer.py** (19KB)
- Calculates 0-100 ASO health score across metadata, ratings, keywords, conversion
- Key: `calculate_overall_score()`, `generate_recommendations()`

**ab_test_planner.py** (23KB)
- Plans and tracks A/B tests with statistical significance
- Key: `design_test()`, `calculate_sample_size()`, `calculate_significance()`

**localization_helper.py** (22KB)
- Manages multi-language optimization, ROI analysis
- Key: `identify_target_markets()`, `translate_metadata()`, `calculate_localization_roi()`

**review_analyzer.py** (26KB)
- Analyzes user reviews for sentiment, issues, feature requests
- Key: `analyze_sentiment()`, `extract_common_themes()`, `generate_response_templates()`

**launch_checklist.py** (29KB)
- Generates pre-launch checklists, compliance validation, timing optimization
- Key: `generate_prelaunch_checklist()`, `optimize_launch_timing()`

### Platform Constraints (Critical)

**Apple App Store:**
- Title: 30 chars
- Subtitle: 30 chars
- Promotional Text: 170 chars
- Description: 4000 chars
- Keywords: 100 chars (comma-separated, no spaces)

**Google Play Store:**
- Title: 50 chars
- Short Description: 80 chars
- Full Description: 4000 chars
- No keyword field (extracted from title/description)

### Data Flow

Input (JSON) → Python Module → Analysis → Output (JSON)
- `sample_input.json`: Example request structure
- `expected_output.json`: Example response with keyword analysis, metadata recommendations

## Working with This Repository

### DO NOT Modify
- Python modules are production-ready (no external dependencies, Python 3.7+)
- SKILL.md is the skill specification file
- Character limit validation is critical for platform compliance

### Development Tasks
When asked to improve or extend this skill:

1. **Adding New Functions**: Add to existing modules maintaining consistency
2. **New Modules**: Create new .py file in `app-store-optimization/` with similar structure
3. **Testing**: Verify against platform character limits (Apple: 30/30/170/100/4000, Google: 50/80/4000)
4. **Documentation**: Update SKILL.md, README.md, HOW_TO_USE.md

### Testing Changes
```bash
cd app-store-optimization
python3 keyword_analyzer.py  # Basic syntax check
python3 metadata_optimizer.py
# Test character limit validation with sample data
```

## Common Use Cases

**Keyword Research:**
User provides app name, category, features → `keyword_analyzer.py` → prioritized keyword list

**Metadata Optimization:**
User provides app info → `metadata_optimizer.py` → platform-specific titles/descriptions with character validation

**ASO Health Check:**
User provides metrics (ratings, keyword rankings, conversion) → `aso_scorer.py` → 0-100 score + recommendations

**Pre-Launch:**
User provides launch date → `launch_checklist.py` → comprehensive checklist for both stores

## Critical Design Principles

1. **Zero External Dependencies**: Standard library only for portability
2. **Platform Compliance**: Always validate character limits
3. **Dual Platform**: Support both Apple App Store and Google Play Store
4. **Actionable Outputs**: Provide specific recommendations, not generic advice
5. **Statistical Rigor**: A/B testing requires proper sample size and significance calculations

## Key Differentiators

- **AI Keyword Focus**: Skill emphasizes finding "AI prioritization" opportunities (low competition, high relevance)
- **Long-Tail Strategy**: Identifies 3-4 word phrases with lower competition
- **Character Limit Enforcement**: Prevents non-compliant metadata submissions
- **No Paid Acquisition**: Focuses exclusively on organic ASO (no Apple Search Ads, Google Ads)

## Version Info

**Current Version**: 1.0.0 (November 7, 2025)
**Platform Requirements**: Current as of November 2025
**Python**: 3.7+
**Target Users**: App developers, app marketers, indie developers, ASO specialists

---

## ASO Agent System (NEW)

### Overview

The ASO skill has been extended with a **4-agent system** that provides end-to-end app store optimization with real data fetching and actionable deliverables. Agents coordinate to produce comprehensive ASO plans that users can execute step-by-step.

### Dual Structure Architecture

This project maintains **two versions** of the ASO skill:

**1. Standalone Skill (Distributable)**
- **Location:** `app-store-optimization/`
- **Purpose:** Standalone skill package users can install to `~/.claude/skills/`
- **Use Case:** Direct skill usage without agents
- **Distribution:** Copy this folder to share the skill

**2. Agent-Integrated Skill (Project-Specific)**
- **Location:** `.claude/skills/aso/`
- **Purpose:** Used by ASO agents for coordinated workflows
- **Use Case:** Agent-orchestrated ASO audits via `/aso-full-audit`
- **Integration:** Agents reference Python modules from this location

**Why Two Copies?**
- Maintains backward compatibility with standalone skill usage
- Provides clean separation: skill as tool vs skill as agent resource
- Allows distribution of standalone skill without agent dependencies

**Keeping Synchronized:**
```bash
# When updating Python modules, sync both:
cp -r app-store-optimization/* .claude/skills/aso/
```

**See:** `.claude/skills/aso/AGENT-INTEGRATION.md` for detailed explanation

### Agent Architecture (4 Agents)

**aso-master** (Orchestrator)
- **Location:** `.claude/agents/aso/aso-master.md`
- **Model:** opus
- **Tools:** Read, Write, Edit, Bash, Grep, Glob
- **Role:** Coordinates all 3 specialist agents, synthesizes outputs into master action plan
- **Output:** `outputs/[app-name]/00-MASTER-ACTION-PLAN.md`

**aso-research** (Research + Data Fetching)
- **Location:** `.claude/agents/aso/aso-research.md`
- **Model:** opus
- **Tools:** Read, Write, Edit, Bash, Grep, Glob, WebFetch, WebSearch
- **Role:** Fetches real competitor data via iTunes API, performs keyword analysis
- **Data Sources:** iTunes Search API (free), WebFetch scraping
- **Outputs:** `keyword-list.md`, `competitor-gaps.md`, `action-research.md`

**aso-optimizer** (Metadata Generation)
- **Location:** `.claude/agents/aso/aso-optimizer.md`
- **Model:** sonnet
- **Tools:** Read, Write, Edit, Bash, Grep, Glob
- **Role:** Generates copy-paste ready metadata for both platforms
- **Outputs:** `apple-metadata.md`, `google-metadata.md`, `ab-test-setup.md`

**aso-strategist** (Strategy + Timelines)
- **Location:** `.claude/agents/aso/aso-strategist.md`
- **Model:** opus
- **Tools:** Read, Write, Edit, Bash, Grep, Glob
- **Role:** Creates launch timelines, checklists, review response templates
- **Outputs:** `prelaunch-checklist.md`, `timeline.md`, `review-responses.md`, `ongoing-tasks.md`

### Agent Workflow

```
User Request → aso-master (orchestrator)
    ↓
Phase 1: aso-research (10-15 min)
    - Fetch competitor data (iTunes API)
    - Analyze keywords
    - Identify competitive gaps
    ↓
Phase 2: aso-optimizer (5-7 min)
    - Generate Apple metadata (validated)
    - Generate Google metadata (validated)
    - Create A/B testing strategy
    ↓
Phase 3: aso-strategist (8-10 min)
    - Create pre-launch checklist (47 items)
    - Build timeline with specific dates
    - Generate review response templates
    ↓
Phase 4: aso-master synthesis (5 min)
    - Consolidate all outputs
    - Create master action plan
    - Validate completeness
    ↓
Deliverable: Complete action plan in outputs/[app-name]/
```

### Slash Commands

**Location:** `.claude/commands/aso/`

- **`/aso-full-audit [app-name]`** - Complete ASO audit (30-40 min)
- **`/aso-optimize [app-name]`** - Quick metadata optimization (5-7 min)
- **`/aso-prelaunch [app-name] [launch-date]`** - Launch planning (8-10 min)
- **`/aso-competitor [app-name] [competitors]`** - Competitive intelligence (10-15 min)

### Output Structure

All agent outputs are saved to `outputs/[app-name]/`:

```
outputs/[app-name]/
├── 00-MASTER-ACTION-PLAN.md    # START HERE - consolidated checklist
├── 01-research/
│   ├── keyword-list.md          # Prioritized keywords with implementation guide
│   ├── competitor-gaps.md       # Opportunities competitors miss
│   └── action-research.md       # Research task checklist
├── 02-metadata/
│   ├── apple-metadata.md        # Copy-paste ready for App Store Connect
│   ├── google-metadata.md       # Copy-paste ready for Play Console
│   ├── visual-assets-spec.md    # Icon/screenshot requirements
│   └── action-metadata.md       # Implementation checklist
├── 03-testing/
│   ├── ab-test-setup.md         # Step-by-step A/B test configuration
│   └── action-testing.md        # Testing tasks
├── 04-launch/
│   ├── prelaunch-checklist.md   # 47-item validation checklist
│   ├── timeline.md              # Week-by-week with specific dates
│   ├── submission-guide.md      # Platform submission steps
│   └── action-launch.md         # Launch execution tasks
├── 05-optimization/
│   ├── review-responses.md      # Pre-written response templates
│   ├── ongoing-tasks.md         # Daily/weekly/monthly schedule
│   └── action-optimization.md   # Ongoing optimization tasks
└── FINAL-REPORT.md              # Executive summary
```

### Data Sources

**Primary: iTunes Search API**
- **Location:** `app-store-optimization/lib/itunes_api.py`
- **Status:** Free, official Apple API
- **Data:** App metadata, ratings, screenshots, categories
- **Limitations:** No search volumes, no keyword rankings

**Secondary: WebFetch Scraping**
- **Location:** `app-store-optimization/lib/scraper.py`
- **Usage:** Fallback when iTunes API insufficient
- **Data:** Visual assessment, "What's New" text, keyword rankings
- **Limitations:** Slower, less reliable, page structure dependent

**Tertiary: User-Provided**
- **Usage:** Last resort when APIs fail
- **Data:** Search volume estimates, keyword rankings, conversion rates
- **Documentation:** See `app-store-optimization/lib/data_sources.md`

### Key Features

1. **Real Data Fetching:** iTunes API integration (no manual data entry)
2. **Actionable Outputs:** Copy-paste ready metadata, step-by-step checklists
3. **Specific Dates:** Timelines use actual calendar dates (not "Week 1")
4. **Platform Compliance:** All metadata validated against character limits
5. **Sequential Coordination:** Research → Optimization → Strategy → Synthesis
6. **Quality Validation:** Each agent validates outputs before handoff

### Installation

**For Users (to ~/.claude/agents/):**
```bash
# Copy agent definitions
cp .claude/agents/aso/*.md ~/.claude/agents/

# Copy slash commands (optional)
cp .claude/commands/aso/*.md ~/.claude/commands/

# Verify installation
ls ~/.claude/agents/aso-*
# Should show: aso-master.md, aso-research.md, aso-optimizer.md, aso-strategist.md
```

**See:** `.claude/INSTALL.md` for detailed instructions

### Usage Examples

**Example 1: Full ASO Audit**
```
User: /aso-full-audit TaskFlow

aso-master will:
1. Gather app details (category, features, platforms, launch date)
2. Invoke aso-research (fetch Todoist, Any.do, Microsoft To Do data)
3. Invoke aso-optimizer (generate Apple + Google metadata)
4. Invoke aso-strategist (create timeline Nov 7 → Dec 15, 2025)
5. Create master action plan

Output: outputs/TaskFlow/00-MASTER-ACTION-PLAN.md
Time: 30-40 minutes
```

**Example 2: Quick Metadata Update**
```
User: /aso-optimize MyApp

aso-optimizer will:
1. Ask for app details and keywords
2. Generate Apple metadata (title 28/30 chars, subtitle 29/30 chars, etc.)
3. Generate Google metadata (title 45/50 chars, short desc 78/80 chars, etc.)
4. Validate all character limits
5. Create A/B testing recommendations

Output: outputs/MyApp/02-metadata/
Time: 5-7 minutes
```

### Important Files

**Implementation Plan:**
- `documentation/implementation/aso-agents-implementation-plan.md` (400+ lines)
- Complete breakdown of all phases, tasks, validation criteria

**Agent Definitions:**
- `.claude/agents/aso/aso-master.md` (500 lines)
- `.claude/agents/aso/aso-research.md` (700 lines)
- `.claude/agents/aso/aso-optimizer.md` (600 lines)
- `.claude/agents/aso/aso-strategist.md` (700 lines)

**Data Fetching:**
- `app-store-optimization/lib/itunes_api.py` (Python API wrapper)
- `app-store-optimization/lib/scraper.py` (WebFetch utilities)
- `app-store-optimization/lib/data_sources.md` (Complete documentation)

**Slash Commands:**
- `.claude/commands/aso/aso-full-audit.md`
- `.claude/commands/aso/aso-optimize.md`
- `.claude/commands/aso/aso-prelaunch.md`
- `.claude/commands/aso/aso-competitor.md`

### Development Guidelines

**When Working with Agents:**

1. **Read agent definitions first** - They contain comprehensive protocols
2. **Follow Universal Agent Protocol** - Pre-work → Execution → Verification
3. **Validate character limits** - ALWAYS check platform constraints
4. **Document data sources** - Note iTunes API vs WebFetch vs user estimates
5. **Use real dates** - Never "Week 1", always "November 7-13, 2025"
6. **Generate actionable outputs** - Copy-paste ready metadata, specific tasks

**Agent Coordination Rules:**

- **Sequential only** - Research → Optimizer → Strategist (data dependencies)
- **Validation gates** - Each agent validates before handoff
- **Quality self-assessment** - Agents rate their work (must be ≥4/5)
- **Error handling** - If API fails, fallback to WebFetch, then user data

**File Creation Rules:**

- **All outputs** → `outputs/[app-name]/`
- **No root files** - Never create files in project root
- **Structured folders** - Follow 01-research/, 02-metadata/, etc.
- **Action checklists** - Every phase has action-*.md with tasks

### Testing Agents

**Test with sample app:**
```bash
# Invoke aso-master with test data
# App: "FitFlow" (fitness app)
# Category: Health & Fitness
# Features: AI workout plans, nutrition tracking
# Competitors: Nike Training Club, Peloton
# Platform: Both (Apple + Google)
# Launch: December 15, 2025

# Validate outputs:
ls outputs/FitFlow/
# Should show: 00-MASTER-ACTION-PLAN.md + 5 phase folders + FINAL-REPORT.md
```

### Success Criteria

- ✅ All 4 agents follow Universal Agent Protocol
- ✅ iTunes API integration working (real competitor data)
- ✅ Metadata validated against character limits (100% compliance)
- ✅ Timelines use specific dates (not placeholders)
- ✅ Action checklists are executable (no vague tasks)
- ✅ Master plan consolidates all outputs
- ✅ Documentation complete (INSTALL.md, USAGE.md)

### Next Steps

1. **Install agents** - Copy to ~/.claude/agents/
2. **Test workflow** - Run `/aso-full-audit TestApp`
3. **Review outputs** - Check outputs/TestApp/
4. **Validate quality** - Ensure actionability ≥4/5
5. **Use for real app** - Apply to actual app launch

### Support

**Documentation:**
- Implementation plan: `documentation/implementation/aso-agents-implementation-plan.md`
- Data sources: `app-store-optimization/lib/data_sources.md`
- Installation: `.claude/INSTALL.md`
- Usage: `.claude/USAGE.md`

**Questions:**
- Review agent definitions for detailed protocols
- Check implementation plan for phase breakdowns
- See data_sources.md for API limitations
