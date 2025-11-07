---
name: aso-full-audit
description: Complete ASO audit with keyword research, competitor intelligence, metadata optimization, and launch planning
---

# ASO Full Audit Command

Execute a comprehensive App Store Optimization audit that produces actionable deliverables across all ASO phases.

## What This Command Does

Invokes **aso-master** orchestrator to coordinate all 3 specialist agents:

1. **aso-research** - Fetches real competitor data, analyzes keywords
2. **aso-optimizer** - Generates copy-paste ready metadata for both platforms
3. **aso-strategist** - Creates launch timeline and ongoing optimization schedule

## Usage

```bash
/aso-full-audit [app-name]
```

**Example:**
```bash
/aso-full-audit FitFlow
```

## What You'll Get

Complete output folder structure at `outputs/[app-name]/`:

```
outputs/FitFlow/
├── 00-MASTER-ACTION-PLAN.md      # ⭐ Start here - consolidated checklist
├── 01-research/
│   ├── keyword-list.md            # Prioritized keywords with implementation guide
│   ├── competitor-gaps.md         # Opportunities competitors are missing
│   └── action-research.md         # Research tasks checklist
├── 02-metadata/
│   ├── apple-metadata.md          # Copy-paste ready for App Store Connect
│   ├── google-metadata.md         # Copy-paste ready for Play Console
│   ├── visual-assets-spec.md      # Icon/screenshot requirements
│   └── action-metadata.md         # Metadata implementation tasks
├── 03-testing/
│   ├── ab-test-setup.md           # Step-by-step A/B test configuration
│   └── action-testing.md          # Testing tasks
├── 04-launch/
│   ├── prelaunch-checklist.md     # 47-item validation checklist
│   ├── timeline.md                # Week-by-week schedule with specific dates
│   ├── submission-guide.md        # Platform submission instructions
│   └── action-launch.md           # Launch execution tasks
├── 05-optimization/
│   ├── review-responses.md        # Pre-written response templates
│   ├── ongoing-tasks.md           # Daily/weekly/monthly optimization schedule
│   └── action-optimization.md     # Ongoing optimization tasks
└── FINAL-REPORT.md                # Executive summary
```

## Workflow

When you run this command, aso-master will:

1. **Ask for app details:**
   - App name
   - Category
   - Key features
   - Target audience
   - Platforms (Apple, Google, or both)
   - Launch date (or TBD)

2. **Execute research phase (10-15 min):**
   - Fetch competitor data via iTunes API
   - Analyze keywords
   - Identify competitive gaps

3. **Execute optimization phase (5-7 min):**
   - Generate Apple metadata
   - Generate Google metadata
   - Create A/B testing strategy

4. **Execute strategy phase (8-10 min):**
   - Create pre-launch checklist
   - Build timeline with specific dates
   - Generate review response templates
   - Create ongoing optimization schedule

5. **Synthesize master plan (5 min):**
   - Consolidate all outputs
   - Create 00-MASTER-ACTION-PLAN.md
   - Validate completeness

**Total Time:** 30-40 minutes

## After Completion

1. Open `outputs/[app-name]/00-MASTER-ACTION-PLAN.md`
2. Review the master checklist
3. Start with Phase 1 (Research tasks)
4. Follow the plan step-by-step
5. Check off tasks as you complete them

## Prerequisites

None - the command handles everything!

## When to Use

- **New app launch:** Complete ASO foundation before submission
- **Existing app refresh:** Revamp your store presence
- **Competitive analysis:** Understand how you stack up
- **Pre-launch planning:** 4-6 weeks before launch date

## When NOT to Use

- **Quick metadata update:** Use `/aso-optimize` instead
- **Pre-launch checklist only:** Use `/aso-prelaunch` instead
- **Competitor analysis only:** Use `/aso-competitor` instead

## Data Sources

The audit fetches real data from:
- iTunes Search API (free, official Apple data)
- WebFetch scraping (App Store/Play Store pages)
- Python analysis modules (keyword_analyzer.py, competitor_analyzer.py, etc.)

## Cost

- **Time:** 30-40 minutes automated execution
- **APIs:** Free (iTunes API has no cost)
- **Optional:** Paid ASO tools (AppTweak, Sensor Tower) if you have API keys

## Example Invocation

```
You: /aso-full-audit TaskFlow

aso-master: I'll create a comprehensive ASO audit for TaskFlow. Let me gather some details:

1. What category is TaskFlow in? (e.g., Productivity, Health & Fitness)
2. What are the key features? (e.g., AI task prioritization, team collaboration)
3. Who's the target audience? (e.g., busy professionals, remote teams)
4. Which platforms? (Apple App Store, Google Play Store, or both)
5. Target launch date? (or "TBD" if not set)

[User provides answers]

aso-master: Perfect! Starting full ASO audit...

✓ Phase 1: Research (aso-research executing...)
  - Fetching competitor data from iTunes API
  - Analyzing top 5 competitors
  - Identifying keyword opportunities

✓ Phase 2: Optimization (aso-optimizer executing...)
  - Generating Apple metadata (character limits validated)
  - Generating Google metadata
  - Creating A/B testing strategy

✓ Phase 3: Strategy (aso-strategist executing...)
  - Creating pre-launch checklist (47 items)
  - Building timeline (Nov 7 → Dec 15, 2025)
  - Generating review response templates

✓ Phase 4: Synthesis (aso-master finalizing...)
  - Consolidating all outputs
  - Creating master action plan

✓ Complete! Your ASO audit is ready at:
  outputs/TaskFlow/00-MASTER-ACTION-PLAN.md

Key Findings:
- 15 high-priority keywords identified
- 3 major competitive gaps found
- Metadata optimized for both platforms
- 38-day launch timeline created

Next Steps:
1. Review the master action plan
2. Start with Phase 1: Research tasks
3. Track your progress with checkboxes
```

## Troubleshooting

**Issue:** iTunes API timeout
**Solution:** Agents will fall back to WebFetch scraping automatically

**Issue:** Can't fetch competitor data
**Solution:** aso-research will prompt you to provide competitor names manually

**Issue:** Unclear app details
**Solution:** Agents will ask clarifying questions before proceeding

## Related Commands

- `/aso-optimize [app-name]` - Quick metadata optimization only
- `/aso-prelaunch [app-name] [launch-date]` - Pre-launch checklist only
- `/aso-competitor [app-name] [competitors]` - Competitor analysis only

---

**Ready to optimize your app store presence? Run the command and follow the master plan!**
