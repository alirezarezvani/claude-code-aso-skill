# 🚀 ASO Agent System for Claude Code

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Claude Code](https://img.shields.io/badge/Claude_Code-Compatible-purple.svg)
![Claude App](https://img.shields.io/badge/Claude_App-Compatible-orange.svg)
![Status](https://img.shields.io/badge/status-production_ready-success.svg)

**Professional App Store Optimization (ASO) powered by AI agents**

[Features](#-features) • [Installation](#-installation) • [Quick Start](#-quick-start) • [Documentation](#-documentation) • [Examples](#-example-outputs)

</div>

---

## 📋 Overview

The **ASO Agent System** is a comprehensive, production-ready multi-agent framework for App Store Optimization (ASO) built for **Claude Code** and **Claude Desktop/Web App**. It combines specialized AI agents with real-time data fetching to generate **actionable, copy-paste ready deliverables** for iOS and Android app optimization.

**Two ways to use:**
- 🖥️ **Claude Code CLI** - Full multi-agent system with automated workflows (developers)
- 🌐 **Claude Desktop/Web App** - Standalone skill for conversational ASO analysis (everyone)

### 🎯 What Makes This Different

Unlike generic ASO tools that provide analysis reports, this system delivers:

✅ **Copy-Paste Ready Metadata** - Character-validated content ready for App Store Connect and Google Play Console
✅ **Real Data Integration** - iTunes Search API + WebFetch for competitor intelligence
✅ **Actionable Task Checklists** - 47-item pre-launch validation with success criteria
✅ **Specific Timelines** - Real calendar dates, not "Week 1" placeholders
✅ **Complete Workflow** - 5-phase execution from research to ongoing optimization

---

## ✨ Features

### 🤖 Multi-Agent System

**4 Specialized Agents** working in coordinated workflow:

- **aso-master** - Orchestrator coordinating all specialist agents (Opus model)
- **aso-research** - Keyword research + competitor analysis with iTunes API (Opus model)
- **aso-optimizer** - Metadata generation with character validation (Sonnet model)
- **aso-strategist** - Launch timelines + ongoing optimization (Opus model)

### 📊 Real Data Integration

- **iTunes Search API** - Free, official Apple API for competitor data (tested & working)
- **WebFetch Utilities** - Additional scraping for comprehensive analysis
- **Character Validation** - Apple (30/30/100) and Google (50/80/4000) limits enforced
- **Natural Language Checking** - No keyword stuffing, reads professionally

### 📁 Comprehensive Deliverables

```
outputs/[YourApp]/
├── 00-MASTER-ACTION-PLAN.md      # Complete roadmap with ASO score
├── 01-research/
│   ├── keyword-list.md           # 20 priority keywords, tiered strategy
│   ├── competitor-gaps.md        # Competitive opportunities
│   └── action-research.md        # Research tasks checklist
├── 02-metadata/
│   ├── apple-metadata.md         # Copy-paste ready (App Store Connect)
│   ├── google-metadata.md        # Copy-paste ready (Play Console)
│   ├── visual-assets-spec.md     # Designer briefing
│   └── action-metadata.md        # Implementation tasks
├── 03-testing/
│   ├── ab-test-setup.md          # A/B test configuration
│   └── action-testing.md         # Testing tasks
├── 04-launch/
│   ├── prelaunch-checklist.md    # 47-item validation
│   ├── timeline.md               # Specific calendar dates
│   ├── submission-guide.md       # Platform procedures
│   └── action-launch.md          # Launch tasks
├── 05-optimization/
│   ├── review-responses.md       # Pre-written templates
│   ├── ongoing-tasks.md          # Daily/weekly/monthly schedule
│   └── action-optimization.md    # Optimization tasks
└── FINAL-REPORT.md               # Executive summary
```

### ⚡ Slash Commands

Four user-facing workflows:

| Command | Duration | Output |
|---------|----------|--------|
| `/aso-full-audit [AppName]` | 30-40 min | Complete audit with all phases |
| `/aso-optimize [AppName]` | 10-15 min | Metadata optimization only |
| `/aso-prelaunch [AppName]` | 15-20 min | Pre-launch validation checklist |
| `/aso-competitor [AppName] "App1,App2"` | 10-15 min | Competitive intelligence |

---

## 🚀 Quick Start

### Prerequisites

**Choose Your Platform:**
- **[Claude Code](https://claude.com/claude-code)** (CLI) - Full multi-agent system with automation
- **[Claude Desktop/Web App](https://claude.ai)** - Standalone skill for direct conversations
- macOS, Linux, or Windows
- Internet connection (for iTunes API)

### Installation (< 5 minutes)

#### Option 1: Claude Code (Full Multi-Agent System) - Recommended

For developers using Claude Code CLI who want the complete multi-agent workflow:

```bash
# Clone repository
git clone https://github.com/alirezarezvani/claude-code-aso-skill.git
cd claude-code-aso-skill

# Install agents (user-level)
cp .claude/agents/aso/*.md ~/.claude/agents/

# Install slash commands (optional)
cp .claude/commands/aso/*.md ~/.claude/commands/

# Verify installation
claude --list-agents | grep aso
```

---

#### Option 2: Claude Desktop/Web App (Standalone Skill) - Easy Upload

For users of Claude Desktop or Web App who want quick ASO analysis:

**Step 1: Download the Skill Package**
```bash
# Download app-store-optimization.zip from the repository
# Or use wget/curl:
wget https://github.com/alirezarezvani/claude-code-aso-skill/raw/main/app-store-optimization.zip
```

**Step 2: Upload to Claude**

**For Claude Desktop App:**
1. Open Claude Desktop
2. Go to **Settings** (⚙️ icon)
3. Navigate to **Capabilities** tab
4. Click **Upload Custom Skill**
5. Select `app-store-optimization.zip`
6. Wait for "Skill installed successfully" message
7. Ready to use!

**For Claude Web App:**
1. Go to [claude.ai](https://claude.ai)
2. Click your profile icon → **Settings**
3. Navigate to **Capabilities** section
4. Click **Upload Custom Skill**
5. Select `app-store-optimization.zip`
6. Confirm upload
7. Ready to use!

**Step 3: Start Using**
```
Hey Claude, I just added the app-store-optimization skill.
Analyze my app: FitFlow - fitness tracking app for beginners.
Generate a complete ASO strategy with keyword research and metadata.
```

---

#### Option 3: Manual Installation (Advanced)

For advanced users who want to customize the skill:

```bash
# Extract and install skill manually
unzip app-store-optimization.zip
cp -r app-store-optimization ~/.claude/skills/

# For Claude Code CLI
# Restart Claude Code
claude --reload

# For Claude Desktop
# Restart Claude Desktop app
```

### First Run

**For Claude Code Users:**
```bash
# Start Claude Code in your project directory
claude

# Run complete ASO audit
/aso-full-audit MyAwesomeApp

# Review outputs
cd outputs/MyAwesomeApp
cat 00-MASTER-ACTION-PLAN.md
```

**For Claude Desktop/Web App Users:**
```
Start a new conversation and say:

"Hey Claude, I just added the app-store-optimization skill.
I need help with App Store Optimization for my app called 'MyAwesomeApp'.
It's a fitness tracking app for beginners.

Please generate:
1. Keyword research with 20 priority keywords
2. Copy-paste ready metadata for Apple App Store
3. Copy-paste ready metadata for Google Play Store
4. A complete action plan with timeline"
```

**That's it!** You'll receive a complete ASO strategy with copy-paste ready metadata, keyword research, and actionable recommendations.

---

## 📖 Usage

### Typical Workflows

#### 1️⃣ New App Launch (Complete Workflow)
```bash
/aso-full-audit MyApp
```
**Generates:**
- ASO health score (0-100)
- 20 priority keywords with implementation guide
- Copy-paste ready metadata (Apple + Google)
- 47-item pre-launch checklist
- Timeline with specific dates
- Ongoing optimization schedule

**Time:** 30-40 minutes
**Output:** Complete `outputs/MyApp/` folder

---

#### 2️⃣ Existing App Optimization
```bash
/aso-optimize MyApp
```
**Generates:**
- Updated metadata optimized for current keywords
- A/B test variants
- Visual asset specifications

**Time:** 10-15 minutes
**Output:** `outputs/MyApp/02-metadata/` folder

---

#### 3️⃣ Pre-Launch Validation
```bash
/aso-prelaunch MyApp
```
**Generates:**
- 47-item validation checklist
- Submission procedures
- Launch timeline
- Common rejection fixes

**Time:** 15-20 minutes
**Output:** `outputs/MyApp/04-launch/` folder

---

#### 4️⃣ Competitive Intelligence
```bash
/aso-competitor MyApp "Todoist,Any.do,Microsoft To Do"
```
**Generates:**
- Competitor keyword analysis
- Feature gap identification
- Pricing strategy comparison
- Opportunity areas

**Time:** 10-15 minutes
**Output:** `outputs/MyApp/01-research/competitor-gaps.md`

---

### Quality Standards

All outputs meet these standards:

✅ **Character Limits Validated**
- Apple title ≤ 30 chars
- Apple subtitle ≤ 30 chars
- Apple keywords ≤ 100 chars (no duplicates)
- Google title ≤ 50 chars
- Google short description ≤ 80 chars

✅ **Real Dates, Not Placeholders**
- "November 7-13, 2025" ✅
- "Week 1" ❌

✅ **Copy-Paste Ready**
- No additional formatting needed
- Pre-validated character counts
- Platform constraints respected

✅ **Actionable Tasks**
- Checkbox format with success criteria
- Validation methods included
- Implementation guidance provided

---

## 🎯 Example Outputs

See the complete example workflow for a fictional fitness app:

**[FitFlow Example](outputs/FitFlow-example/)**

### Master Action Plan
```markdown
# Master Action Plan: FitFlow

**ASO Health Score:** 58/100
**Priority Level:** High (New App Launch)

## Timeline
November 7-10, 2025: Research Phase
November 11-17, 2025: Metadata & Visual Assets
November 18-20, 2025: A/B Test Setup
November 21-25, 2025: Launch Preparation
December 1, 2025: PUBLIC LAUNCH 🚀
```

### Keyword Research
```markdown
| Keyword | Search Volume | Difficulty | Implementation |
|---------|--------------|------------|----------------|
| fitness tracker | 85,000/mo | 55/100 | Apple Title |
| workout planner | 62,000/mo | 48/100 | Apple Subtitle |
| exercise log | 45,000/mo | 42/100 | Description |
```

### Copy-Paste Ready Metadata
```markdown
### Title (30 chars max)
FitFlow: Fitness Tracker
Character Count: 25/30 ✅

### Subtitle (30 chars max)
Easy Workout Planner & Log
Character Count: 26/30 ✅

### Keywords (100 chars max)
activity,goals,routine,challenge,calories,home,progress,simple,exercise,fitness,beginner
Character Count: 91/100 ✅
```

---

## 🏗️ Architecture

### System Design

```
┌─────────────────────────────────────────────────────────────────┐
│                    ASO Agent System                              │
│                                                                   │
│  Standalone Skill ←─────→ Agent System ←─────→ User Outputs    │
└─────────────────────────────────────────────────────────────────┘

Layer 1: Standalone Skill (app-store-optimization/)
         ↓
Layer 2: Agent-Integrated Skill (.claude/skills/aso/)
         ↓
Layer 3: Agent Definitions (.claude/agents/aso/)
         ↓
Layer 4: Slash Commands (.claude/commands/aso/)
         ↓
Layer 5: Output Structure (outputs/[app-name]/)
```

### Dual Structure

**Standalone Skill** (`app-store-optimization/`)
- Distributable Python skill package
- 8 modules for direct invocation
- Works independently of agents
- Available as ZIP file (`app-store-optimization.zip`)

**ZIP Package for Claude Desktop/Web App** (`app-store-optimization.zip`)
- **One-click installation** for Claude Desktop and Web App users
- Upload via Settings → Capabilities
- No command-line required
- Instant access to ASO analysis

**Agent-Integrated** (`.claude/skills/aso/`)
- Used by ASO agents as toolkit
- Synchronized with standalone version
- Enables coordinated workflows
- Full multi-agent automation

**Choose Your Version:**
- **Claude Code CLI** → Clone repository + install agents (Option 1)
- **Claude Desktop/Web App** → Download ZIP + upload to Settings (Option 2)
- **Advanced Users** → Manual installation from source (Option 3)

See [ARCHITECTURE.md](.claude/ARCHITECTURE.md) for complete details.

---

## 📚 Documentation

| Document | Description |
|----------|-------------|
| [ARCHITECTURE.md](.claude/ARCHITECTURE.md) | Complete system architecture (509 lines) |
| [INSTALL.md](.claude/INSTALL.md) | Installation guide for 3 scenarios |
| [USAGE.md](.claude/USAGE.md) | Usage guide with 5 workflows |
| [CLAUDE.md](CLAUDE.md) | Quick reference for Claude instances |
| [Implementation Plan](documentation/implementation/aso-agents-implementation-plan.md) | Complete development plan (400+ lines) |
| [Data Sources](app-store-optimization/lib/data_sources.md) | API documentation and limitations |

---

## 🧪 Testing

### iTunes API Integration ✅

```bash
cd .claude/skills/aso && python3 lib/itunes_api.py

Test Results:
✅ Search for apps: PASSED (Todoist found)
✅ Get app by name: PASSED (Metadata extracted)
✅ Get competitors: PASSED (Top productivity apps fetched)
✅ Compare competitors: PASSED (3 apps compared successfully)

Sample Output:
- Todoist: 4.8★ (120,655 ratings)
- Any.do: 4.6★ (49,604 ratings)
- Microsoft To Do: 4.7★ (250,014 ratings)
```

### Example Workflow ✅

```bash
Created: outputs/FitFlow-example/

Quality Validation:
✅ Character counts validated
✅ Real dates used (November 7 - December 1, 2025)
✅ Actionable tasks with success criteria
✅ Natural language (no keyword stuffing)
✅ Copy-paste ready content
```

---

## 🛠️ Tech Stack

- **Language:** Python 3.8+
- **AI Framework:** Claude Code agents (Opus + Sonnet models)
- **Data Sources:** iTunes Search API, WebFetch
- **Output Format:** Markdown with YAML frontmatter
- **Platform Support:** macOS, Linux, Windows

---

## 📊 Project Statistics

- **Total Files:** 59
- **Lines of Code:** 26,526+
- **Agents:** 4 (2,500+ lines)
- **Python Modules:** 8 (800+ lines)
- **Templates:** 6 action checklists
- **Slash Commands:** 4 workflows
- **Documentation:** 1,500+ lines
- **Development Time:** Production-ready v1.0

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

### Areas for Contribution

1. **Additional Data Sources**
   - Integration with paid ASO APIs (AppTweak, Sensor Tower)
   - iTunes Review API for bulk review fetching
   - Historical ranking data

2. **Localization**
   - Multi-language metadata generation
   - Translation workflow automation
   - Regional keyword research

3. **Enhanced Analytics**
   - Keyword ranking trend tracking
   - ASO score progression over time
   - Competitor movement monitoring

4. **Documentation**
   - Additional use cases and examples
   - Video tutorials
   - Translation of documentation

### Contribution Process

```bash
# Fork repository
git clone https://github.com/alirezarezvani/claude-code-aso-skill.git
cd claude-code-aso-skill

# Create feature branch
git checkout -b feature/your-feature-name

# Make changes and test
# ... your changes ...

# Commit with clear message
git commit -m "feat: add AppTweak API integration"

# Push and create PR
git push origin feature/your-feature-name
```

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE.md](LICENSE.md) file for details.

```
MIT License - Copyright (c) 2025 Alireza Rezvani

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software.
```

---

## 🙏 Acknowledgments

- **Claude Code Team** - For the amazing AI-powered development environment
- **Apple** - For the free iTunes Search API
- **ASO Community** - For best practices and industry benchmarks

---

## 📞 Support

### Getting Help

- **Documentation:** Start with [INSTALL.md](.claude/INSTALL.md) and [USAGE.md](.claude/USAGE.md)
- **Examples:** Review [FitFlow example](outputs/FitFlow-example/)
- **Issues:** Open an issue on [GitHub Issues](https://github.com/alirezarezvani/claude-code-aso-skill/issues)

### Common Questions

**Q: Do I need paid ASO tools?**
A: No. This system uses free iTunes Search API and industry benchmarks.

**Q: Can I use this for both iOS and Android?**
A: Yes. Generates metadata for both Apple App Store and Google Play Store.

**Q: How accurate are the keyword search volumes?**
A: Estimates based on industry benchmarks (±20% accuracy). Use Apple Search Ads data for exact volumes.

**Q: Can I customize the agents?**
A: Yes. All agents are Markdown files in `.claude/agents/aso/` - edit freely.

---

## 🚦 Status

- **Current Version:** 1.0.0 (Production Ready)
- **Release Date:** November 7, 2025
- **Status:** ✅ Stable and tested
- **Maintenance:** Actively maintained

---

## 🗺️ Roadmap

### Version 1.0 (Current) ✅
- [x] Multi-agent system with orchestration
- [x] iTunes API integration
- [x] Copy-paste ready metadata
- [x] Complete documentation
- [x] Example workflow

### Version 1.1 (Planned)
- [ ] iTunes Review API integration
- [ ] Historical tracking database
- [ ] Enhanced A/B test analytics
- [ ] Multi-language support (Spanish, German, French)

### Version 2.0 (Future)
- [ ] Paid API integration (AppTweak, Sensor Tower)
- [ ] Web dashboard for tracking
- [ ] Automated reporting
- [ ] Team collaboration features

---

## ⭐ Star History

If you find this project useful, please consider giving it a star on GitHub!

---

<div align="center">

**Built with ❤️ using Claude Code**

[⬆ Back to Top](#-aso-agent-system-for-claude-code)

</div>
