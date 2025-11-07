---
name: aso-competitor
description: Competitive intelligence analysis with keyword gaps and opportunities identification
---

# ASO Competitor Analysis Command

Deep-dive competitive intelligence to identify what competitors are doing well and where opportunities exist.

## Usage

```bash
/aso-competitor [app-name] [competitor1,competitor2,...]
```

**Examples:**
```bash
/aso-competitor TaskFlow "Todoist,Any.do,Microsoft To Do"
/aso-competitor FitFlow auto
```

Use `auto` to automatically discover top 5 competitors in the category.

## What This Command Does

Invokes **aso-research** in competitor-analysis mode to:

- Fetch real competitor data via iTunes API
- Analyze competitor ASO strategies
- Identify keyword gaps (what they're missing)
- Extract best practices
- Provide actionable recommendations

## Output

Creates `outputs/[app-name]/01-research/` with:
- `competitor-gaps.md` - Opportunities analysis
- `competitor-intelligence.md` - Detailed competitor breakdown
- `action-research.md` - Competitive positioning tasks

## When to Use

- **Market entry:** Understand competitive landscape
- **Differentiation:** Find your unique positioning
- **Keyword strategy:** Discover underutilized keywords
- **Best practices:** Learn from successful competitors

## Time

10-15 minutes

## Required Information

- App name and category
- Competitor names (or "auto" to discover)
- Platform (Apple or Google)

## Example

```
You: /aso-competitor TaskFlow "Todoist,Any.do,Microsoft To Do"

aso-research: Analyzing 3 competitors for TaskFlow...

✓ Fetching Todoist data from iTunes API
  - Rating: 4.7 (150K ratings)
  - Title: "Todoist: To-Do List & Tasks"
  - Keywords: todo, task, organize

✓ Fetching Any.do data
  - Rating: 4.6 (89K ratings)
  - Title: "Any.do - To do list & Tasks"
  - Keywords: todo, calendar, reminders

✓ Fetching Microsoft To Do data
  - Rating: 4.8 (210K ratings)
  - Title: "Microsoft To Do"
  - Keywords: lists, planner, task

✓ Running competitor analysis...

Key Findings:
- 0/3 competitors mention "AI" → BIG OPPORTUNITY
- 2/3 focus on personal use (not team)
- All use generic "todo" keywords

Your competitive gaps report is ready:
outputs/TaskFlow/01-research/competitor-gaps.md

Top Recommendations:
1. Emphasize AI features (zero competition)
2. Target team collaboration keywords
3. Differentiate with "smart prioritization"

Next: Use these insights in your metadata
```

## Data Sources

- iTunes Search API (real-time competitor data)
- WebFetch scraping (if API insufficient)
- competitor_analyzer.py (Python analysis module)

## Related Commands

- `/aso-full-audit` - Complete ASO with competitors included
- `/aso-optimize` - Use competitor insights for metadata
