---
name: aso-optimize
description: Quick metadata optimization for Apple App Store and Google Play Store with copy-paste ready content
---

# ASO Optimize Command

Generate copy-paste ready app store metadata optimized for discoverability and conversion.

## Usage

```bash
/aso-optimize [app-name]
```

**Example:**
```bash
/aso-optimize TaskFlow
```

## What This Command Does

Invokes **aso-optimizer** directly (bypasses research and strategy phases) to quickly generate:

- Apple App Store metadata (title, subtitle, keywords, description)
- Google Play Store metadata (title, short desc, full desc)
- Character limit validation
- A/B testing recommendations

## Output

Creates `outputs/[app-name]/02-metadata/` with:
- `apple-metadata.md` - Ready to paste into App Store Connect
- `google-metadata.md` - Ready to paste into Play Console
- `visual-assets-spec.md` - Icon/screenshot requirements
- `action-metadata.md` - Implementation checklist

## When to Use

- **Metadata refresh:** Update existing app's store listing
- **Quick optimization:** Need metadata fast without full audit
- **Post-research:** Already have keywords, just need metadata written
- **Platform expansion:** Adding Google Play after Apple launch

## Time

5-7 minutes

## Required Information

- App name and category
- Key features (3-5 bullets)
- Target keywords (or will use defaults for category)
- Platforms (Apple, Google, or both)

## Example

```
You: /aso-optimize FitFlow

aso-optimizer: I'll optimize metadata for FitFlow. Quick questions:

1. Category? (e.g., Health & Fitness)
2. Top 5 keywords? (or I can suggest based on category)
3. Key features? (e.g., AI workout plans, nutrition tracking)
4. Platform? (Apple, Google, or both)

[User provides]

aso-optimizer: Generating optimized metadata...

✓ Apple metadata complete (all character limits validated)
✓ Google metadata complete
✓ A/B test strategy included

Your copy-paste ready metadata is at:
outputs/FitFlow/02-metadata/apple-metadata.md

Next: Copy into App Store Connect and submit!
```
