# ASO Data Sources Documentation

**Last Updated:** November 7, 2025
**Version:** 1.0

---

## Overview

This document explains all data sources available to the ASO agent system, their capabilities, limitations, and best practices for usage.

---

## Data Source Hierarchy

### Priority Order

1. **iTunes Search API** (First choice - free, official, reliable)
2. **WebFetch Scraping** (Fallback - slower, less reliable)
3. **User-Provided Data** (Last resort - manual input)

**Rationale:** Always prefer official APIs for speed, reliability, and legal compliance. Use scraping only when APIs don't provide needed data.

---

## 1. iTunes Search API

### Overview

- **Provider:** Apple Inc.
- **Access:** Free, no authentication required
- **Documentation:** https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/
- **Rate Limit:** None officially stated (reasonable use expected)
- **Reliability:** High (99.9%+ uptime)

### Capabilities

**Available Data:**
- App metadata (title, description, developer)
- Ratings (average rating, total count)
- Category and genres
- Screenshots URLs
- Icon URL
- App Store URL
- Release date, version, file size
- Price and in-app purchases info
- Content rating

**Search Methods:**
- Search by keyword
- Search by app ID
- Search by developer
- Search by category

### Limitations

**NOT Available:**
- ❌ Keyword search volumes
- ❌ Keyword rankings (where app ranks for keywords)
- ❌ Download numbers (estimates only)
- ❌ Conversion rates
- ❌ Historical data (only current state)
- ❌ User reviews text (separate endpoint)
- ❌ "What's New" text (use WebFetch)
- ❌ Subtitle text (use WebFetch)

### Usage Examples

```bash
# Search for apps
curl "https://itunes.apple.com/search?term=todoist&entity=software&limit=5"

# Get specific app by ID
curl "https://itunes.apple.com/search?id=572688855&entity=software"

# Search by category
curl "https://itunes.apple.com/search?term=productivity&entity=software&limit=25"
```

### Python Integration

```python
from app_store_optimization.lib.itunes_api import iTunesAPI

api = iTunesAPI()

# Get competitor data
competitors = api.compare_competitors([
    "Todoist",
    "Any.do",
    "Microsoft To Do"
])

for comp in competitors:
    print(f"{comp['app_name']}: {comp['rating']}★ ({comp['ratings_count']} ratings)")
```

### Best Practices

1. **Cache Results:** Don't fetch same app multiple times in one session
2. **Batch Requests:** Fetch multiple apps in one session
3. **Handle Errors:** API may timeout, have fallback strategy
4. **Verify Results:** Check resultCount before accessing results
5. **Country Codes:** Use appropriate country code (us, gb, de, etc.)

### Data Accuracy

- **Ratings:** Real-time, accurate within minutes
- **Metadata:** Updated when developers submit changes
- **Screenshots:** Updated with each app version
- **Freshness:** Current state only, no historical data

---

## 2. WebFetch Scraping

### Overview

- **Provider:** Claude Code built-in tool
- **Access:** Available to agents
- **Method:** AI-powered web page extraction
- **Rate Limit:** Self-imposed (respectful delays)
- **Reliability:** Medium (depends on page structure)

### Capabilities

**Available Data:**
- Visual layout assessment
- "What's New" text
- Subtitle text (Apple)
- First few visible reviews
- Screenshot analysis
- Keyword rankings (position in search results)
- Competitor visual assets

**Search Methods:**
- App Store search pages
- Google Play search pages
- Individual app pages
- Category browse pages

### Limitations

**NOT Available:**
- ❌ Data behind login/paywall
- ❌ Historical data
- ❌ Private analytics
- ❌ Bulk review scraping (use iTunes review API)
- ❌ Exact search volumes

**Reliability Issues:**
- Page structure changes break scrapers
- Rate limiting can occur
- Slower than API calls (10-30 seconds per page)
- Regional variations in page layout

### Usage Pattern

```python
from app_store_optimization.lib.scraper import WebFetchPrompts

# Get App Store search results
config = WebFetchPrompts.app_store_search("productivity")

# Agent then uses:
# WebFetch(url=config["url"], prompt=config["prompt"])

# Returns: List of apps with basic metadata
```

### Best Practices

1. **Respectful Delays:** Wait 2-3 seconds between requests
2. **Limit Requests:** Max 10 pages per analysis session
3. **Fallback Strategy:** If scraping fails, use iTunes API or ask user
4. **Validate Results:** Check extracted data for completeness
5. **Cache Results:** Don't scrape same page twice

### Data Accuracy

- **Current State:** Shows what's visible right now
- **Regional:** May vary by user location
- **Device-Dependent:** Mobile vs desktop views differ
- **Freshness:** Real-time but structure-dependent

---

## 3. User-Provided Data

