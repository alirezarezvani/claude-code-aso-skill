# ASO Agent System Architecture

**Project:** aeo-skill
**Version:** 1.0
**Date:** November 7, 2025

---

## System Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    ASO Agent System                              │
│                                                                   │
│  Standalone Skill ←─────→ Agent System ←─────→ User Outputs    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Architecture Layers

### Layer 1: Standalone Skill (Distributable)

**Location:** `app-store-optimization/`

```
app-store-optimization/
├── SKILL.md                      # Skill definition for Claude Code
├── keyword_analyzer.py           # Keyword research module
├── competitor_analyzer.py        # Competitor intelligence
├── metadata_optimizer.py         # Metadata generation
├── aso_scorer.py                 # ASO health scoring
├── ab_test_planner.py            # A/B testing strategy
├── localization_helper.py        # Multi-language optimization
├── review_analyzer.py            # Review sentiment analysis
├── launch_checklist.py           # Pre-launch validation
└── lib/                          # Data fetching utilities
    ├── itunes_api.py             # iTunes Search API wrapper
    ├── scraper.py                # WebFetch utilities
    └── data_sources.md           # Data source documentation
```

**Usage:**
```bash
# Users install skill globally
cp -r app-store-optimization ~/.claude/skills/

# Direct skill invocation
"Hey Claude—I just added the app-store-optimization skill.
 Can you research keywords for my productivity app?"

# Claude uses Python modules directly
```

**Characteristics:**
- ✅ Self-contained
- ✅ No dependencies on agents
- ✅ Distributable
- ✅ Works with Claude Code skill system

---

### Layer 2: Agent-Integrated Skill (Project-Specific)

**Location:** `.claude/skills/aso/`

```
.claude/skills/aso/
├── SKILL.md                      # Same as standalone
├── *.py                          # Same Python modules (8 files)
├── lib/                          # Same data fetching utilities
└── AGENT-INTEGRATION.md          # Integration documentation
```

**Purpose:**
- Used by ASO agents as their "toolkit"
- Agents reference Python modules from this location
- Project-specific integration

**Agent References:**
```bash
# aso-research agent
cd .claude/skills/aso && python3 keyword_analyzer.py < input.json

# aso-optimizer agent
cd .claude/skills/aso && python3 metadata_optimizer.py < input.json

# aso-strategist agent
cd .claude/skills/aso && python3 aso_scorer.py < input.json
```

**Characteristics:**
- ✅ Agents know where to find Python modules
- ✅ Clean separation from distributable skill
- ✅ Version control friendly
- ✅ Easy to synchronize with standalone version

---

### Layer 3: Agent Definitions

**Location:** `.claude/agents/aso/`

```
.claude/agents/aso/
├── aso-master.md                 # Orchestrator (opus, 500 lines)
├── aso-research.md               # Research + data fetching (opus, 700 lines)
├── aso-optimizer.md              # Metadata generation (sonnet, 600 lines)
└── aso-strategist.md             # Strategy + timelines (opus, 700 lines)
```

**Agent Workflow:**
```
User: /aso-full-audit MyApp
    ↓
aso-master.md
    ↓
┌───────────────────────────────────────────────┐
│ Phase 1: aso-research                         │
│ - Uses: .claude/skills/aso/keyword_analyzer   │
│ - Uses: .claude/skills/aso/competitor_analyzer│
│ - Fetches: iTunes API data                    │
│ - Output: keyword-list.md, competitor-gaps.md │
└───────────────────────────────────────────────┘
    ↓
┌───────────────────────────────────────────────┐
│ Phase 2: aso-optimizer                        │
│ - Uses: .claude/skills/aso/metadata_optimizer │
│ - Uses: .claude/skills/aso/ab_test_planner    │
│ - Output: apple-metadata.md, google-metadata  │
└───────────────────────────────────────────────┘
    ↓
┌───────────────────────────────────────────────┐
│ Phase 3: aso-strategist                       │
│ - Uses: .claude/skills/aso/aso_scorer         │
│ - Uses: .claude/skills/aso/launch_checklist   │
│ - Output: timeline.md, prelaunch-checklist.md │
└───────────────────────────────────────────────┘
    ↓
aso-master (synthesis)
    ↓
outputs/MyApp/00-MASTER-ACTION-PLAN.md
```

**Characteristics:**
- ✅ Coordinated workflow
- ✅ Sequential execution
- ✅ Quality validation gates
- ✅ Comprehensive deliverables

---

### Layer 4: Slash Commands

**Location:** `.claude/commands/aso/`

```
.claude/commands/aso/
├── aso-full-audit.md             # Complete audit workflow
├── aso-optimize.md               # Quick metadata optimization
├── aso-prelaunch.md              # Launch planning
└── aso-competitor.md             # Competitive intelligence
```

