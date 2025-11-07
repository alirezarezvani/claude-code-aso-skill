# ASO Agent System Usage Guide

**Version:** 1.0
**Date:** November 7, 2025

---

## Quick Start

### Your First ASO Audit

```bash
# Open Claude Code
# Type the following slash command:
/aso-full-audit MyApp

# The system will:
# 1. Prompt you for app details (name, category, competitors)
# 2. Invoke aso-master orchestrator
# 3. Coordinate 3 specialist agents (research, optimizer, strategist)
# 4. Generate complete ASO plan in outputs/MyApp/

# Estimated time: 30-40 minutes
```

**What you'll get:**
- Keyword strategy with priority rankings
- Copy-paste ready metadata (Apple & Google)
- Competitor analysis and gaps
- A/B test setup guide
- Pre-launch checklist (47 items)
- Launch timeline with specific dates
- Ongoing optimization schedule

---

## Available Slash Commands

### `/aso-full-audit [app-name]`

**Purpose:** Complete ASO audit and strategy creation

**When to use:**
- Launching new app
- Major ASO overhaul
- First-time ASO optimization
- Quarterly comprehensive review

**Example:**
```bash
/aso-full-audit FitFlow
```

**Process:**
1. aso-master gathers app details from you
2. aso-research fetches competitor data via iTunes API
3. aso-optimizer generates metadata for both platforms
4. aso-strategist creates timeline and checklists
5. aso-master synthesizes everything into master action plan

**Output Location:** `outputs/FitFlow/`

**Time:** 30-40 minutes

---

### `/aso-optimize [app-name]`

**Purpose:** Quick metadata optimization (skip research phase)

**When to use:**
- You already have competitor research
- Need metadata refresh only
- A/B test variant generation
- Updating for new app version

**Example:**
```bash
/aso-optimize FitFlow
```

**Process:**
1. aso-master prompts for keywords and messaging priorities
2. aso-optimizer generates optimized metadata
3. Outputs metadata files only (skips research and launch planning)

**Output Location:** `outputs/FitFlow/02-metadata/`

**Time:** 10-15 minutes

---

### `/aso-prelaunch [app-name]`

**Purpose:** Pre-launch validation and submission guide

**When to use:**
- Preparing to submit app for review
- Need submission checklist
- Want launch timeline
- Validating metadata before submission

**Example:**
```bash
/aso-prelaunch FitFlow
```

**Process:**
1. aso-strategist validates all metadata
2. Generates 47-item pre-launch checklist
3. Creates timeline with specific submission dates
4. Provides submission guide for both platforms

**Output Location:** `outputs/FitFlow/04-launch/`

**Time:** 15-20 minutes

---

### `/aso-competitor [app-name] [competitors]`

**Purpose:** Competitive intelligence and gap analysis

**When to use:**
- Researching new competitors
- Quarterly competitive check
- Identifying market opportunities
- Strategic positioning

**Example:**
```bash
/aso-competitor FitFlow "Strava,Nike Run Club,MapMyRun"
```

**Process:**
1. aso-research fetches competitor data via iTunes API
2. Analyzes metadata, keywords, ratings, reviews
3. Identifies competitive gaps and opportunities
4. Generates actionable insights

**Output Location:** `outputs/FitFlow/01-research/competitor-gaps.md`

**Time:** 10-15 minutes

---

## Typical Workflows

### Workflow 1: New App Launch (Complete)

**Goal:** Launch app with optimized ASO from day one

**Steps:**
```bash
# 1. Run full audit
/aso-full-audit MyNewApp

# Agent will prompt:
# - App name?
# - Category?
# - Target audience?
# - Top 3 competitors?
# - Key features?

# 2. Review outputs
cd outputs/MyNewApp
ls

# You'll see:
# - 00-MASTER-ACTION-PLAN.md  ← START HERE
# - 01-research/
# - 02-metadata/
# - 03-testing/
# - 04-launch/
# - 05-optimization/
# - FINAL-REPORT.md

# 3. Execute action plans
# Follow 00-MASTER-ACTION-PLAN.md step by step

# 4. Copy metadata
# Copy apple-metadata.md → App Store Connect
# Copy google-metadata.md → Play Console

# 5. Validate pre-launch
# Check all 47 items in prelaunch-checklist.md

# 6. Submit for review
# Follow submission-guide.md

# 7. Launch!
# Follow timeline.md for launch day tasks
```

