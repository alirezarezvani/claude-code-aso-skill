# Metadata Implementation Action Checklist: {{APP_NAME}}

**Phase:** 02-metadata
**Duration:** {{DURATION}}
**Priority:** {{PRIORITY}}
**Generated:** {{DATE}}

---

## Overview

This checklist covers all tasks required to implement optimized metadata across Apple App Store and Google Play Store. All metadata files are copy-paste ready with validated character counts.

**Estimated Time:** {{ESTIMATED_HOURS}} hours

---

## Pre-Implementation Validation

- [ ] **Review Generated Metadata**
  - Read `apple-metadata.md` thoroughly
  - Read `google-metadata.md` thoroughly
  - Ensure messaging aligns with brand voice
  - **Success Criteria:** Metadata reviewed and approved by product owner

- [ ] **Verify Character Counts**
  - Apple title: {{APPLE_TITLE_LENGTH}}/30 chars ✅
  - Apple subtitle: {{APPLE_SUBTITLE_LENGTH}}/30 chars ✅
  - Apple keywords: {{APPLE_KEYWORDS_LENGTH}}/100 chars ✅
  - Google title: {{GOOGLE_TITLE_LENGTH}}/50 chars ✅
  - Google short desc: {{GOOGLE_SHORT_LENGTH}}/80 chars ✅
  - **Success Criteria:** All character counts validated

- [ ] **Check Keyword Implementation**
  - Priority keywords appear in titles
  - Secondary keywords in descriptions
  - No keyword stuffing (natural language)
  - **Success Criteria:** Keyword placement validated

---

## Apple App Store Implementation

### App Store Connect Setup

- [ ] **Log into App Store Connect**
  - URL: https://appstoreconnect.apple.com
  - Navigate to "My Apps" → {{APP_NAME}}
  - **Success Criteria:** App Store Connect accessed

- [ ] **Submit Title and Subtitle**
  - Copy title from `apple-metadata.md`
  - Paste into "Name" field (exactly as written)
  - Copy subtitle from `apple-metadata.md`
  - Paste into "Subtitle" field (exactly as written)
  - **Success Criteria:** Title and subtitle submitted

- [ ] **Submit Keywords**
  - Copy keywords from `apple-metadata.md`
  - Paste into "Keywords" field (exactly as written)
  - Verify no double spaces
  - Verify no trailing commas
  - **Success Criteria:** Keywords submitted with correct formatting

- [ ] **Submit Promotional Text** (if applicable)
  - Copy promotional text from `apple-metadata.md`
  - Paste into "Promotional Text" field
  - **Success Criteria:** Promotional text submitted

- [ ] **Submit Description**
  - Copy description from `apple-metadata.md`
  - Paste into "Description" field (exactly as written)
  - Preview formatting (bullets, line breaks)
  - **Success Criteria:** Description submitted with correct formatting

- [ ] **Submit "What's New"**
  - Copy update notes from `apple-metadata.md`
  - Paste into "What's New in This Version" field
  - **Success Criteria:** Update notes submitted

### Visual Assets Submission (Apple)

- [ ] **Prepare Designer Brief**
  - Send `visual-assets-spec.md` to designer
  - Schedule kickoff meeting to review requirements
  - Set deadline: {{VISUAL_DEADLINE}}
  - **Success Criteria:** Designer brief delivered

- [ ] **Review App Icon**
  - 1024x1024px required
  - No alpha channels
  - Follows design spec
  - **Success Criteria:** Icon approved

- [ ] **Review iPhone Screenshots**
  - 6.7" display: {{SCREENSHOT_COUNT_67}} screenshots required
  - 5.5" display: {{SCREENSHOT_COUNT_55}} screenshots required
  - Messaging matches spec
  - Order follows priority: {{SCREENSHOT_ORDER}}
  - **Success Criteria:** Screenshots approved

- [ ] **Review iPad Screenshots** (if applicable)
  - 12.9" display: {{IPAD_SCREENSHOT_COUNT}} screenshots required
  - Tablet-optimized messaging
  - **Success Criteria:** iPad screenshots approved

