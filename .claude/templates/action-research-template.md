# Research Phase Action Checklist: {{APP_NAME}}

**Phase:** 01-research
**Duration:** {{DURATION}}
**Priority:** {{PRIORITY}}
**Generated:** {{DATE}}

---

## Overview

This checklist covers all research tasks required to establish your ASO strategy. Complete these tasks before moving to metadata implementation.

**Estimated Time:** {{ESTIMATED_HOURS}} hours

---

## Keyword Research Tasks

### Primary Keywords

- [ ] **Validate Priority Keywords with Apple Search Ads**
  - Sign up for Apple Search Ads account (free)
  - Use Keyword Tool to check search volumes
  - Document actual search volumes in `keyword-list.md`
  - **Success Criteria:** Search volumes documented for top 10 keywords

- [ ] **Research Long-Tail Keyword Opportunities**
  - Use keyword combinations from `keyword-list.md`
  - Test searches in App Store to see competitors
  - Document 10+ long-tail keywords (3+ words)
  - **Success Criteria:** 10 long-tail keywords with low competition (<30 difficulty)

- [ ] **Analyze Keyword Difficulty vs Opportunity**
  - Review difficulty scores in `keyword-list.md`
  - Identify "sweet spot" keywords (medium volume, low competition)
  - Prioritize 5 keywords for immediate focus
  - **Success Criteria:** 5 priority keywords identified with implementation plan

### Secondary Keywords

{{SECONDARY_KEYWORD_TASKS}}

---

## Competitor Analysis Tasks

### Direct Competitors

- [ ] **Test Top 3 Competitor Apps**
  - Download and use: {{COMPETITOR_1}}, {{COMPETITOR_2}}, {{COMPETITOR_3}}
  - Document user experience (onboarding, core features, pain points)
  - Take screenshots of key features
  - **Success Criteria:** Detailed UX notes for each competitor

- [ ] **Analyze Competitor Metadata**
  - Review titles, subtitles, descriptions from `competitor-gaps.md`
  - Identify keywords they're targeting
  - Note messaging strategies (benefit-driven vs feature-driven)
  - **Success Criteria:** Keyword overlap analysis completed

- [ ] **Identify Competitive Gaps**
  - Compare your features to competitor features
  - Document what they're missing (your opportunities)
  - Note their weaknesses (poor ratings, confusing UX, etc.)
  - **Success Criteria:** 5+ competitive advantages documented

### Indirect Competitors

{{INDIRECT_COMPETITOR_TASKS}}

---

## Target Audience Research

- [ ] **Define Primary User Persona**
  - Age range: {{AGE_RANGE}}
  - Use case: {{USE_CASE}}
  - Pain points: {{PAIN_POINTS}}
  - **Success Criteria:** Persona documented with specific demographics

- [ ] **Identify User Search Intent**
  - What problem are users solving?
  - What keywords would they use?
  - What alternative solutions exist?
  - **Success Criteria:** User intent mapped to keyword strategy

- [ ] **Analyze Review Themes**
  - Read 20+ reviews of competitor apps
  - Identify common complaints (your opportunities)
  - Note desired features (your roadmap)
  - **Success Criteria:** Review themes documented in `competitor-gaps.md`

---

## Category Research

- [ ] **Analyze Category Positioning**
  - Current category: {{CURRENT_CATEGORY}}
  - Alternative categories to consider: {{ALT_CATEGORIES}}
  - Top apps in each category
  - **Success Criteria:** Category strategy documented with reasoning

- [ ] **Review Category-Specific Keywords**
  - Browse App Store category pages
  - Note keywords used by top apps
  - Identify category-specific trends
  - **Success Criteria:** 5+ category keywords added to strategy

---

## Visual Research

- [ ] **Screenshot Analysis**
  - Review top 10 competitor screenshots
  - Note common messaging patterns
  - Identify effective visual hierarchies
  - Document dos and don'ts
  - **Success Criteria:** Screenshot strategy brief created for designer

- [ ] **Icon Analysis**
  - Review top 10 competitor icons
  - Note color schemes and symbolism
  - Identify differentiation opportunities
  - **Success Criteria:** Icon design brief created for designer

