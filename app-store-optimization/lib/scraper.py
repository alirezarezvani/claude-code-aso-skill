"""
Web scraping utilities for App Store and Google Play Store data.
Uses Claude Code's WebFetch tool for agent-based scraping.

Note: This module is designed to be used by ASO agents, not run standalone.
Agents have access to the WebFetch tool which handles the actual HTTP requests.
"""

from typing import Dict, List, Any, Optional


class WebFetchPrompts:
    """
    Prompts for WebFetch tool when scraping app store pages.
    These are used by agents to extract specific data.
    """

    @staticmethod
    def app_store_search(keyword: str) -> Dict[str, str]:
        """
        Generate WebFetch prompt for App Store search results.

        Args:
            keyword: Search keyword

        Returns:
            Dictionary with URL and prompt for WebFetch
        """
        url = f"https://apps.apple.com/us/search?term={keyword.replace(' ', '+')}"
        prompt = f"""
        Extract information about the top 10 apps shown in search results for "{keyword}".

        For each app, provide:
        1. App name
        2. Developer name
        3. Category
        4. Icon URL (if visible)
        5. App Store URL/link
        6. Brief tagline or description snippet
        7. Rating (if visible)

        Format as JSON array with these fields.
        """

        return {
            "url": url,
            "prompt": prompt
        }

    @staticmethod
    def app_store_app_page(app_url: str) -> Dict[str, str]:
        """
        Generate WebFetch prompt for individual App Store app page.

        Args:
            app_url: Full URL to app page

        Returns:
            Dictionary with URL and prompt for WebFetch
        """
        prompt = """
        Extract the following information from this App Store app page:

        **Metadata:**
        1. App title (exact text)
        2. Subtitle (if present)
        3. Developer name
        4. Category
        5. Full description text
        6. "What's New" section (latest update)
        7. App Store URL

        **Ratings & Reviews:**
        8. Average rating (e.g., 4.7)
        9. Total number of ratings
        10. Recent reviews (first 3-5 visible reviews with rating and text)

        **Visual Assets:**
        11. Number of screenshots shown
        12. Does it have an app preview video? (yes/no)

        **Additional Info:**
        13. Age rating
        14. Languages supported (if listed)
        15. File size
        16. Price or "Free"

        Format as structured JSON with these fields.
        """

        return {
            "url": app_url,
            "prompt": prompt
        }

    @staticmethod
    def play_store_search(keyword: str) -> Dict[str, str]:
        """
        Generate WebFetch prompt for Google Play Store search results.

        Args:
            keyword: Search keyword

        Returns:
            Dictionary with URL and prompt for WebFetch
        """
        url = f"https://play.google.com/store/search?q={keyword.replace(' ', '+')}&c=apps"
        prompt = f"""
        Extract information about the top 10 apps shown in search results for "{keyword}".

        For each app, provide:
        1. App name
        2. Developer name
        3. Category
        4. Play Store URL/package name
        5. Brief description snippet
        6. Rating (if visible)
        7. Number of downloads range (e.g., "1M+")

        Format as JSON array with these fields.
        """

        return {
            "url": url,
            "prompt": prompt
        }

    @staticmethod
    def play_store_app_page(app_url_or_package: str) -> Dict[str, str]:
        """
        Generate WebFetch prompt for individual Google Play Store app page.

        Args:
            app_url_or_package: Full URL or package name (e.g., com.todoist)

        Returns:
            Dictionary with URL and prompt for WebFetch
        """
        # Handle both full URLs and package names
        if app_url_or_package.startswith("http"):
            url = app_url_or_package
        else:
            url = f"https://play.google.com/store/apps/details?id={app_url_or_package}"

        prompt = """
        Extract the following information from this Google Play Store app page:

        **Metadata:**
        1. App title (exact text)
        2. Developer name
        3. Category
        4. Short description (first paragraph/tagline)
        5. Full description text
        6. "What's new" section (latest update notes)

        **Ratings & Reviews:**
        7. Average rating (e.g., 4.5)
        8. Total number of reviews
        9. Rating distribution (5-star, 4-star, etc. percentages if visible)
        10. Recent reviews (first 3-5 visible reviews with rating and text)

        **Visual Assets:**
        11. Number of screenshots shown
        12. Does it have a promo video? (yes/no)
        13. Feature graphic present? (yes/no)

        **Additional Info:**
        14. Downloads range (e.g., "10M+")
        15. Content rating (e.g., "Everyone", "Teen")
        16. Size (e.g., "50MB")
        17. Price or "Free"
        18. In-app purchases range (if listed)

        Format as structured JSON with these fields.
        """

        return {
            "url": url,
            "prompt": prompt
        }