- [ ] **Review App Preview Video** (if applicable)
  - 30 seconds max
  - Follows script from spec
  - Clear call-to-action
  - **Success Criteria:** Video approved

- [ ] **Upload Visual Assets**
  - Upload icon to App Store Connect
  - Upload all screenshot sizes
  - Upload video (if applicable)
  - Verify all assets display correctly
  - **Success Criteria:** Visual assets uploaded and verified

### Apple Metadata Review

- [ ] **Preview App Store Listing**
  - Use App Store Connect preview tool
  - Check formatting on iPhone
  - Check formatting on iPad
  - **Success Criteria:** Listing looks correct in preview

- [ ] **Get Internal Feedback**
  - Share preview link with team
  - Collect feedback on messaging
  - Make adjustments if needed
  - **Success Criteria:** Team approval received

---

## Google Play Store Implementation

### Play Console Setup

- [ ] **Log into Play Console**
  - URL: https://play.google.com/console
  - Navigate to {{APP_NAME}}
  - **Success Criteria:** Play Console accessed

- [ ] **Submit Title**
  - Copy title from `google-metadata.md`
  - Paste into "App name" field (exactly as written)
  - **Success Criteria:** Title submitted

- [ ] **Submit Short Description**
  - Copy short description from `google-metadata.md`
  - Paste into "Short description" field (exactly as written)
  - Verify 80 char limit
  - **Success Criteria:** Short description submitted

- [ ] **Submit Full Description**
  - Copy full description from `google-metadata.md`
  - Paste into "Full description" field (exactly as written)
  - Preview formatting (HTML if used)
  - **Success Criteria:** Full description submitted

### Visual Assets Submission (Google)

- [ ] **Review App Icon**
  - 512x512px required
  - Follows design spec
  - **Success Criteria:** Icon approved

- [ ] **Review Feature Graphic**
  - 1024x500px required
  - Key messaging visible
  - Follows design spec
  - **Success Criteria:** Feature graphic approved

- [ ] **Review Phone Screenshots**
  - Min 2, max 8 screenshots
  - 16:9 or 9:16 aspect ratio
  - Messaging matches spec
  - Order follows priority: {{PLAY_SCREENSHOT_ORDER}}
  - **Success Criteria:** Screenshots approved

- [ ] **Review Tablet Screenshots** (if applicable)
  - 7" and 10" tablet screenshots
  - Tablet-optimized messaging
  - **Success Criteria:** Tablet screenshots approved

- [ ] **Review Promo Video** (if applicable)
  - YouTube URL format
  - 30-120 seconds
  - Follows script from spec
  - **Success Criteria:** Video approved

- [ ] **Upload Visual Assets**
  - Upload icon to Play Console
  - Upload feature graphic
  - Upload all screenshot sizes
  - Add promo video URL (if applicable)
  - Verify all assets display correctly
  - **Success Criteria:** Visual assets uploaded and verified

### Google Metadata Review

- [ ] **Preview Play Store Listing**
  - Use Play Console preview tool
  - Check formatting on phone
  - Check formatting on tablet
  - **Success Criteria:** Listing looks correct in preview

- [ ] **Get Internal Feedback**
  - Share preview link with team
  - Collect feedback on messaging
  - Make adjustments if needed
  - **Success Criteria:** Team approval received

---

## Localization (If Applicable)

{{LOCALIZATION_TASKS}}

---

## Quality Validation

Before submitting for review, validate:

- [ ] **Character Limits Respected**
  - All Apple fields within limits
  - All Google fields within limits
  - No truncated text
  - **Success Criteria:** Character count validation passed

- [ ] **Keywords Implemented Correctly**
  - Priority keywords in titles
  - Secondary keywords in descriptions
  - Natural language (no stuffing)
  - No duplicate keywords
  - **Success Criteria:** Keyword implementation validated

- [ ] **Messaging Consistency**
  - Same value proposition across platforms
  - Brand voice consistent
  - No contradictions between Apple/Google
  - **Success Criteria:** Messaging consistency validated

- [ ] **Visual Assets Quality**
  - All required sizes provided
  - High resolution (no pixelation)
  - Messaging clearly legible
  - Screenshots follow correct order
  - **Success Criteria:** Visual quality validated