### Overview

- **Source:** Manual input from user
- **Reliability:** Depends on user's access to data
- **Use Case:** When APIs and scraping fail or insufficient

### When to Request User Data

1. **Search Volume Estimates**
   - User has Apple Search Ads account
   - User has Google Keyword Planner access
   - User has paid ASO tool subscription

2. **Keyword Rankings**
   - User manually checks app store
   - User has ranking tracker
   - User has ASO tool data

3. **Conversion Rates**
   - User has App Store Connect access
   - User has Play Console access
   - User tracks impression-to-install rates

4. **Competitor Intelligence**
   - User knows competitors in their niche
   - User has insider market knowledge
   - APIs can't find competitors

### How to Request

**Good Request Format:**
```
⚠️ Data Fetching Limited

I was unable to automatically fetch [specific data type] for your app.

To proceed, please provide:

1. [Specific data point 1]
   - Example: Search volume for "task manager" (if available from Apple Search Ads)
   - Or: "Unknown" if not available

2. [Specific data point 2]
   - Example: Current keyword rankings for your top 5 keywords
   - Or: "Not tracked" if not available

Alternatively, I can proceed with:
- Industry-standard estimates
- Category benchmarks
- Best-practice recommendations
```

**Bad Request Format:**
```
❌ "Please provide all your app data"  (too vague)
❌ "I need your analytics"  (unclear what's needed)
❌ "Send me everything"  (overwhelming)
```

### Best Practices

1. **Be Specific:** Ask for exact data points
2. **Provide Examples:** Show format you expect
3. **Offer Alternatives:** Give options if data unavailable
4. **Explain Why:** Tell user how data will be used
5. **Set Expectations:** Note if estimates are used

### Data Accuracy

- **Variable:** Depends on user's access and accuracy
- **Trust but Verify:** Validate user inputs for reasonableness
- **Document Source:** Note when using user estimates vs API data

---

## 4. Optional Paid APIs (Future)

### Overview

Third-party ASO tools provide additional data not available from free sources.

### AppTweak

- **Cost:** $300/month
- **Data:** Keyword rankings, search volume estimates, ASO score
- **API:** RESTful
- **Setup:** Requires API key
- **Accuracy:** Industry estimates (not official data)

### Sensor Tower

- **Cost:** $500/month
- **Data:** Download estimates, revenue estimates, competitive intelligence
- **API:** RESTful
- **Setup:** Requires API key
- **Accuracy:** Proprietary algorithms (generally reliable)

### App Annie (data.ai)

- **Cost:** $1000+/month
- **Data:** Global market data, category insights, user engagement
- **API:** RESTful
- **Setup:** Requires API key
- **Accuracy:** Industry-leading (large data set)

### Integration Strategy

**Phase 1 (Current):** Free tier only (iTunes API + WebFetch)
**Phase 2 (Future):** Optional paid API support

**Implementation:**
```python
# Check for API key in environment
import os

if os.getenv("APPTWEAK_API_KEY"):
    # Use AppTweak for keyword volumes
    pass
else:
    # Fall back to iTunes API + estimates
    pass
```

---

## Data Source Comparison

| Data Type | iTunes API | WebFetch | User Input | Paid APIs |
|-----------|------------|----------|------------|-----------|
| **App Metadata** | ✅ Excellent | ⚠️ Good | ❌ Manual | ✅ Excellent |
| **Ratings/Reviews** | ✅ Excellent | ⚠️ Limited | ❌ Manual | ✅ Excellent |
| **Search Volume** | ❌ No | ❌ No | ⚠️ If available | ✅ Yes (estimates) |
| **Keyword Rankings** | ❌ No | ⚠️ Top 10 only | ⚠️ If tracked | ✅ Yes (all positions) |
| **Download Numbers** | ❌ No | ❌ No | ⚠️ If tracked | ✅ Yes (estimates) |
| **Competitor Data** | ✅ Yes | ⚠️ Limited | ❌ Manual | ✅ Excellent |
| **Speed** | ⚡ Fast (< 5s) | 🐌 Slow (10-30s) | ⏱️ Varies | ⚡ Fast (< 5s) |
| **Reliability** | ✅ 99%+ | ⚠️ 80-90% | ⚠️ Variable | ✅ 95%+ |
| **Cost** | 💚 Free | 💚 Free | 💚 Free | 💰 $300-1000/mo |

---

## Estimation Techniques

When real data isn't available, use these estimation methods:

### Search Volume Estimates

**Method 1: Category Benchmarks**
```
High-volume keywords (fitness, game, music): 100K+/month
Medium-volume keywords (task manager, photo editor): 20-50K/month
Low-volume keywords (niche terms): 1-10K/month
Long-tail keywords (3+ words): 500-5K/month
```