**Command Invocation:**
```bash
# User types
/aso-full-audit MyApp

# Command expands to
Invoke aso-master agent with full workflow parameters

# aso-master coordinates all 3 specialist agents
```

**Characteristics:**
- ✅ User-friendly shortcuts
- ✅ Parameterized workflows
- ✅ Clear documentation
- ✅ Consistent interface

---

### Layer 5: Output Structure

**Location:** `outputs/[app-name]/`

```
outputs/MyApp/
├── 00-MASTER-ACTION-PLAN.md      # Consolidated checklist
│
├── 01-research/
│   ├── keyword-list.md           # Keywords with implementation guide
│   ├── competitor-gaps.md        # Competitive opportunities
│   └── action-research.md        # Research tasks
│
├── 02-metadata/
│   ├── apple-metadata.md         # Copy-paste ready
│   ├── google-metadata.md        # Copy-paste ready
│   ├── visual-assets-spec.md     # Icon/screenshot specs
│   └── action-metadata.md        # Implementation tasks
│
├── 03-testing/
│   ├── ab-test-setup.md          # Step-by-step test setup
│   └── action-testing.md         # Testing tasks
│
├── 04-launch/
│   ├── prelaunch-checklist.md    # 47-item validation
│   ├── timeline.md               # Specific dates
│   ├── submission-guide.md       # Platform submission steps
│   └── action-launch.md          # Launch tasks
│
├── 05-optimization/
│   ├── review-responses.md       # Pre-written templates
│   ├── ongoing-tasks.md          # Daily/weekly/monthly schedule
│   └── action-optimization.md    # Ongoing tasks
│
└── FINAL-REPORT.md               # Executive summary
```

**Characteristics:**
- ✅ Actionable deliverables
- ✅ Copy-paste ready metadata
- ✅ Specific dates (not placeholders)
- ✅ Step-by-step guides
- ✅ User can execute immediately

---

## Data Flow

```
┌──────────────┐
│ User Request │
└──────┬───────┘
       │
       ↓
┌──────────────────────────┐
│ Slash Command            │
│ /aso-full-audit MyApp    │
└──────┬───────────────────┘
       │
       ↓
┌────────────────────────────────────────────────┐
│ aso-master (Orchestrator)                      │
│ - Gathers app details from user                │
│ - Plans workflow phases                        │
│ - Invokes specialist agents sequentially       │
└────────┬───────────────────────────────────────┘
         │
         ↓
┌────────────────────────────────────────────────┐
│ Phase 1: aso-research                          │
│                                                │
│ ┌──────────────────────────────────┐          │
│ │ iTunes Search API                │          │
│ │ - Fetch competitor data          │          │
│ │ - Get ratings, metadata          │          │
│ └───────────┬──────────────────────┘          │
│             │                                 │
│             ↓                                 │
│ ┌──────────────────────────────────┐          │
│ │ .claude/skills/aso/              │          │
│ │ - keyword_analyzer.py            │          │
│ │ - competitor_analyzer.py         │          │
│ └───────────┬──────────────────────┘          │
│             │                                 │
│             ↓                                 │
│ ┌──────────────────────────────────┐          │
│ │ Output: outputs/MyApp/01-research│          │
│ └──────────────────────────────────┘          │
└────────┬───────────────────────────────────────┘
         │
         ↓
┌────────────────────────────────────────────────┐
│ Phase 2: aso-optimizer                         │
│                                                │
│ ┌──────────────────────────────────┐           │
│ │ .claude/skills/aso/              │           │
│ │ - metadata_optimizer.py          │           │
│ │ - ab_test_planner.py             │           │
│ └───────────┬──────────────────────┘           │
│             │                                  │
│             ↓                                  │
│ ┌──────────────────────────────────┐           │
│ │ Output: outputs/MyApp/02-metadata│           │
│ │ - Apple metadata (validated)     │           │
│ │ - Google metadata (validated)    │           │
│ └──────────────────────────────────┘           │
└────────┬───────────────────────────────────────┘
         │
         ↓
┌────────────────────────────────────────────────┐
│ Phase 3: aso-strategist                        │
│                                                │
│ ┌──────────────────────────────────┐           │
│ │ .claude/skills/aso/              │           │
│ │ - aso_scorer.py                  │           │
│ │ - launch_checklist.py            │           │
│ └───────────┬──────────────────────┘           │
│             │                                  │
│             ↓                                  │
│ ┌──────────────────────────────────┐           │
│ │ Output: outputs/MyApp/04-launch  │           │
│ │ - Timeline with specific dates   │           │
│ │ - Pre-launch checklist (47 items)│           │
│ └──────────────────────────────────┘           │
└────────┬───────────────────────────────────────┘
         │
         ↓
┌────────────────────────────────────────────────┐
│ Phase 4: aso-master (Synthesis)                │
│ - Consolidates all outputs                     │
│ - Creates master action plan                   │
│ - Validates completeness                       │
│ - Quality self-assessment                      │
│                                                │
│ Output: outputs/MyApp/                         │
│         00-MASTER-ACTION-PLAN.md               │
└────────┬───────────────────────────────────────┘
         │
         ↓
┌────────────────────────┐
│ User Receives          │
│ Complete Action Plan   │
│ - Can execute          │
│   immediately          │
│ - Copy-paste ready     │
│ - Specific dates       │
│ - Step-by-step guides  │
└────────────────────────┘
```

