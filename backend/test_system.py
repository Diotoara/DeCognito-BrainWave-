#!/usr/bin/env python3
"""
System test script for OSINT Platform
"""
import asyncio
import sys
import os
import logging
from pathlib import Path

# Add backend to path
sys.path.insert(0, str(Path(__file__).parent))

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

async def test_environment():
    """Test environment variables."""
    logger.info("=== Testing Environment Variables ===")
    
    required_vars = [
        'REDDIT_CLIENT_ID',
        'REDDIT_CLIENT_SECRET',
        'GITHUB_TOKEN',
        'GEMINI_API_KEY'
    ]
    
    missing_vars = []
    for var in required_vars:
        value = os.getenv(var)
        if value:
            logger.info(f"✓ {var}: {'*' * (len(value) - 4)}{value[-4:]}")
        else:
            logger.error(f"✗ {var}: Missing")
            missing_vars.append(var)
    
    if missing_vars:
        logger.error(f"Missing environment variables: {', '.join(missing_vars)}")
        return False
    
    return True

async def test_reddit_scraper():
    """Test Reddit scraper."""
    logger.info("=== Testing Reddit Scraper ===")
    
    try:
        from scrapers.reddit_scraper import RedditScraper
        scraper = RedditScraper()
        
        # Test connection
        connection_test = scraper.test_connection()
        if connection_test['status'] == 'success':
            logger.info("✓ Reddit connection successful")
        else:
            logger.warning(f"⚠️ Reddit connection issue: {connection_test['message']}")
        
        # Test scraping
        result = await scraper.scrape_user("test", limit=5)
        if 'error' not in result:
            logger.info(f"✓ Reddit scraping successful: {result.get('total_items', 0)} items")
            return True
        else:
            logger.error(f"✗ Reddit scraping failed: {result['error']}")
            return False
            
    except Exception as e:
        logger.error(f"✗ Reddit scraper test failed: {str(e)}")
        return False

async def test_sentiment_analyzer():
    """Test sentiment analyzer."""
    logger.info("=== Testing Sentiment Analyzer ===")
    
    try:
        from ai_models.sentiment_model import SentimentAnalyzer
        analyzer = SentimentAnalyzer()
        
        # Test single analysis
        result = await analyzer.analyze_single("This is a great day!")
        if 'error' not in result:
            logger.info(f"✓ Sentiment analysis successful: {result}")
            return True
        else:
            logger.error(f"✗ Sentiment analysis failed: {result['error']}")
            return False
            
    except Exception as e:
        logger.error(f"✗ Sentiment analyzer test failed: {str(e)}")
        return False

async def test_github_scraper():
    """Test GitHub scraper."""
    logger.info("=== Testing GitHub Scraper ===")
    
    try:
        from scrapers.github_scraper import GitHubScraper
        scraper = GitHubScraper()
        
        result = await scraper.scrape_user("octocat")
        if 'error' not in result:
            logger.info(f"✓ GitHub scraping successful")
            return True
        else:
            logger.error(f"✗ GitHub scraping failed: {result['error']}")
            return False
            
    except Exception as e:
        logger.error(f"✗ GitHub scraper test failed: {str(e)}")
        return False

async def main():
    """Run all tests."""
    logger.info("🧪 Starting OSINT Platform System Tests")
    
    tests = [
        ("Environment Variables", test_environment),
        ("Reddit Scraper", test_reddit_scraper),
        ("Sentiment Analyzer", test_sentiment_analyzer),
        ("GitHub Scraper", test_github_scraper),
    ]
    
    results = {}
    
    for test_name, test_func in tests:
        try:
            result = await test_func()
            results[test_name] = result
        except Exception as e:
            logger.error(f"Test {test_name} crashed: {str(e)}")
            results[test_name] = False
    
    # Summary
    logger.info("=== Test Results Summary ===")
    passed = 0
    total = len(results)
    
    for test_name, result in results.items():
        status = "✓ PASS" if result else "✗ FAIL"
        logger.info(f"{status}: {test_name}")
        if result:
            passed += 1
    
    logger.info(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        logger.info("🎉 All tests passed! System is ready.")
        return True
    else:
        logger.error("❌ Some tests failed. Check the logs above.")
        return False

if __name__ == "__main__":
    success = asyncio.run(main())
    sys.exit(0 if success else 1)