**Method 2: Relative Popularity**
- Compare to known keywords
- Use Google Trends for relative comparison
- Estimate based on competitor count

### Keyword Difficulty Estimates

**Formula:**
```python
difficulty = (competing_apps / 50000) * 0.7 + (search_volume / 1000000) * 0.3
difficulty_score = difficulty * 100  # 0-100 scale
```

**Categories:**
- Low: < 30 (good opportunity)
- Medium: 30-60 (moderate competition)
- High: 60-80 (challenging)
- Very High: 80+ (extremely competitive)

### Competition Level

**Thresholds:**
```python
competing_apps < 1000: Low competition
1000 ≤ competing_apps < 5000: Medium competition
5000 ≤ competing_apps < 10000: High competition
competing_apps ≥ 10000: Very high competition
```

---

## Data Quality Guidelines

### Always Document

When using any data source, document:
1. **Source:** Where data came from (API, scraping, user, estimate)
2. **Timestamp:** When data was fetched
3. **Confidence:** High (API), Medium (scraping), Low (estimate)
4. **Limitations:** What the data doesn't include

**Example:**
```markdown
## Keyword Analysis - Task Manager

**Data Source:** iTunes Search API + User Estimates
**Fetched:** November 7, 2025, 10:30 AM PST
**Confidence:** High (API data), Low (search volume estimates)

- Search Volume: 45,000/month (estimated based on category benchmarks)
- Competing Apps: 850 (exact, from iTunes API search)
- Average Rating: 4.5★ (exact, from iTunes API)

**Limitations:**
- Search volume is estimated (no official Apple data available)
- Competing apps count based on keyword search results
- Regional data is US-only
```

### Validation Checks

Before using data, validate:
```python
# Validation checks
assert 0 <= rating <= 5, "Rating must be 0-5"
assert ratings_count >= 0, "Ratings count can't be negative"
assert len(title) <= 30, "Apple title must be ≤ 30 chars"
assert 0 <= conversion_rate <= 1, "CVR must be 0-100%"
```

---

## Troubleshooting

### Issue: iTunes API timeout

**Cause:** Network issues, server overload
**Solution:**
1. Retry after 5 seconds
2. If fails again, use WebFetch
3. If both fail, ask user for data

### Issue: WebFetch extraction incomplete

**Cause:** Page structure changed, unclear prompt
**Solution:**
1. Refine prompt to be more specific
2. Try alternative scraping approach
3. Fall back to iTunes API
4. Ask user for missing data

### Issue: Data inconsistency

**Cause:** Different sources, timing delays
**Solution:**
1. Document source for each data point
2. Prefer most recent data
3. Note discrepancies in output
4. Use most conservative estimate

### Issue: Rate limiting

**Cause:** Too many requests in short time
**Solution:**
1. Implement delays (2-3 seconds)
2. Cache results to avoid repeat requests
3. Batch requests when possible
4. Switch to alternative data source

---

## Legal & Ethical Considerations

### iTunes Search API

✅ **Allowed:**
- Commercial use
- Competitive analysis
- ASO research
- Integration into tools

❌ **Not Allowed:**
- Excessive requests (DDoS-like behavior)
- Scraping for unrelated purposes
- Redistributing Apple's data without attribution

### Web Scraping

✅ **Allowed:**
- Scraping public data
- Competitive research
- Personal use

❌ **Not Allowed:**
- Bypassing technical measures
- Scraping at scale that burdens servers
- Violating robots.txt
- Using scraped data for spam

### User Privacy

✅ **Always:**
- Only request data user has access to
- Explain how data will be used
- Store data securely
- Delete after analysis

❌ **Never:**
- Request passwords or API keys directly
- Store sensitive user data
- Share user data with third parties

---

## Future Enhancements

### Planned (Phase 2)

1. **iTunes Review API Integration**
   - Bulk review fetching
   - Sentiment analysis
   - Feature request extraction

2. **Optional Paid API Support**
   - AppTweak integration (if user has API key)
   - Sensor Tower integration
   - Environment variable configuration

3. **Caching Layer**
   - Local cache for recent API responses
   - Reduce redundant requests
   - Faster subsequent analyses

4. **Historical Data Tracking**
   - Store snapshots of rankings over time
   - Track competitor changes
   - Trend analysis

---

## Summary

**Primary Data Source:** iTunes Search API (free, reliable, official)
**Fallback:** WebFetch scraping (slower, less reliable)
**Last Resort:** User-provided data (variable accuracy)
**Future:** Optional paid APIs (better data, requires subscription)

**Key Principle:** Always prefer official APIs, use scraping only when necessary, document all data sources clearly, validate data quality.

---

**Questions?** Refer to implementation plan: `documentation/implementation/aso-agents-implementation-plan.md`
