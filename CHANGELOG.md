# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.1.3] - Unreleased

### ASO Watcher

- **`aso_skill.watcher`** — new module that diffs competitor metadata
  across time. Reads a JSON config listing competitors, fetches current
  iTunes data, compares against the per-app `StateStore`, and returns the
  list of material changes (title, subtitle, version, seller, price, plus
  rating delta above a configurable threshold; defaults to 0.1). Noisy
  fields like description and `userRatingCount` are deliberately skipped.
- **`aso watch` CLI subcommand** —
  ```text
  aso watch --config .aso-watch.json --update-state --format issue-body
  ```
  Exits 0 when nothing changed, 1 when changes were detected. The
  `issue-body` format renders a markdown table suitable for pasting into
  a GitHub issue.
- **Example workflow** at
  `documentation/workflows/aso-watch-example.yml` — daily GitHub Action
  that downstream repos can copy. Runs `aso watch`, opens an issue when
  changes are detected, and commits the refreshed state back to the
  repo so the next run sees an up-to-date baseline.
- **Example config** at
  `documentation/workflows/aso-watch.example.json` — shows the JSON
  schema (`app_name`, `country`, `rating_delta_threshold`, `competitors`)
  with three sample competitors.
- 12 new tests in `tests/test_watcher.py` covering config validation,
  first-run "new" detection, change detection, rating-threshold
  enforcement, failed-fetch handling, and the issue-body renderer.

---

## [1.1.2] - Unreleased

### Claude Code plugin marketplace listing

- **`.claude-plugin/marketplace.json`** — new marketplace manifest so
  users can install the entire skill (4 agents + 4 slash commands + all
  analytic modules) with two commands:
  ```text
  /plugin marketplace add alirezarezvani/claude-code-aso-skill
  /plugin install aso@aso-skill
  ```
  Paths are mapped to the existing layout via the `skills`, `agents`,
  and `commands` fields — no restructuring of the repo.
- **`README.md`** — install section reordered: plugin marketplace is now
  Option 1 (Recommended), with the manual `cp` instructions, ZIP upload,
  and advanced manual install kept as Options 2-4.

---

## [1.1.1] - Unreleased

### Foundation polish

- **`aso_skill.StateStore`** — new minimal per-app state store. Persists the
  last-known `apple_metadata`, `google_metadata`, `keyword_set`,
  `last_aso_score`, and `competitors` to
  `outputs/<app>/.state/current.json`. Atomic write via tempfile +
  `os.replace`. Schema-versioned (`schema_version: 1`); a future-version
  file raises rather than silently corrupting. 10 new tests.
- **`aso_skill.webfetch_prompts`** — renamed from `scraper.py` to reflect
  what the module actually does (it builds `{url, prompt}` dicts the agent
  feeds into its WebFetch tool — it does no HTTP itself).
  `app-store-optimization/lib/scraper.py` remains as a backward-compat
  symlink, so any external references keep working.
- **Documentation dates** — replaced the 11 hardcoded
  `November 7, 2025` / `Date:` / `Last Updated:` footers in README,
  INSTALL, USAGE, ARCHITECTURE, data_sources.md, the implementation plan,
  branch-protection-setup.md, and CHANGELOG with the current date.
  Historical references (release-tag dates, "Actual Completion: …",
  fixture timestamps in API-response examples) are left intact.

---

## [1.1.0] - Unreleased

### Foundation overhaul — make the skill a real, tested, installable Python package

This release is internal foundation work. There are no agent-contract changes:
the four slash commands (`/aso-full-audit`, `/aso-optimize`, `/aso-prelaunch`,
`/aso-competitor`), the `outputs/[app-name]/` folder layout, and every legacy
file path inside `app-store-optimization/` and `.claude/skills/aso/` continue
to work unchanged.

### Added
- **`aso_skill/` Python package** — canonical home for the eight analytic
  modules (`scorer.py`, `metadata.py`, `keywords.py`, `competitors.py`,
  `ab_test.py`, `localization.py`, `reviews.py`, `checklist.py`) plus
  `itunes.py` and `itunes_cache.py`. Public API is re-exported from
  `aso_skill/__init__.py`. Now properly `pip install`-able.
- **`aso` CLI** — new console script (`pip install -e .` exposes `aso`).
  Subcommands: `score`, `optimize`, `validate`, `keywords`, `ab-test`,
  `checklist`, `itunes {search,app}`. Reads JSON from `--input` or stdin,
  writes JSON to `--output` or stdout. Exit codes: 0 ok, 1 validation
  failure, 2 usage error.
- **`__main__` blocks** on all analytic modules so `python3 aso_scorer.py
  < input.json` works — this fixes the previously-broken agent contract at
  `aso-strategist.md:932`.
- **`pytest` suite** (`tests/`, 50 tests, runs in <3s, stdlib-only) covering
  the scorer math, character-limit validation, A/B significance, CLI
  subprocess invocation, golden-output structural assertions, iTunes cache
  behaviour, and a date-regression guard.
