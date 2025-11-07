# Agent Integration Note

**Location:** `.claude/skills/aso/`
**Purpose:** Agent-integrated version of the ASO skill

---

## Dual Structure Explanation

This project maintains **two copies** of the ASO skill:

### 1. Standalone Skill (Distributable)
**Location:** `app-store-optimization/`
**Purpose:**
- Standalone skill package
- Users can copy this folder to `~/.claude/skills/` or project `.claude/skills/`
- Independent of the agent system
- Can be distributed separately

### 2. Agent-Integrated Skill (Project-Specific)
**Location:** `.claude/skills/aso/` (THIS FOLDER)
**Purpose:**
- Used by ASO agents (aso-master, aso-research, aso-optimizer, aso-strategist)
- Agents reference Python modules from this location
- Integrated with agent workflow
- Project-specific implementation

---

## Why Two Copies?

**Separation of Concerns:**
- `app-store-optimization/` = Skill as a **tool** (reusable, distributable)
- `.claude/skills/aso/` = Skill as **agent resource** (project-integrated)

**Use Cases:**

**Use Case 1: Standalone Skill**
```bash
# User installs skill globally
cp -r app-store-optimization ~/.claude/skills/

# Claude Code loads skill
# User: "Hey Claude—I just added the app-store-optimization skill..."
# Claude uses Python modules directly
```

**Use Case 2: Agent-Coordinated Workflow**
```bash
# Agents installed
cp .claude/agents/aso/*.md ~/.claude/agents/

# User: /aso-full-audit MyApp
# aso-master → aso-research → uses .claude/skills/aso/keyword_analyzer.py
# Complete workflow with coordination
```

---

## Agent References

All ASO agents reference this location:

**aso-research.md:**
```bash
cd .claude/skills/aso
python3 keyword_analyzer.py < input.json
python3 competitor_analyzer.py < input.json
```

**aso-optimizer.md:**
```bash
cd .claude/skills/aso
python3 metadata_optimizer.py < input.json
python3 ab_test_planner.py < input.json
```

**aso-strategist.md:**
```bash
cd .claude/skills/aso
python3 aso_scorer.py < input.json
python3 launch_checklist.py < input.json
```

---

## Keeping Synchronized

If you update Python modules:

**Option A: Update Both**
```bash
# Make changes in app-store-optimization/
# Then copy to agent version
cp -r app-store-optimization/* .claude/skills/aso/
```

**Option B: Symlink (Advanced)**
```bash
# Remove agent copy
rm -rf .claude/skills/aso

# Create symlink
ln -s ../../app-store-optimization .claude/skills/aso

# Now agents use the original directly
```

**Recommended:** Keep separate for stability. Update both when changes are needed.

---

## File Structure

```
aeo-skill/
├── app-store-optimization/        # STANDALONE SKILL (distributable)
│   ├── SKILL.md
│   ├── *.py                       # 8 Python modules
│   └── lib/                       # Data fetching utilities
│
└── .claude/
    ├── skills/aso/                # AGENT-INTEGRATED (project-specific)
    │   ├── SKILL.md               # Same as above
    │   ├── *.py                   # Same Python modules
    │   ├── lib/                   # Same utilities
    │   └── AGENT-INTEGRATION.md   # This file
    │
    ├── agents/aso/                # Agents that USE the skill
    │   ├── aso-master.md          # References ../skills/aso/
    │   ├── aso-research.md
    │   ├── aso-optimizer.md
    │   └── aso-strategist.md
    │
    └── commands/aso/              # Slash commands invoke agents
        ├── aso-full-audit.md
        ├── aso-optimize.md
        ├── aso-prelaunch.md
        └── aso-competitor.md
```

---

## For Developers

When adding new Python modules:

1. **Add to `app-store-optimization/`** (primary)
2. **Copy to `.claude/skills/aso/`** (agent version)
3. **Update agent definitions** if new modules are used
4. **Update SKILL.md** in both locations
5. **Test both workflows:**
   - Standalone: Direct Python module usage
   - Agent-coordinated: `/aso-full-audit` command

---

## Summary

- **Two copies** of the ASO skill exist
- **app-store-optimization/** = Standalone, distributable
- **.claude/skills/aso/** = Agent-integrated, project-specific
- **Agents always use** `.claude/skills/aso/`
- **Keep synchronized** when making updates

This architecture ensures the skill can work **both ways**: as a standalone tool and as part of the coordinated agent system.
