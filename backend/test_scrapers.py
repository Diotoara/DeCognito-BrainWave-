import asyncio
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def test_scrapers():
    print("🧪 Testing OSINT Scrapers...")
    
    # Test Reddit
    try:
        from scrapers.reddit_scraper import RedditScraper
        reddit = RedditScraper()
        result = await reddit.scrape_user("test", limit=5)
        print(f"✓ Reddit: {'Success' if 'error' not in result else 'Failed - ' + result['error']}")
    except Exception as e:
        print(f"✗ Reddit: Failed to initialize - {str(e)}")
    
    # Test GitHub
    try:
        from scrapers.github_scraper import GitHubScraper
        github = GitHubScraper()
        result = await github.scrape_user("octocat")
        print(f"✓ GitHub: {'Success' if 'error' not in result else 'Failed - ' + result['error']}")
    except Exception as e:
        print(f"✗ GitHub: Failed to initialize - {str(e)}")
    
    # Test AI Models
    try:
        from ai_models.sentiment_model import SentimentAnalyzer
        sentiment = SentimentAnalyzer()
        result = await sentiment.analyze_single("This is a test message")
        print(f"✓ Sentiment AI: {'Success' if 'error' not in result else 'Failed - ' + result['error']}")
    except Exception as e:
        print(f"✗ Sentiment AI: Failed to initialize - {str(e)}")
    
    print("\n🚀 Test completed! Check the results above.")

if __name__ == "__main__":
    asyncio.run(test_scrapers())