**Timeline:**
- Day 1: Run audit, review outputs (2 hours)
- Days 2-3: Implement metadata (4 hours)
- Days 4-5: Visual assets creation (designer, 8 hours)
- Day 6: Pre-launch validation (2 hours)
- Day 7: Submit for review
- Days 8-10: App review (Apple 24-48h, Google 2-7 days)
- Day 11+: Launch and monitor

**Total:** ~2 weeks from audit to launch

---

### Workflow 2: Existing App Optimization

**Goal:** Improve ASO for app already in store

**Steps:**
```bash
# 1. Run full audit to establish baseline
/aso-full-audit ExistingApp

# 2. Review current ASO health score
cat outputs/ExistingApp/FINAL-REPORT.md
# Look for ASO Health Score: XX/100

# 3. Identify quick wins
cat outputs/ExistingApp/00-MASTER-ACTION-PLAN.md
# Section: "Quick Wins (Complete First)"

# 4. Implement high-priority improvements
# Start with metadata optimization
# Then visual assets
# Then A/B testing

# 5. Monitor results weekly
# Use ongoing-tasks.md schedule

# 6. Re-audit after 3 months
/aso-full-audit ExistingApp
# Compare scores to see improvement
```

**Expected Results:**
- Month 1: 10-20% increase in impressions
- Month 3: 15-25% increase in conversion rate
- Month 6: 50%+ increase in organic installs

---

### Workflow 3: Competitive Intelligence

**Goal:** Monitor competitors and identify opportunities

**Steps:**
```bash
# 1. Identify top 5 competitors
# Research your category manually or use discovery tools

# 2. Run competitor analysis
/aso-competitor MyApp "Competitor1,Competitor2,Competitor3"

# 3. Review competitor gaps
cat outputs/MyApp/01-research/competitor-gaps.md

# Look for:
# - Keywords they're not targeting (opportunities)
# - Messaging weaknesses (your advantages)
# - Feature gaps (differentiation)

# 4. Update your strategy
# Incorporate insights into next metadata iteration

# 5. Schedule regular competitive checks
# Add to calendar: Monthly competitor analysis
```

**Use Cases:**
- Quarterly strategic planning
- Before major feature launch
- When entering new market
- After competitor launches

---

### Workflow 4: A/B Testing

**Goal:** Optimize conversion rate through data-driven testing

**Steps:**
```bash
# 1. Generate test variants
/aso-optimize MyApp

# When prompted, specify:
# - "Generate A/B test variants for screenshots"
# - "Test messaging approach: benefit-driven vs feature-driven"

# 2. Review test setup guide
cat outputs/MyApp/03-testing/ab-test-setup.md

# 3. Configure tests in App Store Connect
# Follow step-by-step guide

# 4. Monitor weekly
# Use action-testing.md checklist

# 5. Analyze results after 2-4 weeks
# Make decision based on statistical significance

# 6. Apply winning variant
# Update metadata files

# 7. Plan next test
# Continuous optimization
```

**Test Ideas:**
- Screenshot messaging (benefit vs feature)
- App icon variations
- First screenshot emphasis (different value props)
- Title phrasing

---

### Workflow 5: Pre-Launch Validation

**Goal:** Ensure app is ready for submission

**Steps:**
```bash
# 1. Run pre-launch check
/aso-prelaunch MyApp

# 2. Work through checklist
cat outputs/MyApp/04-launch/prelaunch-checklist.md

# 47 items covering:
# - Metadata validation (12 items)
# - Visual assets validation (11 items)
# - Technical validation (8 items)
# - Legal & compliance (7 items)
# - Marketing & support (9 items)

# 3. Fix any issues identified
# Each checklist item has validation criteria

# 4. Verify timeline
cat outputs/MyApp/04-launch/timeline.md
# Confirm dates are realistic

# 5. Review submission guide
cat outputs/MyApp/04-launch/submission-guide.md
# Understand review process

# 6. Submit when all 47 items checked
```

**Pro Tips:**
- Start checklist 1 week before planned submission
- Catch issues early (esp. legal/compliance)
- Have demo account ready (Apple requires for some apps)

---

## Agent-Specific Usage

### Using aso-master Directly

**When:**
- Complex workflows requiring coordination
- Custom workflows not covered by slash commands

**How:**
```
# In Claude Code conversation:
"Can you invoke the aso-master agent to create a custom ASO workflow for my app?
I need research for keywords 'fitness' and 'workout', metadata for Apple only,
and skip the testing phase."

# aso-master will:
# 1. Understand your custom requirements
# 2. Coordinate appropriate specialist agents
# 3. Generate tailored outputs
```

---