- [ ] **App Preview Videos** (if applicable)
  - Review competitor videos
  - Note video lengths and structures
  - Document effective storytelling approaches
  - **Success Criteria:** Video script outline created

---

## Data Validation Tasks

- [ ] **Verify Competitor Data Accuracy**
  - Cross-reference iTunes API data with manual checks
  - Confirm ratings and review counts are current
  - Update any outdated information
  - **Success Criteria:** All competitor data verified within 7 days

- [ ] **Document Data Sources**
  - Note which data came from iTunes API
  - Note which data came from WebFetch
  - Note which data came from manual research
  - **Success Criteria:** Data sources clearly documented in all files

- [ ] **Validate Keyword Search Volumes**
  - If using Apple Search Ads data, confirm accuracy
  - If using estimates, note confidence level
  - Document methodology for estimates
  - **Success Criteria:** Search volume methodology documented

---

## Platform-Specific Research

### Apple App Store

- [ ] **Review Apple Search Ads Data** (if available)
  - Check exact search volumes
  - Note competition levels
  - Document cost-per-tap estimates
  - **Success Criteria:** Apple Search Ads insights documented

- [ ] **Analyze App Store Search Results**
  - Search for your priority keywords
  - Note which apps appear in top 10
  - Identify patterns in top-ranking apps
  - **Success Criteria:** Search result analysis completed for 10 keywords

### Google Play Store

- [ ] **Analyze Play Store Search Results**
  - Search for your priority keywords
  - Note which apps appear in top 10
  - Compare to App Store results (differences?)
  - **Success Criteria:** Play Store analysis completed for 10 keywords

- [ ] **Review Google Play Console Data** (if available)
  - Check organic vs paid traffic
  - Note conversion rates by keyword
  - Document user acquisition costs
  - **Success Criteria:** Play Console insights documented

---

## Documentation Tasks

- [ ] **Update keyword-list.md**
  - Add any new keywords discovered
  - Update search volumes with real data
  - Adjust difficulty scores based on research
  - **Success Criteria:** keyword-list.md reflects latest research

- [ ] **Update competitor-gaps.md**
  - Add detailed UX analysis notes
  - Include screenshots of competitor features
  - Document competitive advantages
  - **Success Criteria:** competitor-gaps.md is comprehensive reference

- [ ] **Create Research Summary**
  - Key findings (3-5 bullet points)
  - Top opportunities identified
  - Recommended next steps
  - **Success Criteria:** Research summary added to both files

---

## Quality Validation

Before moving to Phase 2 (Metadata), validate:

- [ ] **Keyword Strategy Complete**
  - 10+ primary keywords with search volumes
  - 10+ long-tail keywords with low competition
  - 5 priority keywords identified for immediate focus
  - Implementation guide for each keyword (where to use)

- [ ] **Competitor Analysis Complete**
  - 3+ direct competitors analyzed (UX tested)
  - Metadata comparison completed
  - 5+ competitive gaps identified
  - Review themes documented

- [ ] **Data Quality Verified**
  - All data sources documented
  - Outdated information updated
  - Confidence levels noted for estimates
  - iTunes API data validated

---

## Handoff to Phase 2 (Metadata)

When all tasks are complete, proceed to Phase 2. The metadata implementation phase will use:
- ✅ Priority keywords from research
- ✅ Competitor insights for messaging
- ✅ User pain points for benefit-driven copy
- ✅ Visual research for designer brief

**Phase 2 Location:** `outputs/{{APP_NAME}}/02-metadata/`

---

## Timeline

**Target Completion:** {{TARGET_DATE}}

**Daily Breakdown:**
{{DAILY_BREAKDOWN}}

---

## Support

**Questions about keyword research:**
- Review: `keyword-list.md` for methodology
- Reference: `app-store-optimization/lib/data_sources.md`

**Questions about competitor analysis:**
- Review: `competitor-gaps.md` for analysis framework
- Reference: iTunes Search API for data fetching

**Questions about data sources:**
- Review: `app-store-optimization/lib/data_sources.md`
- Reference: Implementation plan for API details

---

**Generated by:** aso-research agent
**Last Updated:** {{DATE}}
**Completion Status:** {{COMPLETION_PERCENTAGE}}%
