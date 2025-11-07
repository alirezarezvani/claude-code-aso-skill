# ASO Agent System Installation Guide

**Version:** 1.0
**Date:** November 7, 2025

---

## Prerequisites

Before installing the ASO agent system, ensure you have:

- ✅ **Claude Code CLI** installed and configured
- ✅ **Python 3.8+** installed (for skill Python modules)
- ✅ **Git** installed (optional, for version control)
- ✅ **Apple Developer Account** (for App Store Connect access)
- ✅ **Google Play Developer Account** (for Play Console access)

---

## Installation Options

### Option 1: Agent System Only (Recommended)

Install agents for coordinated ASO workflows with full orchestration.

**Who should use this:**
- Teams conducting comprehensive ASO
- Product managers needing structured deliverables
- Developers launching new apps

**What you get:**
- 4 specialized agents (master, research, optimizer, strategist)
- Slash commands for quick workflows
- Structured output templates
- Data fetching via iTunes API and WebFetch

### Option 2: Standalone Skill Only

Install skill for direct Python module usage without agents.

**Who should use this:**
- Developers wanting programmatic access
- Quick keyword analysis
- Integration into existing tools

**What you get:**
- 8 Python modules (keyword analysis, competitor analysis, etc.)
- Direct command-line usage
- No agent coordination
- Manual workflow

### Option 3: Both (Maximum Flexibility)

Install both agent system and standalone skill.

**Who should use this:**
- Advanced users
- Development teams
- Users experimenting with both approaches

**What you get:**
- Everything from Option 1 and Option 2
- Choice of workflow style
- Maximum flexibility

---

## Option 1: Install Agent System (Recommended)

### Step 1: Copy Agents

```bash
# Navigate to this project
cd /path/to/aeo-skill

# Copy agents to your user-level agents folder
cp .claude/agents/aso/*.md ~/.claude/agents/

# Verify installation
ls ~/.claude/agents/aso-*

# Expected output:
# aso-master.md
# aso-optimizer.md
# aso-research.md
# aso-strategist.md
```

### Step 2: Copy Slash Commands (Optional but Recommended)

```bash
# Copy slash commands
cp .claude/commands/aso/*.md ~/.claude/commands/

# Verify installation
ls ~/.claude/commands/aso-*

# Expected output:
# aso-competitor.md
# aso-full-audit.md
# aso-optimize.md
# aso-prelaunch.md
```

### Step 3: Verify Agent Access

Open Claude Code and check that agents are available:

```bash
# In Claude Code, type:
/help

# You should see:
# Available commands:
# - /aso-full-audit [app-name]
# - /aso-optimize [app-name]
# - /aso-prelaunch [app-name]
# - /aso-competitor [app-name] [competitors]
```

### Step 4: Test Installation

```bash
# Test with a simple query
/aso-full-audit TestApp

# Expected: aso-master agent will start and prompt for app details
```

**Installation Complete!** ✅

The agent system will use the skill modules from `.claude/skills/aso/` in this project when invoked.

---

## Option 2: Install Standalone Skill

### Step 1: Copy Skill to Global Skills Folder

```bash
# Navigate to this project
cd /path/to/aeo-skill

# Copy skill to your global skills folder
cp -r app-store-optimization ~/.claude/skills/

# Verify installation
ls ~/.claude/skills/app-store-optimization

# Expected output: SKILL.md and 8 Python modules
```

### Step 2: Test Skill

```bash
# In Claude Code, invoke skill directly
# "Hey Claude—I just added the app-store-optimization skill.
#  Can you analyze keywords for my productivity app?"

# Claude will use Python modules directly
```

**Installation Complete!** ✅

---

## Option 3: Install Both

### Step 1: Install Agent System

Follow "Option 1" steps above.

### Step 2: Install Standalone Skill

Follow "Option 2" steps above.

**Installation Complete!** ✅

You can now choose between:
- Agent-coordinated workflows (`/aso-full-audit`)
- Direct skill usage (manual invocation)

---

## Verification Checklist

After installation, verify everything is working:

- [ ] **Agents Installed**
  ```bash
  ls ~/.claude/agents/aso-* | wc -l
  # Should output: 4
  ```

- [ ] **Slash Commands Installed** (if Option 1 or 3)
  ```bash
  ls ~/.claude/commands/aso-* | wc -l
  # Should output: 4
  ```

- [ ] **Skill Installed** (if Option 2 or 3)
  ```bash
  ls ~/.claude/skills/app-store-optimization | wc -l
  # Should output: 11+ files
  ```

- [ ] **Python Modules Accessible**
  ```bash
  cd ~/.claude/skills/app-store-optimization
  python3 keyword_analyzer.py --help
  # Should output: Usage instructions
  ```

- [ ] **Test Basic Workflow**
  - Open Claude Code
  - Run `/aso-full-audit TestApp`
  - Should see aso-master agent start