### Using aso-research Directly

**When:**
- Need only research (no metadata generation)
- Exploring new market/category
- Competitive intelligence

**How:**
```
"Can you invoke the aso-research agent to analyze the top 10 apps
in the 'productivity' category and identify keyword opportunities?"
```

---

### Using aso-optimizer Directly

**When:**
- Have research done, need metadata only
- Generating A/B test variants
- Updating metadata for new version

**How:**
```
"Can you invoke the aso-optimizer agent to generate metadata
for my productivity app using these keywords: [list]?"
```

---

### Using aso-strategist Directly

**When:**
- Need launch planning only
- Creating timeline for major update
- ASO health score calculation

**How:**
```
"Can you invoke the aso-strategist agent to create a launch timeline
for my app submission on November 15, 2025?"
```

---

## Advanced Usage

### Custom Workflows

**Scenario:** You want research + metadata, but skip testing and launch planning

**Solution:**
```
# In Claude Code:
"Invoke aso-master with this custom workflow:
1. aso-research: Analyze competitors [list]
2. aso-optimizer: Generate metadata for Apple only
3. Skip testing phase
4. Skip launch phase
5. Output only research and metadata folders"

# aso-master will coordinate accordingly
```

---

### Localization

**Scenario:** You need ASO for multiple languages

**Solution:**
```bash
# Run audit for primary language first
/aso-full-audit MyApp

# Then request localization
"Can you invoke aso-optimizer to create localized metadata for:
- Spanish (Spain)
- German
- French
Based on the English metadata in outputs/MyApp/02-metadata/"
```

---

### Integration with Development Workflow

**Scenario:** Integrate ASO into CI/CD pipeline

**Solution:**
```bash
# Run audit programmatically
python3 .claude/skills/aso/keyword_analyzer.py < input.json > output.json

# Parse results in CI
# Use for automated metadata validation
```

---

## Output Structure Reference

Every `/aso-full-audit` generates this structure:

```
outputs/[AppName]/
├── 00-MASTER-ACTION-PLAN.md      # Your roadmap (start here)
│
├── 01-research/
│   ├── keyword-list.md           # Keywords with implementation guide
│   ├── competitor-gaps.md        # Opportunities vs competitors
│   └── action-research.md        # Research tasks checklist
│
├── 02-metadata/
│   ├── apple-metadata.md         # Copy-paste to App Store Connect
│   ├── google-metadata.md        # Copy-paste to Play Console
│   ├── visual-assets-spec.md     # Brief for designer
│   └── action-metadata.md        # Implementation tasks
│
├── 03-testing/
│   ├── ab-test-setup.md          # Test configuration guide
│   └── action-testing.md         # Testing tasks
│
├── 04-launch/
│   ├── prelaunch-checklist.md    # 47-item validation
│   ├── timeline.md               # Calendar dates (not placeholders!)
│   ├── submission-guide.md       # App Store & Play Store procedures
│   └── action-launch.md          # Launch tasks
│
├── 05-optimization/
│   ├── review-responses.md       # Templates for review replies
│   ├── ongoing-tasks.md          # Daily/weekly/monthly schedule
│   └── action-optimization.md    # Ongoing optimization tasks
│
└── FINAL-REPORT.md               # Executive summary with ASO score
```

---

## Best Practices

### 1. Start with Full Audit

Always run `/aso-full-audit` first, even if you think you only need metadata. The comprehensive research informs better metadata.

### 2. Follow Master Action Plan

The `00-MASTER-ACTION-PLAN.md` is your roadmap. Follow it sequentially for best results.

### 3. Use Real Data

When agents prompt for competitor names, provide real apps (not hypotheticals). The system fetches real data via iTunes API.

### 4. Update Regularly

Re-run audits quarterly to:
- Update keyword strategy
- Refresh competitive intelligence
- Recalculate ASO health score

### 5. Document Changes

When you implement changes, document what you did and when in the action checklists. Track your progress.

### 6. Monitor Weekly

Use `ongoing-tasks.md` schedule for consistent monitoring. Set calendar reminders.

### 7. A/B Test Continuously

Always have at least one A/B test running. Continuous optimization is key to ASO success.

---

## Common Use Cases

### Use Case: "My app isn't getting installs"

```bash
# Run full audit
/aso-full-audit MyApp

# Focus on:
# 1. Keyword rankings (01-research/keyword-list.md)
# 2. Conversion rate baseline (FINAL-REPORT.md)
# 3. Quick wins (00-MASTER-ACTION-PLAN.md)

# Likely issues:
# - Not ranking for priority keywords
# - Low conversion rate (poor visuals/messaging)
# - Wrong category selection
```