- **iTunes file cache** (`aso_skill/itunes_cache.py`) — 24h TTL by default,
  per-URL keying with `sha1` short hash, stale-fallback on network failure,
  cache dir under `$XDG_CACHE_HOME/aso-skill/itunes/`. Bypass via
  `ASO_ITUNES_NO_CACHE=1`; clear via `aso itunes --clear-cache`.
- **`scripts/materialize_compat.py`** — Windows / ZIP fallback that replaces
  the backward-compat symlinks with real file copies when the filesystem
  doesn't support them.

### Changed
- **`pyproject.toml`** — bumped to 1.1.0, added `[project.scripts]`,
  `[project.optional-dependencies] test`, `[tool.setuptools.packages.find]`,
  `[tool.pytest.ini_options]`. Fixed the silent ruff isort
  `known-first-party` typo (was the hyphenated name, which ruff ignored).
- **`python-quality.yml`** — now lints `aso_skill scripts tests` (the new
  canonical paths) and runs `pytest tests/` across the existing 3.8–3.13
  matrix. Character-limit check rewritten against the dict-form constants.
- **`.claude/skills/aso/`** — converted from a hand-maintained copy (which
  had silently drifted from `app-store-optimization/`) into a directory
  symlink. Drift is now structurally impossible.
- **Legacy hyphenated paths** (`app-store-optimization/aso_scorer.py` and
  the seven sibling .py files plus `lib/itunes_api.py`) are now symlinks
  into `aso_skill/`. Agents that `cd app-store-optimization && python3
  <module>.py` keep working without modification.

### Fixed
- **Hardcoded reference date** in `aso-strategist.md` (lines 27, 237, 1097)
  and `aso-prelaunch.md:66` — replaced with instructions to compute the
  current date via `date -u +%Y-%m-%d` at run time. Previously every
  generated timeline after Nov 2025 referenced past dates.
- **Drift between** `.claude/skills/aso/` and `app-store-optimization/` —
  every analytic file had diverged (different sizes, different content).
  Symlinking ends the drift permanently.
- **Broken agent contract** — `aso-strategist.md:932` invoked
  `python3 aso_scorer.py < /tmp/aso_input.json` against a module without
  any `__main__` block. New main blocks make this command work.

### Migration / breaking changes
- **None for end users.** Every existing path keeps working. ZIP installs,
  `cp -r app-store-optimization ~/.claude/skills/`, agent prompts, and
  `/aso-*` slash commands all continue to function.
- **For contributors:** new code should go in `aso_skill/`, not
  `app-store-optimization/` (which is now a symlink farm).

---

## [1.0.0] - 2025-11-07

### 🎉 Initial Release - Production Ready

First stable release of the ASO Agent System for Claude Code. Complete multi-agent framework for App Store Optimization with real data integration.

### Added

#### Core Agent System
- **aso-master** agent - Orchestrator coordinating all specialist agents (500 lines)
- **aso-research** agent - Keyword research with iTunes API integration (700 lines)
- **aso-optimizer** agent - Metadata generation with character validation (600 lines)
- **aso-strategist** agent - Launch timelines and ongoing optimization (700 lines)
- Total agent code: 2,500+ lines with comprehensive workflows

#### Slash Commands
- `/aso-full-audit [AppName]` - Complete ASO audit (30-40 min workflow)
- `/aso-optimize [AppName]` - Quick metadata optimization (10-15 min)
- `/aso-prelaunch [AppName]` - Pre-launch validation (15-20 min)
- `/aso-competitor [AppName] "Competitors"` - Competitive intelligence (10-15 min)

#### Data Integration
- iTunes Search API wrapper (`itunes_api.py`) - Tested and working
- WebFetch utilities (`scraper.py`) - Additional data scraping
- Real competitor data fetching (no generic recommendations)
- Character limit validation (Apple: 30/30/100, Google: 50/80/4000)

#### Output Structure
- `00-MASTER-ACTION-PLAN.md` - Complete roadmap with ASO health score
- `01-research/` - Keyword research (20 keywords, tiered strategy)
- `02-metadata/` - Copy-paste ready metadata for both platforms
- `03-testing/` - A/B test configuration and monitoring
- `04-launch/` - 47-item pre-launch checklist with timeline
- `05-optimization/` - Review response templates and task schedule
- `FINAL-REPORT.md` - Executive summary

#### Templates
- 6 action checklist templates for all workflow phases
- Master action plan template with ASO scoring
- Platform-specific metadata templates
- A/B testing configuration templates
- Pre-launch validation checklist (47 items)

#### Documentation
- `README.md` - Comprehensive project documentation (540+ lines)
- `LICENSE.md` - MIT License with third-party attributions
- `CHANGELOG.md` - Version history (this file)
- `.claude/ARCHITECTURE.md` - Complete system architecture (509 lines)
- `.claude/INSTALL.md` - Installation guide for 3 scenarios
- `.claude/USAGE.md` - Usage guide with 5 workflows
- `CLAUDE.md` - Quick reference for Claude instances (+280 lines)
- `documentation/implementation/aso-agents-implementation-plan.md` - Development plan (400+ lines)