---

## Project-Specific Setup

The agent system uses `.claude/skills/aso/` in this project as its toolkit. This folder should remain in the project.

**Why?**
- Agents reference `.claude/skills/aso/` when invoked
- Keeps project self-contained
- Allows version control of skill modules

**Do NOT delete `.claude/skills/aso/` folder** if using agents.

---

## Configuration (Optional)

### iTunes Search API

No configuration needed—iTunes Search API is free and requires no authentication.

### WebFetch Tool

No configuration needed—WebFetch is a built-in Claude Code tool.

### Paid ASO Tools (Future)

If you have API keys for paid ASO tools (AppTweak, Sensor Tower, etc.), you can configure them:

```bash
# Set environment variables
export APPTWEAK_API_KEY="your-key-here"
export SENSOR_TOWER_API_KEY="your-key-here"

# Agents will detect and use these automatically
```

**Currently:** Agents work without paid APIs using iTunes Search API only.

---

## Updating the System

### Update Agents

```bash
# Navigate to project
cd /path/to/aeo-skill

# Copy updated agents
cp .claude/agents/aso/*.md ~/.claude/agents/

# Restart Claude Code
```

### Update Skill

```bash
# If using standalone skill (Option 2 or 3)
cp -r app-store-optimization ~/.claude/skills/

# If using agent system, update project skill folder
# (agents reference .claude/skills/aso/ in project, not global)
```

### Keep Project Skill Synchronized

If you update `app-store-optimization/` modules, sync to agent-integrated version:

```bash
# From project root
cp -r app-store-optimization/* .claude/skills/aso/

# This ensures agents use latest skill modules
```

---

## Troubleshooting

### Issue: Agents not showing up in Claude Code

**Solution:**
```bash
# Verify agents are in correct location
ls ~/.claude/agents/aso-*

# If empty, re-copy:
cp .claude/agents/aso/*.md ~/.claude/agents/

# Restart Claude Code
```

### Issue: Slash commands not working

**Solution:**
```bash
# Verify commands are installed
ls ~/.claude/commands/aso-*

# If empty, copy:
cp .claude/commands/aso/*.md ~/.claude/commands/

# Restart Claude Code
```

### Issue: Python modules not found

**Solution:**
```bash
# Verify .claude/skills/aso/ exists in project
ls .claude/skills/aso/*.py

# If missing, re-copy from standalone skill:
mkdir -p .claude/skills && cp -r app-store-optimization .claude/skills/aso

# Agents reference this location
```

### Issue: iTunes API not working

**Potential causes:**
- Network connectivity
- API rate limiting (rare)

**Solution:**
```bash
# Test iTunes API directly
curl "https://itunes.apple.com/search?term=todoist&entity=software&limit=1"

# Should return JSON with app data
# If fails, check internet connection
```

### Issue: Permission errors

**Solution:**
```bash
# Ensure proper permissions
chmod -R 755 ~/.claude/agents/aso-*
chmod -R 755 ~/.claude/skills/app-store-optimization
```

---

## Uninstallation

### Remove Agents

```bash
rm ~/.claude/agents/aso-*.md
```

### Remove Slash Commands

```bash
rm ~/.claude/commands/aso-*.md
```

### Remove Standalone Skill

```bash
rm -rf ~/.claude/skills/app-store-optimization
```

### Clean Project Files (if no longer needed)

```bash
# Navigate to project
cd /path/to/aeo-skill

# Remove agent-integrated skill
rm -rf .claude/skills/aso

# Keep app-store-optimization/ for distribution
```

---

## Next Steps

After installation:

1. **Read Usage Guide:** See `.claude/USAGE.md` for workflows and examples
2. **Review Architecture:** See `.claude/ARCHITECTURE.md` for system design
3. **Read Implementation Plan:** See `documentation/implementation/aso-agents-implementation-plan.md`
4. **Run First Audit:** Try `/aso-full-audit YourAppName`

---

## System Requirements

**Minimum:**
- Claude Code CLI (latest version)
- Python 3.8+
- 1GB free disk space
- Internet connection (for API access)

**Recommended:**
- Python 3.10+
- 2GB free disk space
- Fast internet connection
- Apple Developer Account
- Google Play Developer Account

---

## Getting Help

**Documentation:**
- Usage Guide: `.claude/USAGE.md`
- Architecture: `.claude/ARCHITECTURE.md`
- Implementation Plan: `documentation/implementation/aso-agents-implementation-plan.md`
- Data Sources: `app-store-optimization/lib/data_sources.md`

**Issues:**
- Check troubleshooting section above
- Review agent definitions in `.claude/agents/aso/`
- Consult implementation plan for workflows

---

**Installation Guide Version:** 1.0
**Last Updated:** November 7, 2025
**Maintained By:** ASO Agent System Team