- [ ] **Compliance Check**
  - No prohibited keywords (Apple guidelines)
  - No misleading claims
  - No competitor names (unless comparative)
  - Privacy policy linked (if required)
  - **Success Criteria:** Compliance validated

---

## Submission Tasks

### Apple App Store

- [ ] **Submit for Review**
  - Click "Submit for Review" in App Store Connect
  - Respond to any review questions
  - Estimated review time: 24-48 hours
  - **Success Criteria:** Submission successful

- [ ] **Monitor Review Status**
  - Check App Store Connect daily
  - Respond to rejection reasons immediately (if any)
  - **Success Criteria:** App approved or issues resolved

### Google Play Store

- [ ] **Submit for Review**
  - Click "Submit update" in Play Console
  - Respond to any review questions
  - Estimated review time: 2-7 days
  - **Success Criteria:** Submission successful

- [ ] **Monitor Review Status**
  - Check Play Console daily
  - Respond to rejection reasons immediately (if any)
  - **Success Criteria:** App approved or issues resolved

---

## Post-Launch Metadata Tasks

- [ ] **Verify Live Listings**
  - Search for app on App Store (verify it appears)
  - Search for app on Play Store (verify it appears)
  - Check that all metadata displays correctly
  - **Success Criteria:** Listings verified live

- [ ] **Establish Baseline Metrics**
  - Document current keyword rankings
  - Document current conversion rate
  - Document current impressions/installs
  - **Success Criteria:** Baseline metrics documented

- [ ] **Schedule First Metadata Review**
  - Set calendar reminder for 30 days
  - Plan to review A/B test results
  - Prepare to iterate based on data
  - **Success Criteria:** Review scheduled

---

## Common Issues and Fixes

### Issue: Metadata Rejected (Apple)

**Common Reasons:**
- Keyword stuffing in title/subtitle
- Misleading claims in description
- Inappropriate keywords

**Solution:**
- Review Apple App Store Review Guidelines
- Remove problematic keywords/claims
- Resubmit with clearer messaging
- **Reference:** `submission-guide.md` for detailed fixes

### Issue: Metadata Rejected (Google)

**Common Reasons:**
- Short description too vague
- Full description doesn't match app functionality
- Inappropriate content

**Solution:**
- Review Google Play Developer Policy Center
- Clarify app functionality in descriptions
- Remove any policy violations
- **Reference:** `submission-guide.md` for detailed fixes

### Issue: Low Conversion Rate

**Potential Causes:**
- Screenshots don't communicate value clearly
- Description doesn't address user pain points
- Title/subtitle unclear

**Solution:**
- Review `visual-assets-spec.md` for messaging improvements
- A/B test different screenshot messaging
- Iterate based on user feedback
- **Reference:** `ab-test-setup.md` for testing strategy

---

## Timeline

**Target Completion:** {{TARGET_DATE}}

**Breakdown:**
- Metadata submission (Apple): {{APPLE_SUBMISSION_DATE}}
- Metadata submission (Google): {{GOOGLE_SUBMISSION_DATE}}
- Visual assets delivery: {{VISUAL_DELIVERY_DATE}}
- Final submission: {{FINAL_SUBMISSION_DATE}}

---

## Handoff to Phase 3 (Testing)

When all metadata is live, proceed to Phase 3. The testing phase will:
- ✅ Set up A/B tests for metadata variations
- ✅ Monitor conversion rates
- ✅ Iterate based on data

**Phase 3 Location:** `outputs/{{APP_NAME}}/03-testing/`

---

## Support

**Questions about character limits:**
- Apple: 30/30/100 chars (title/subtitle/keywords)
- Google: 50/80/4000 chars (title/short/full)

**Questions about visual assets:**
- Review: `visual-assets-spec.md`
- Reference: Platform-specific asset guidelines

**Questions about submission:**
- Review: `submission-guide.md` (Phase 4)
- Reference: App Store Review Guidelines / Play Policy

---

**Generated by:** aso-optimizer agent
**Last Updated:** {{DATE}}
**Completion Status:** {{COMPLETION_PERCENTAGE}}%
