---
name: aso-prelaunch
description: Generate comprehensive pre-launch checklist and timeline with specific dates for app store submission
---

# ASO Pre-Launch Command

Create a detailed pre-launch checklist and week-by-week timeline to ensure successful app store submission.

## Usage

```bash
/aso-prelaunch [app-name] [launch-date]
```

**Examples:**
```bash
/aso-prelaunch TaskFlow 2025-12-15
/aso-prelaunch FitFlow TBD
```

## What This Command Does

Invokes **aso-strategist** directly to generate:

- Pre-launch checklist (47 validation items)
- Week-by-week timeline with specific calendar dates
- Submission guides for both platforms
- Review response templates
- Ongoing optimization schedule

## Output

Creates `outputs/[app-name]/04-launch/` and `outputs/[app-name]/05-optimization/` with:
- `prelaunch-checklist.md` - Complete validation before submission
- `timeline.md` - Specific dates from today to launch
- `submission-guide.md` - Step-by-step submission instructions
- `review-responses.md` - Pre-written response templates
- `ongoing-tasks.md` - Daily/weekly/monthly optimization tasks

## When to Use

- **4-6 weeks before launch:** Plan your launch timeline
- **First-time launch:** Need comprehensive checklist
- **Multi-platform launch:** Coordinating Apple + Google
- **Soft launch planning:** Phased rollout strategy

## Time

8-10 minutes

## Required Information

- App name
- Launch date (or "TBD" for estimate)
- Platforms (Apple, Google, or both)
- App maturity (pre-launch, soft launch, or already live)

## Example

```
You: /aso-prelaunch TaskFlow 2025-12-15

aso-strategist: Creating launch plan for TaskFlow (launch: Dec 15, 2025)

Today: November 7, 2025
Time to launch: 38 days (5.4 weeks)

Generating:
- Pre-launch checklist (47 items across 7 phases)
- Timeline (Nov 7 → Dec 15 with specific dates)
- Submission guides
- Review response templates

✓ Complete!

Your launch timeline: outputs/TaskFlow/04-launch/timeline.md

Key Milestones:
- Nov 13: Metadata finalized
- Nov 28: Soft launch (New Zealand)
- Dec 15: GLOBAL LAUNCH 🚀

Next: Review prelaunch-checklist.md and start Phase 1
```