class ScraperGuide:
    """
    Guide for agents on how to use WebFetch for scraping.
    Includes best practices and error handling strategies.
    """

    @staticmethod
    def get_usage_instructions() -> str:
        """
        Get instructions for agents on using WebFetch tool.

        Returns:
            Markdown-formatted instructions
        """
        return """
# WebFetch Scraping Guide for ASO Agents

## Overview

WebFetch is a built-in Claude Code tool that fetches web pages and extracts information using AI. Use it when iTunes Search API doesn't provide sufficient data.

## Basic Usage Pattern

```python
from app_store_optimization.lib.scraper import WebFetchPrompts

# Get pre-configured prompt for App Store search
config = WebFetchPrompts.app_store_search("task manager")

# Then use WebFetch tool with:
# - url: config["url"]
# - prompt: config["prompt"]

# WebFetch will return extracted data as structured text/JSON
```

## Scraping Workflow

### 1. App Store Search Results

**When to use:** Finding top-ranking apps for a keyword

**Process:**
1. Get prompt config: `WebFetchPrompts.app_store_search("productivity")`
2. Use WebFetch tool with the URL and prompt
3. Parse returned data (will be list of apps)
4. Extract competitor names and URLs

**Example:**
```
config = WebFetchPrompts.app_store_search("productivity")
# Use WebFetch tool
# Results: List of 10 apps with names, ratings, URLs
```

### 2. Individual App Pages

**When to use:** Getting detailed metadata for a specific app

**Process:**
1. Get app URL from search results or user
2. Get prompt config: `WebFetchPrompts.app_store_app_page(url)`
3. Use WebFetch tool
4. Extract title, description, rating, etc.

**Example:**
```
config = WebFetchPrompts.app_store_app_page("https://apps.apple.com/us/app/todoist/...")
# Use WebFetch tool
# Results: Complete app metadata
```

### 3. Google Play Store

**Process:** Same as App Store but use play_store_* methods

## Best Practices

### 1. Respectful Delays
- Wait 2-3 seconds between requests
- Don't scrape more than 10 pages in rapid succession
- Use iTunes API when possible (it's faster and official)

### 2. Error Handling
```python
# If WebFetch fails:
try:
    # Attempt WebFetch
    pass
except Exception as e:
    # Fall back to:
    # 1. iTunes Search API (if Apple)
    # 2. Ask user for data manually
    # 3. Use category defaults
```

### 3. Data Validation
- Always validate extracted data
- Check for missing fields
- Confirm character counts seem reasonable
- Verify URLs are properly formatted

### 4. Rate Limiting
If you encounter rate limiting:
- Wait 60 seconds
- Reduce number of pages to scrape
- Use cached data if available
- Ask user to provide data manually

## Common Scraping Scenarios

### Scenario 1: Competitor Research
```
Goal: Analyze top 5 competitors

Steps:
1. WebFetch App Store search for category keyword
2. Extract top 5 app URLs
3. For each URL:
   - WebFetch individual app page
   - Extract metadata
   - Save to competitor_data list
4. Pass to competitor_analyzer.py
```

### Scenario 2: Keyword Rankings
```
Goal: Find where your app ranks for a keyword

Steps:
1. WebFetch App Store search for keyword
2. Extract list of apps shown
3. Find your app's position in list
4. If not in top 10, note "Not in top 10"
```

### Scenario 3: Review Scraping
```
Goal: Get recent user reviews

Notes:
- iTunes API provides reviews (use that first!)
- WebFetch can get first few visible reviews
- For bulk review analysis, use iTunes API endpoint
```

## Limitations

### What WebFetch CAN Do:
- Extract visible text and metadata
- Get ratings and review counts
- Identify visual elements (screenshots, video)
- Extract descriptions and "What's New" sections

### What WebFetch CANNOT Do:
- Access private app analytics
- Get historical data (only current state)
- Bypass paywalls or login requirements
- Get exact search volume numbers
- Access private reviews or analytics

## When to Use iTunes API Instead

Prefer iTunes Search API for:
- ✅ Competitor names → Use iTunes search
- ✅ Basic metadata (title, desc, rating) → Use iTunes API
- ✅ Bulk competitor comparison → Use iTunes API
- ✅ Speed (API is faster than scraping)

Use WebFetch only for:
- ⚠️ Data not in iTunes API
- ⚠️ Visual assessment (screenshots, layout)
- ⚠️ Keyword rankings on store pages
- ⚠️ "What's New" text (not always in API)

## Legal & Ethical Considerations

1. **robots.txt Compliance**
   - Respect robots.txt restrictions
   - App Store and Play Store allow reasonable scraping

2. **Terms of Service**
   - Scraping for competitive research is generally allowed
   - Don't use scraped data for spam or manipulation
   - Don't scrape at scale that burdens servers

3. **Data Privacy**
   - Only scrape public data
   - Don't scrape user-identifiable information
   - Respect copyright on descriptions/content

4. **Frequency Limits**
   - Max 10 pages per minute
   - Max 100 pages per hour
   - Use caching to avoid repeat requests

## Troubleshooting

### Issue: WebFetch timeout
**Solution:** URL may be slow, try again or use iTunes API

### Issue: Data extraction incomplete
**Solution:** Refine prompt to be more specific about required fields

### Issue: Different layout on mobile vs desktop
**Solution:** Add "mobile view" or "desktop view" to prompt

### Issue: Store page in wrong language
**Solution:** Add country code to URL (e.g., `/us/` for US English)

---

**Remember:** WebFetch is your fallback when iTunes API doesn't provide needed data. Always prefer the official API when possible for speed and reliability.
"""