#### Example Outputs
- Complete FitFlow example workflow (`outputs/FitFlow-example/`)
- Demonstrates all quality standards and deliverables
- ASO health score: 58/100
- 20 priority keywords with implementation guide
- Copy-paste ready metadata with character validation
- Timeline: November 7 - December 1, 2025 (real dates)

#### Distribution
- Standalone skill package (`app-store-optimization/`)
- Agent-integrated version (`.claude/skills/aso/`)
- Distributable ZIP file (`app-store-optimization.zip`)
- Dual structure supporting both direct skill usage and agent coordination

### Technical Details

#### Quality Standards Implemented
- ✅ Character limits validated for both platforms
- ✅ Natural language checking (no keyword stuffing)
- ✅ Real calendar dates (not placeholders)
- ✅ Copy-paste ready content (no formatting needed)
- ✅ Actionable tasks with success criteria
- ✅ Data-backed recommendations (iTunes API)

#### Testing
- iTunes API integration tested successfully
- Test apps: Todoist (4.8★, 120K ratings), Any.do (4.6★, 49K ratings), Microsoft To Do (4.7★, 250K ratings)
- Example workflow validated for quality standards
- All deliverables verified for character counts and actionability

#### Project Statistics
- Total files: 59
- Lines of code: 26,526+
- Agents: 4 (2,500+ lines)
- Python modules: 8 (800+ lines)
- Templates: 6 action checklists
- Slash commands: 4 workflows
- Documentation: 1,500+ lines

### Known Limitations

#### iTunes Search API
- No keyword search volumes (estimated using benchmarks)
- No keyword rankings (must be checked manually)
- No download numbers (estimated only)
- No historical data (current state only)

#### WebFetch
- Slower than API calls (10-30 seconds per page)
- Structure-dependent extraction
- Self-imposed rate limiting

#### User Data Required
- Search volumes should be verified with Apple Search Ads
- Keyword rankings must be tracked manually initially
- Conversion rates tracked via App Store Connect

### Migration Notes

This is the initial release - no migration needed.

### Installation

```bash
# Clone repository
git clone https://github.com/alirezarezvani/claude-code-aso-skill.git
cd claude-code-aso-skill

# Install agents (user-level)
cp .claude/agents/aso/*.md ~/.claude/agents/

# Install slash commands (optional)
cp .claude/commands/aso/*.md ~/.claude/commands/

# Verify
claude --list-agents | grep aso
```

### Upgrade Notes

First release - no upgrade needed.

---

## [Unreleased]

### Planned for v1.1

#### Features
- [ ] iTunes Review API integration for bulk review fetching
- [ ] Historical tracking database for keyword rankings
- [ ] Enhanced A/B test analytics with statistical significance
- [ ] Multi-language support (Spanish, German, French)
- [ ] Automated screenshot text generation
- [ ] App preview video script templates

#### Improvements
- [ ] Faster data fetching with concurrent API calls
- [ ] Enhanced competitor analysis with pricing trends
- [ ] ASO score improvement recommendations
- [ ] Automated metadata refresh scheduling

#### Documentation
- [ ] Video tutorials for common workflows
- [ ] Advanced customization guide
- [ ] Translation of documentation to Spanish, German, French

### Planned for v2.0

#### Major Features
- [ ] Paid ASO API integration (AppTweak, Sensor Tower)
- [ ] Web dashboard for tracking and visualization
- [ ] Automated reporting via email/Slack
- [ ] Team collaboration features
- [ ] Keyword ranking tracking over time
- [ ] Conversion funnel analysis
- [ ] Review sentiment analysis with ML

#### Breaking Changes
- None currently planned

---

## Version History

### [1.0.0] - 2025-11-07
- Initial production release
- Multi-agent system with 4 specialized agents
- iTunes API integration tested
- Complete documentation and examples
- 26,526+ lines of code

---

## Semantic Versioning

This project follows [Semantic Versioning](https://semver.org/):

- **MAJOR** version (X.0.0) - Incompatible API changes
- **MINOR** version (0.X.0) - Backward-compatible functionality additions
- **PATCH** version (0.0.X) - Backward-compatible bug fixes

---

## Support

For questions about this changelog:
- Open an issue: https://github.com/alirezarezvani/claude-code-aso-skill/issues
- Read documentation: `.claude/INSTALL.md` and `.claude/USAGE.md`

---

## Links

- [Homepage](https://github.com/alirezarezvani/claude-code-aso-skill)
- [Documentation](.claude/)
- [Issues](https://github.com/alirezarezvani/claude-code-aso-skill/issues)
- [Releases](https://github.com/alirezarezvani/claude-code-aso-skill/releases)

---

**Maintained by:** Alireza Rezvani
**License:** MIT
**Last Updated:** 2026-05-19