---

### Use Case: "My competitor just launched and is ranking higher"

```bash
# Analyze competitor
/aso-competitor MyApp "NewCompetitor"

# Review outputs:
# - What keywords are they targeting?
# - What's their messaging approach?
# - What can you learn from their strategy?

# Then optimize your metadata
/aso-optimize MyApp
# Incorporate insights
```

---

### Use Case: "I need to launch in 2 weeks"

```bash
# Fast-track workflow
/aso-full-audit MyApp

# Prioritize:
# 1. Implement metadata immediately (Day 1-2)
# 2. Skip A/B testing (do post-launch)
# 3. Fast-track visual assets (Day 3-5)
# 4. Validate pre-launch (Day 6)
# 5. Submit (Day 7)
# 6. Launch (Day 14)

# Use quick wins from master action plan
```

---

### Use Case: "I want to improve my 3.5★ rating"

```bash
# While ASO focuses on discovery (not ratings directly), you can:

# 1. Analyze review themes
cat outputs/MyApp/05-optimization/review-responses.md

# 2. Identify common complaints
# Use templates to respond professionally

# 3. Address bugs mentioned in reviews
# Prioritize critical issues

# 4. Use "What's New" to highlight fixes
# Show users you're listening

# 5. Improve onboarding (reduces 1-star "doesn't work" reviews)
# Better first impression = better ratings
```

---

## Troubleshooting

### Issue: Agent prompts for information you don't have

**Example:** "What's your average conversion rate?"

**Solution:**
- If unknown, say "Unknown" or "Not tracked yet"
- Agents will use industry benchmarks
- You can update later with real data

---

### Issue: Metadata exceeds character limits

**Solution:**
- This should never happen—agents validate character counts
- If it does, review metadata files
- Use character counter: `echo "text" | wc -c`
- Edit to fit limits (see data_sources.md for limits)

---

### Issue: Competitor data not found via iTunes API

**Solution:**
- Verify competitor app name spelling
- Try searching App Store manually first
- Use exact app name from App Store
- If still not found, provide manual data

---

### Issue: Outputs folder is messy (multiple runs)

**Solution:**
```bash
# Agents backup old outputs automatically
# Find backups:
ls outputs/*.backup.*

# Clean up old backups after confirming current outputs are good:
rm -rf outputs/*.backup.*
```

---

## Tips and Tricks

### Tip 1: Bookmark Output README

```bash
# Keep this open while working
open outputs/README.md
```

### Tip 2: Use Templates for Reviews

```bash
# Copy templates to notes app for quick access
cat outputs/MyApp/05-optimization/review-responses.md
```

### Tip 3: Set Calendar Reminders

Based on `ongoing-tasks.md` schedule:
- Daily: 10 minutes (crash monitoring, review responses)
- Weekly: 1 hour (keyword rankings, A/B tests)
- Monthly: 2 hours (comprehensive review)

### Tip 4: Track ASO Score Over Time

```bash
# Create tracking spreadsheet
# Month | ASO Score | Impressions | CVR | Installs
# Nov   | 62/100    | 10,000     | 5%  | 500
# Dec   | 68/100    | 15,000     | 6%  | 900
```

### Tip 5: Collaborate with Team

Share outputs folder with team:
- Designer: `02-metadata/visual-assets-spec.md`
- Developer: `04-launch/prelaunch-checklist.md` (technical items)
- Marketing: `00-MASTER-ACTION-PLAN.md` (overview)

---

## Success Metrics

Track these to measure ASO effectiveness:

### Week 1
- [ ] Keyword rankings improved for 3+ priority keywords
- [ ] Conversion rate baseline established

### Month 1
- [ ] 20% increase in impressions
- [ ] 10% increase in conversion rate

### Month 3
- [ ] ASO health score +15 points
- [ ] Top 10 ranking for 5+ priority keywords

### Month 6
- [ ] 50% increase in organic installs
- [ ] 4.5+ average rating with 100+ reviews

---

## Next Steps

1. **Install the system:** See `.claude/INSTALL.md`
2. **Run your first audit:** `/aso-full-audit YourAppName`
3. **Review architecture:** See `.claude/ARCHITECTURE.md`
4. **Read implementation plan:** See `documentation/implementation/aso-agents-implementation-plan.md`

---

**Usage Guide Version:** 1.0
**Last Updated:** November 7, 2025
**Maintained By:** ASO Agent System Team