def get_scraping_examples() -> Dict[str, str]:
    """
    Get example scraping scenarios for agents.

    Returns:
        Dictionary of scenario name to example code
    """
    return {
        "app_store_search": """
# Example: Scrape App Store search results for "productivity"
config = WebFetchPrompts.app_store_search("productivity")

# Agent would then use WebFetch tool:
# WebFetch(url=config["url"], prompt=config["prompt"])

# Expected output: List of 10 apps with metadata
""",

        "app_page_metadata": """
# Example: Scrape individual app page
app_url = "https://apps.apple.com/us/app/todoist-to-do-list-tasks/id572688855"
config = WebFetchPrompts.app_store_app_page(app_url)

# Agent would then use WebFetch tool:
# WebFetch(url=config["url"], prompt=config["prompt"])

# Expected output: Complete app metadata (title, description, rating, etc.)
""",

        "competitor_analysis": """
# Example: Scrape 3 competitors for comparison
competitors = ["Todoist", "Any.do", "Microsoft To Do"]

competitor_data = []
for name in competitors:
    # 1. Search for app
    search_config = WebFetchPrompts.app_store_search(name)
    # WebFetch to get app URL

    # 2. Get app details
    app_config = WebFetchPrompts.app_store_app_page(app_url)
    # WebFetch to get metadata

    # 3. Add to list
    competitor_data.append(metadata)

# Now pass to competitor_analyzer.py for analysis
"""
    }


def main():
    """Print usage guide and examples for agents."""
    print("=" * 80)
    print("WebFetch Scraper Utility for ASO Agents")
    print("=" * 80)

    print("\n📚 Usage Instructions:\n")
    print(ScraperGuide.get_usage_instructions())

    print("\n" + "=" * 80)
    print("Example Prompts")
    print("=" * 80)

    print("\n1. App Store Search:")
    config = WebFetchPrompts.app_store_search("productivity")
    print(f"   URL: {config['url']}")
    print(f"   Prompt: {config['prompt'][:100]}...")

    print("\n2. App Store App Page:")
    config = WebFetchPrompts.app_store_app_page("https://apps.apple.com/us/app/todoist/id572688855")
    print(f"   URL: {config['url']}")
    print(f"   Prompt: {config['prompt'][:100]}...")

    print("\n3. Play Store Search:")
    config = WebFetchPrompts.play_store_search("fitness")
    print(f"   URL: {config['url']}")
    print(f"   Prompt: {config['prompt'][:100]}...")

    print("\n" + "=" * 80)
    print("Code Examples")
    print("=" * 80)

    examples = get_scraping_examples()
    for scenario, code in examples.items():
        print(f"\n{scenario}:")
        print(code)


if __name__ == "__main__":
    main()