---

## Key Integration Points

### 1. Agent → Skill Integration

**How agents reference Python modules:**

```markdown
# In agent definition (e.g., aso-research.md)

## Python Module Integration

### Running keyword_analyzer.py

**Prepare Input Data:**
```python
keywords_data = [...]
with open('/tmp/keyword_input.json', 'w') as f:
    json.dump(keywords_data, f)
```

**Execute Analyzer:**
```bash
cd .claude/skills/aso
python3 keyword_analyzer.py < /tmp/keyword_input.json > /tmp/keyword_output.json
```

**Parse Results:**
```python
with open('/tmp/keyword_output.json') as f:
    results = json.load(f)
# Use results to generate keyword-list.md
```
```

### 2. Command → Agent Integration

**How commands invoke agents:**

```markdown
# In slash command (e.g., aso-full-audit.md)

## What This Command Does

Invokes **aso-master** orchestrator to coordinate all 3 specialist agents:

1. **aso-research** - Fetches real competitor data, analyzes keywords
2. **aso-optimizer** - Generates copy-paste ready metadata
3. **aso-strategist** - Creates launch timeline and checklists
```

### 3. Skill → API Integration

**How skill fetches data:**

```python
# In .claude/skills/aso/lib/itunes_api.py

api = iTunesAPI()
competitors = api.compare_competitors([
    "Todoist",
    "Any.do",
    "Microsoft To Do"
])

# Returns: List of app metadata dictionaries
```

---

## Installation & Usage

### For Users: Install Agent System

```bash
# 1. Copy agents
cp .claude/agents/aso/*.md ~/.claude/agents/

# 2. Copy slash commands (optional)
cp .claude/commands/aso/*.md ~/.claude/commands/

# 3. Verify
ls ~/.claude/agents/aso-*

# 4. Use
# Open Claude Code
/aso-full-audit MyApp
```

**Note:** The `.claude/skills/aso/` folder stays in the project. Agents reference it when invoked.

### For Developers: Skill Distribution

```bash
# Distribute the standalone skill
cp -r app-store-optimization /path/to/distribution/

# Users install
cp -r app-store-optimization ~/.claude/skills/

# Direct skill usage (no agents)
"Hey Claude—I just added the app-store-optimization skill..."
```

---

## Synchronization

### When to Sync

Sync `app-store-optimization/` → `.claude/skills/aso/` when:
- Python modules updated
- New modules added
- Bug fixes applied
- Data fetching utilities changed

### How to Sync

```bash
# Simple copy (overwrites all files)
cp -r app-store-optimization/* .claude/skills/aso/

# Selective sync (specific files)
cp app-store-optimization/keyword_analyzer.py .claude/skills/aso/
cp app-store-optimization/lib/*.py .claude/skills/aso/lib/
```

### Automated Sync Script

```bash
#!/bin/bash
# sync-skill.sh

echo "Syncing standalone skill to agent-integrated version..."
rsync -av --delete app-store-optimization/ .claude/skills/aso/
echo "✓ Sync complete!"
```

---

## Summary

**Three Use Cases:**

1. **Standalone Skill Usage**
   - Copy `app-store-optimization/` to `~/.claude/skills/`
   - Direct Python module invocation
   - No agents required

2. **Agent-Coordinated Workflow**
   - Install agents to `~/.claude/agents/`
   - Agents use `.claude/skills/aso/` as toolkit
   - Full orchestration via `/aso-full-audit`

3. **Hybrid**
   - Both standalone skill AND agent system installed
   - User chooses: direct skill usage or agent-coordinated workflow
   - Maximum flexibility

**Key Architecture Principles:**

- ✅ **Separation of Concerns:** Skill vs Agents
- ✅ **Distributable:** Standalone skill can be shared
- ✅ **Integrated:** Agents have clean toolkit reference
- ✅ **Maintainable:** Single source of truth (app-store-optimization/)
- ✅ **Flexible:** Multiple usage modes

---

**See Also:**
- `.claude/skills/aso/AGENT-INTEGRATION.md` - Integration details
- `documentation/implementation/aso-agents-implementation-plan.md` - Implementation plan
- `CLAUDE.md` - Complete project reference
