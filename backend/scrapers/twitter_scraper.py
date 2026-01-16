# import snscrape.modules.twitter as sntwitter
# import asyncio
# from typing import Dict, List
# from datetime import datetime
# import requests
# from bs4 import BeautifulSoup

# class TwitterScraper:
#     def __init__(self):
#         self.session = requests.Session()
#         self.session.headers.update({
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
#         })
    
#     async def scrape_user(self, username: str, limit: int = 100) -> Dict:
#         try:
#             tweets = []
            
#             # Method 1: snscrape (primary)
#             try:
#                 for i, tweet in enumerate(sntwitter.TwitterUserScraper(username).get_items()):
#                     if i >= limit:
#                         break
                    
#                     tweets.append({
#                         'id': tweet.id,
#                         'content': tweet.content,
#                         'date': tweet.date.isoformat() if tweet.date else None,
#                         'retweet_count': tweet.retweetCount,
#                         'like_count': tweet.likeCount,
#                         'reply_count': tweet.replyCount,
#                         'url': tweet.url
#                     })
#             except Exception as e:
#                 print(f"snscrape failed: {e}")
#                 # Fallback to web scraping
#                 tweets = await self._scrape_twitter_web(username, limit)
            
#             # Get profile info
#             profile_info = await self._get_profile_info(username)
            
#             return {
#                 'platform': 'twitter',
#                 'user_info': profile_info,
#                 'tweets': tweets,
#                 'scraped_at': datetime.now().isoformat()
#             }
            
#         except Exception as e:
#             return {
#                 'platform': 'twitter',
#                 'error': str(e),
#                 'scraped_at': datetime.now().isoformat()
#             }
    
#     async def _scrape_twitter_web(self, username: str, limit: int) -> List[Dict]:
#         """Fallback web scraping method"""
#         try:
#             # This is a simplified version - in production, you'd need more sophisticated scraping
#             url = f"https://nitter.net/{username}"
#             response = self.session.get(url)
#             soup = BeautifulSoup(response.content, 'html.parser')
            
#             tweets = []
#             tweet_elements = soup.find_all('div', class_='tweet-content')[:limit]
            
#             for element in tweet_elements:
#                 content = element.get_text(strip=True)
#                 if content:
#                     tweets.append({
#                         'content': content,
#                         'date': datetime.now().isoformat(),
#                         'source': 'web_scrape'
#                     })
            
#             return tweets
#         except Exception as e:
#             print(f"Web scraping failed: {e}")
#             return []
    
#     async def _get_profile_info(self, username: str) -> Dict:
#         """Get basic profile information"""
#         try:
#             # Try to get profile info from nitter or other sources
#             return {
#                 'username': username,
#                 'platform': 'twitter',
#                 'scraped_method': 'fallback'
#             }
#         except Exception as e:
#             return {'username': username, 'error': str(e)}


# new 
# import asyncio
# import aiohttp
# import requests
# from typing import Dict, List, Optional
# from datetime import datetime
# import json
# import time
# import random
# from bs4 import BeautifulSoup
# import re
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import TimeoutException, WebDriverException
# import logging

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# class TwitterScraper:
#     def __init__(self):
#         self.session = requests.Session()
#         self.session.headers.update({
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#             'Accept-Language': 'en-US,en;q=0.5',
#             'Accept-Encoding': 'gzip, deflate, br',
#             'Connection': 'keep-alive',
#             'Upgrade-Insecure-Requests': '1',
#         })
#         self.driver = None
    
#     def _setup_selenium_driver(self):
#         """Setup Selenium WebDriver with optimal settings"""
#         if self.driver is None:
#             chrome_options = Options()
#             chrome_options.add_argument('--headless')
#             chrome_options.add_argument('--no-sandbox')
#             chrome_options.add_argument('--disable-dev-shm-usage')
#             chrome_options.add_argument('--disable-gpu')
#             chrome_options.add_argument('--window-size=1920,1080')
#             chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
#             chrome_options.add_argument('--disable-blink-features=AutomationControlled')
#             chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#             chrome_options.add_experimental_option('useAutomationExtension', False)
            
#             try:
#                 self.driver = webdriver.Chrome(options=chrome_options)
#                 self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
#             except Exception as e:
#                 logger.error(f"Failed to setup Chrome driver: {e}")
#                 raise
    
#     def _close_driver(self):
#         """Close the Selenium driver"""
#         if self.driver:
#             self.driver.quit()
#             self.driver = None
    
#     async def scrape_user(self, username: str, limit: int = 100) -> Dict:
#         """Main scraping method with multiple fallback strategies"""
#         try:
#             tweets = []
            
#             # Method 1: Try Selenium scraping (most reliable for X.com)
#             try:
#                 logger.info(f"Attempting Selenium scraping for {username}")
#                 tweets = await self._scrape_with_selenium(username, limit)
#                 if tweets:
#                     logger.info(f"Successfully scraped {len(tweets)} tweets with Selenium")
#                 else:
#                     logger.warning("Selenium scraping returned no tweets")
#             except Exception as e:
#                 logger.error(f"Selenium scraping failed: {e}")
            
#             # Method 2: Try alternative scraping services
#             if not tweets:
#                 try:
#                     logger.info(f"Attempting alternative scraping for {username}")
#                     tweets = await self._scrape_nitter_instances(username, limit)
#                     if tweets:
#                         logger.info(f"Successfully scraped {len(tweets)} tweets with alternative method")
#                 except Exception as e:
#                     logger.error(f"Alternative scraping failed: {e}")
            
#             # Method 3: Try RSS/syndication feeds
#             if not tweets:
#                 try:
#                     logger.info(f"Attempting RSS feed scraping for {username}")
#                     tweets = await self._scrape_rss_feeds(username, limit)
#                     if tweets:
#                         logger.info(f"Successfully scraped {len(tweets)} tweets from RSS feeds")
#                 except Exception as e:
#                     logger.error(f"RSS feed scraping failed: {e}")
            
#             # Get profile info
#             profile_info = await self._get_profile_info(username)
            
#             return {
#                 'platform': 'twitter',
#                 'user_info': profile_info,
#                 'tweets': tweets,
#                 'total_tweets': len(tweets),
#                 'scraped_at': datetime.now().isoformat()
#             }
            
#         except Exception as e:
#             logger.error(f"All scraping methods failed: {e}")
#             return {
#                 'platform': 'twitter',
#                 'error': str(e),
#                 'scraped_at': datetime.now().isoformat()
#             }
#         finally:
#             self._close_driver()
    
#     async def _scrape_with_selenium(self, username: str, limit: int) -> List[Dict]:
#         """Scrape using Selenium WebDriver"""
#         self._setup_selenium_driver()
#         tweets = []
        
#         try:
#             url = f"https://x.com/{username}"
#             logger.info(f"Navigating to {url}")
            
#             self.driver.get(url)
            
#             # Wait for page to load
#             WebDriverWait(self.driver, 10).until(
#                 EC.presence_of_element_located((By.TAG_NAME, "article"))
#             )
            
#             # Scroll and collect tweets
#             last_height = self.driver.execute_script("return document.body.scrollHeight")
#             tweet_count = 0
            
#             while tweet_count < limit:
#                 # Find tweet elements
#                 tweet_elements = self.driver.find_elements(By.TAG_NAME, "article")
                
#                 for element in tweet_elements[tweet_count:]:
#                     if tweet_count >= limit:
#                         break
                    
#                     try:
#                         # Extract tweet content
#                         content = self._extract_tweet_content(element)
#                         if content:
#                             tweets.append({
#                                 'id': f"tweet_{tweet_count}",
#                                 'content': content,
#                                 'date': datetime.now().isoformat(),
#                                 'source': 'selenium_scrape',
#                                 'username': username
#                             })
#                             tweet_count += 1
#                     except Exception as e:
#                         logger.warning(f"Error extracting tweet: {e}")
#                         continue
                
#                 # Scroll down
#                 self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#                 time.sleep(random.uniform(2, 4))  # Random delay
                
#                 # Check if new content loaded
#                 new_height = self.driver.execute_script("return document.body.scrollHeight")
#                 if new_height == last_height:
#                     break
#                 last_height = new_height
            
#             return tweets
            
#         except TimeoutException:
#             logger.error("Timeout waiting for page to load")
#             return []
#         except WebDriverException as e:
#             logger.error(f"WebDriver error: {e}")
#             return []
#         except Exception as e:
#             logger.error(f"Unexpected error in Selenium scraping: {e}")
#             return []
    
#     def _extract_tweet_content(self, element) -> Optional[str]:
#         """Extract tweet content from a tweet element"""
#         try:
#             # Look for tweet text in various possible selectors
#             selectors = [
#                 '[data-testid="tweetText"]',
#                 '[data-testid="tweet-text"]',
#                 '.tweet-text',
#                 '.css-901oao.r-18jsvk2.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0',
#                 'div[lang]'
#             ]
            
#             for selector in selectors:
#                 try:
#                     text_element = element.find_element(By.CSS_SELECTOR, selector)
#                     if text_element and text_element.text:
#                         return text_element.text.strip()
#                 except:
#                     continue
            
#             # Fallback: get all text from the article element
#             text = element.text
#             if text:
#                 # Clean up the text (remove extra whitespace, etc.)
#                 lines = [line.strip() for line in text.split('\n') if line.strip()]
#                 # The tweet content is usually one of the longer lines
#                 for line in lines:
#                     if len(line) > 10 and not line.startswith('@') and not line.isdigit():
#                         return line
            
#             return None
#         except Exception as e:
#             logger.warning(f"Error extracting tweet content: {e}")
#             return None
    
#     async def _scrape_nitter_instances(self, username: str, limit: int) -> List[Dict]:
#         """Try scraping from Nitter instances"""
#         nitter_instances = [
#             "https://nitter.net",
#             "https://nitter.it",
#             "https://nitter.cc",
#             "https://nitter.unixfox.eu",
#             "https://nitter.domain.glass"
#         ]
        
#         for instance in nitter_instances:
#             try:
#                 logger.info(f"Trying Nitter instance: {instance}")
#                 url = f"{instance}/{username}"
                
#                 async with aiohttp.ClientSession() as session:
#                     async with session.get(url, timeout=10) as response:
#                         if response.status == 200:
#                             content = await response.text()
#                             soup = BeautifulSoup(content, 'html.parser')
                            
#                             tweets = []
#                             tweet_elements = soup.find_all('div', class_='tweet-content')[:limit]
                            
#                             for i, element in enumerate(tweet_elements):
#                                 text = element.get_text(strip=True)
#                                 if text:
#                                     tweets.append({
#                                         'id': f"nitter_{i}",
#                                         'content': text,
#                                         'date': datetime.now().isoformat(),
#                                         'source': f'nitter_{instance}',
#                                         'username': username
#                                     })
                            
#                             if tweets:
#                                 return tweets
                            
#             except Exception as e:
#                 logger.warning(f"Nitter instance {instance} failed: {e}")
#                 continue
        
#         return []
    
#     async def _scrape_rss_feeds(self, username: str, limit: int) -> List[Dict]:
#         """Try scraping from RSS feeds or syndication services"""
#         # This is a placeholder for RSS-based scraping
#         # You would implement RSS feed parsing here
#         try:
#             # Example: Some services provide RSS feeds for Twitter profiles
#             # This would require finding working RSS bridge services
#             logger.info(f"RSS feed scraping not implemented for {username}")
#             return []
#         except Exception as e:
#             logger.error(f"RSS feed scraping failed: {e}")
#             return []
    
#     async def _get_profile_info(self, username: str) -> Dict:
#         """Get basic profile information"""
#         try:
#             # Try to get profile info using various methods
#             profile_info = {
#                 'username': username,
#                 'platform': 'twitter/x',
#                 'scraped_method': 'fallback',
#                 'profile_url': f'https://x.com/{username}'
#             }
            
#             # If we have selenium driver, try to get more info
#             if self.driver:
#                 try:
#                     # Look for profile information
#                     display_name_element = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="UserName"]')
#                     if display_name_element:
#                         profile_info['display_name'] = display_name_element.text
                        
#                     bio_element = self.driver.find_element(By.CSS_SELECTOR, '[data-testid="UserDescription"]')
#                     if bio_element:
#                         profile_info['bio'] = bio_element.text
                        
#                 except Exception as e:
#                     logger.warning(f"Could not extract profile info: {e}")
            
#             return profile_info
            
#         except Exception as e:
#             return {
#                 'username': username, 
#                 'error': str(e),
#                 'platform': 'twitter/x'
#             }

# # Usage example
# async def main():
#     scraper = TwitterScraper()
    
#     # Test the scraper
#     username = "elonmusk"  # Replace with desired username
#     result = await scraper.scrape_user(username, limit=50)
    
#     print(f"Scraped {len(result.get('tweets', []))} tweets")
#     print(json.dumps(result, indent=2))

# if __name__ == "__main__":
#     asyncio.run(main())



# # new
# import asyncio
# import aiohttp
# import requests
# from typing import Dict, List, Optional
# from datetime import datetime
# import json
# import time
# import random
# from bs4 import BeautifulSoup
# import re
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import TimeoutException, WebDriverException
# import logging
# import os

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# class TwitterScraper:
#     def __init__(self, bearer_token: str = None):
#         self.bearer_token = bearer_token or os.getenv('TWITTER_BEARER_TOKEN')
#         self.session = requests.Session()
#         self.session.headers.update({
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
#             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#             'Accept-Language': 'en-US,en;q=0.5',
#             'Accept-Encoding': 'gzip, deflate, br',
#             'Connection': 'keep-alive',
#             'Upgrade-Insecure-Requests': '1',
#         })
#         self.driver = None
        
#         # Setup API headers if bearer token is available
#         if self.bearer_token:
#             self.api_headers = {
#                 'Authorization': f'Bearer {self.bearer_token}',
#                 'Content-Type': 'application/json',
#                 'User-Agent': 'TwitterScraper/1.0'
#             }
#             logger.info("✓ Twitter API Bearer token configured")
#         else:
#             logger.warning("⚠ No Twitter Bearer token provided, API methods will be skipped")
    
#     def _setup_selenium_driver(self):
#         """Setup Selenium WebDriver with optimal settings"""
#         if self.driver is None:
#             chrome_options = Options()
#             chrome_options.add_argument('--headless')
#             chrome_options.add_argument('--no-sandbox')
#             chrome_options.add_argument('--disable-dev-shm-usage')
#             chrome_options.add_argument('--disable-gpu')
#             chrome_options.add_argument('--window-size=1920,1080')
#             chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
#             chrome_options.add_argument('--disable-blink-features=AutomationControlled')
#             chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
#             chrome_options.add_experimental_option('useAutomationExtension', False)
#             chrome_options.add_argument('--disable-web-security')
#             chrome_options.add_argument('--disable-features=VizDisplayCompositor')
#             chrome_options.add_argument('--disable-extensions')
#             chrome_options.add_argument('--disable-plugins')
#             chrome_options.add_argument('--disable-images')
#             chrome_options.add_argument('--disable-javascript')
            
#             try:
#                 self.driver = webdriver.Chrome(options=chrome_options)
#                 self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
#                 self.driver.set_page_load_timeout(30)
#                 logger.info("✓ Selenium WebDriver initialized")
#             except Exception as e:
#                 logger.error(f"Failed to setup Chrome driver: {e}")
#                 raise
    
#     def _close_driver(self):
#         """Close the Selenium driver"""
#         if self.driver:
#             self.driver.quit()
#             self.driver = None
    
#     async def scrape_user(self, username: str, limit: int = 100) -> Dict:
#         """Main scraping method with multiple fallback strategies"""
#         try:
#             tweets = []
#             profile_info = {}
            
#             # Method 1: Try Twitter API v2 (most reliable)
#             if self.bearer_token:
#                 try:
#                     logger.info(f"Attempting Twitter API v2 scraping for {username}")
#                     api_result = await self._scrape_with_api_v2(username, limit)
#                     if api_result['tweets']:
#                         tweets = api_result['tweets']
#                         profile_info = api_result.get('profile_info', {})
#                         logger.info(f"✓ Successfully scraped {len(tweets)} tweets with API v2")
#                 except Exception as e:
#                     logger.error(f"Twitter API v2 scraping failed: {e}")
            
#             # Method 2: Try Selenium scraping
#             if not tweets:
#                 try:
#                     logger.info(f"Attempting Selenium scraping for {username}")
#                     tweets = await self._scrape_with_selenium(username, limit)
#                     if tweets:
#                         logger.info(f"✓ Successfully scraped {len(tweets)} tweets with Selenium")
#                     else:
#                         logger.warning("Selenium scraping returned no tweets")
#                 except Exception as e:
#                     logger.error(f"Selenium scraping failed: {e}")
            
#             # Method 3: Try alternative scraping services
#             if not tweets:
#                 try:
#                     logger.info(f"Attempting alternative scraping for {username}")
#                     tweets = await self._scrape_nitter_instances(username, limit)
#                     if tweets:
#                         logger.info(f"✓ Successfully scraped {len(tweets)} tweets with alternative method")
#                 except Exception as e:
#                     logger.error(f"Alternative scraping failed: {e}")
            
#             # Method 4: Try RSS/syndication feeds
#             if not tweets:
#                 try:
#                     logger.info(f"Attempting RSS feed scraping for {username}")
#                     tweets = await self._scrape_rss_feeds(username, limit)
#                     if tweets:
#                         logger.info(f"✓ Successfully scraped {len(tweets)} tweets from RSS feeds")
#                 except Exception as e:
#                     logger.error(f"RSS feed scraping failed: {e}")
            
#             # Get profile info if not already obtained
#             if not profile_info:
#                 profile_info = await self._get_profile_info(username)
            
#             return {
#                 'platform': 'twitter',
#                 'user_info': profile_info,
#                 'tweets': tweets,
#                 'total_tweets': len(tweets),
#                 'scraped_at': datetime.now().isoformat(),
#                 'success': len(tweets) > 0
#             }
            
#         except Exception as e:
#             logger.error(f"All scraping methods failed: {e}")
#             return {
#                 'platform': 'twitter',
#                 'error': str(e),
#                 'scraped_at': datetime.now().isoformat(),
#                 'success': False
#             }
#         finally:
#             self._close_driver()
    
#     async def _scrape_with_api_v2(self, username: str, limit: int) -> Dict:
#         """Scrape using Twitter API v2"""
#         try:
#             # First, get user ID from username
#             user_lookup_url = f"https://api.twitter.com/2/users/by/username/{username}"
#             user_params = {
#                 'user.fields': 'description,public_metrics,created_at,verified,location,url'
#             }
            
#             async with aiohttp.ClientSession() as session:
#                 async with session.get(user_lookup_url, headers=self.api_headers, params=user_params) as response:
#                     if response.status != 200:
#                         error_text = await response.text()
#                         logger.error(f"User lookup failed: {response.status} - {error_text}")
#                         return {'tweets': [], 'profile_info': {}}
                    
#                     user_data = await response.json()
#                     if 'data' not in user_data:
#                         logger.error(f"User not found: {username}")
#                         return {'tweets': [], 'profile_info': {}}
                    
#                     user_info = user_data['data']
#                     user_id = user_info['id']
                    
#                     # Get user's tweets
#                     tweets_url = f"https://api.twitter.com/2/users/{user_id}/tweets"
#                     tweets_params = {
#                         'max_results': min(limit, 100),  # API limit is 100 per request
#                         'tweet.fields': 'created_at,public_metrics,context_annotations,lang,reply_settings',
#                         'exclude': 'retweets,replies'
#                     }
                    
#                     async with session.get(tweets_url, headers=self.api_headers, params=tweets_params) as tweets_response:
#                         if tweets_response.status != 200:
#                             error_text = await tweets_response.text()
#                             logger.error(f"Tweets fetch failed: {tweets_response.status} - {error_text}")
#                             return {'tweets': [], 'profile_info': self._format_profile_info(user_info, username)}
                        
#                         tweets_data = await tweets_response.json()
#                         tweets = []
                        
#                         if 'data' in tweets_data:
#                             for tweet in tweets_data['data']:
#                                 tweets.append({
#                                     'id': tweet['id'],
#                                     'content': tweet['text'],
#                                     'date': tweet['created_at'],
#                                     'source': 'twitter_api_v2',
#                                     'username': username,
#                                     'metrics': tweet.get('public_metrics', {}),
#                                     'lang': tweet.get('lang', 'en')
#                                 })
                        
#                         return {
#                             'tweets': tweets,
#                             'profile_info': self._format_profile_info(user_info, username)
#                         }
                        
#         except Exception as e:
#             logger.error(f"API v2 scraping error: {e}")
#             return {'tweets': [], 'profile_info': {}}
    
#     def _format_profile_info(self, user_info: Dict, username: str) -> Dict:
#         """Format profile information from API response"""
#         return {
#             'username': username,
#             'display_name': user_info.get('name', ''),
#             'bio': user_info.get('description', ''),
#             'followers_count': user_info.get('public_metrics', {}).get('followers_count', 0),
#             'following_count': user_info.get('public_metrics', {}).get('following_count', 0),
#             'tweet_count': user_info.get('public_metrics', {}).get('tweet_count', 0),
#             'verified': user_info.get('verified', False),
#             'location': user_info.get('location', ''),
#             'url': user_info.get('url', ''),
#             'created_at': user_info.get('created_at', ''),
#             'platform': 'twitter/x',
#             'profile_url': f'https://x.com/{username}'
#         }
    
#     async def _scrape_with_selenium(self, username: str, limit: int) -> List[Dict]:
#         """Scrape using Selenium WebDriver with improved error handling"""
#         self._setup_selenium_driver()
#         tweets = []
        
#         try:
#             url = f"https://x.com/{username}"
#             logger.info(f"Navigating to {url}")
            
#             self.driver.get(url)
            
#             # Wait for page to load with multiple possible selectors
#             selectors_to_wait = [
#                 "article",
#                 '[data-testid="tweet"]',
#                 '[data-testid="tweetText"]',
#                 '.css-1dbjc4n'
#             ]
            
#             element_found = False
#             for selector in selectors_to_wait:
#                 try:
#                     WebDriverWait(self.driver, 15).until(
#                         EC.presence_of_element_located((By.CSS_SELECTOR, selector))
#                     )
#                     element_found = True
#                     break
#                 except TimeoutException:
#                     continue
            
#             if not element_found:
#                 logger.error("Could not find any tweet elements on page")
#                 return []
            
#             # Scroll and collect tweets
#             last_height = self.driver.execute_script("return document.body.scrollHeight")
#             tweet_count = 0
#             scroll_attempts = 0
#             max_scroll_attempts = 10
            
#             while tweet_count < limit and scroll_attempts < max_scroll_attempts:
#                 # Find tweet elements with multiple selectors
#                 tweet_elements = []
#                 for selector in ["article", '[data-testid="tweet"]', '.tweet']:
#                     try:
#                         elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
#                         if elements:
#                             tweet_elements = elements
#                             break
#                     except:
#                         continue
                
#                 if not tweet_elements:
#                     logger.warning("No tweet elements found")
#                     break
                
#                 # Extract content from new tweets
#                 current_tweets = len(tweets)
#                 for element in tweet_elements:
#                     if tweet_count >= limit:
#                         break
                    
#                     try:
#                         content = self._extract_tweet_content(element)
#                         if content and content not in [t['content'] for t in tweets]:
#                             tweets.append({
#                                 'id': f"tweet_{tweet_count}",
#                                 'content': content,
#                                 'date': datetime.now().isoformat(),
#                                 'source': 'selenium_scrape',
#                                 'username': username
#                             })
#                             tweet_count += 1
#                     except Exception as e:
#                         logger.warning(f"Error extracting tweet: {e}")
#                         continue
                
#                 # If no new tweets were found, scroll down
#                 if len(tweets) == current_tweets:
#                     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#                     time.sleep(random.uniform(3, 5))
                    
#                     # Check if new content loaded
#                     new_height = self.driver.execute_script("return document.body.scrollHeight")
#                     if new_height == last_height:
#                         scroll_attempts += 1
#                     else:
#                         scroll_attempts = 0
#                     last_height = new_height
            
#             return tweets
            
#         except TimeoutException:
#             logger.error("Timeout waiting for page to load")
#             return []
#         except WebDriverException as e:
#             logger.error(f"WebDriver error: {e}")
#             return []
#         except Exception as e:
#             logger.error(f"Unexpected error in Selenium scraping: {e}")
#             return []
    
#     def _extract_tweet_content(self, element) -> Optional[str]:
#         """Extract tweet content from a tweet element with improved selectors"""
#         try:
#             # Enhanced list of selectors to find tweet text
#             selectors = [
#                 '[data-testid="tweetText"]',
#                 '[data-testid="tweet-text"]',
#                 '.tweet-text',
#                 '.css-901oao.r-18jsvk2.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0',
#                 'div[lang]',
#                 '.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0',
#                 'span.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0'
#             ]
            
#             for selector in selectors:
#                 try:
#                     text_elements = element.find_elements(By.CSS_SELECTOR, selector)
#                     for text_element in text_elements:
#                         if text_element and text_element.text:
#                             text = text_element.text.strip()
#                             if len(text) > 5:  # Avoid short/empty strings
#                                 return text
#                 except:
#                     continue
            
#             # Fallback: get all text from the article element and extract meaningful content
#             text = element.text
#             if text:
#                 lines = [line.strip() for line in text.split('\n') if line.strip()]
#                 # Look for the main tweet content (usually longer lines that aren't metadata)
#                 for line in lines:
#                     if (len(line) > 20 and 
#                         not line.startswith('@') and 
#                         not line.isdigit() and 
#                         not line.startswith('Show this thread') and
#                         not line.startswith('Replying to') and
#                         not re.match(r'^\d+[hms]$', line)):  # Avoid timestamps
#                         return line
            
#             return None
#         except Exception as e:
#             logger.warning(f"Error extracting tweet content: {e}")
#             return None
    
#     async def _scrape_nitter_instances(self, username: str, limit: int) -> List[Dict]:
#         """Try scraping from Nitter instances with better error handling"""
#         nitter_instances = [
#             "https://nitter.net",
#             "https://nitter.it",
#             "https://nitter.cc",
#             "https://nitter.unixfox.eu",
#             "https://nitter.domain.glass",
#             "https://nitter.snopyta.org",
#             "https://nitter.fdn.fr"
#         ]
        
#         for instance in nitter_instances:
#             try:
#                 logger.info(f"Trying Nitter instance: {instance}")
#                 url = f"{instance}/{username}"
                
#                 timeout = aiohttp.ClientTimeout(total=15)
#                 async with aiohttp.ClientSession(timeout=timeout) as session:
#                     async with session.get(url, headers=self.session.headers) as response:
#                         if response.status == 200:
#                             content = await response.text()
#                             soup = BeautifulSoup(content, 'html.parser')
                            
#                             tweets = []
#                             # Try different selectors for Nitter
#                             selectors = [
#                                 '.tweet-content',
#                                 '.tweet-text',
#                                 '.tweet-body',
#                                 '.tweet .tweet-content p'
#                             ]
                            
#                             for selector in selectors:
#                                 tweet_elements = soup.select(selector)[:limit]
#                                 if tweet_elements:
#                                     break
                            
#                             for i, element in enumerate(tweet_elements):
#                                 text = element.get_text(strip=True)
#                                 if text and len(text) > 10:
#                                     tweets.append({
#                                         'id': f"nitter_{i}",
#                                         'content': text,
#                                         'date': datetime.now().isoformat(),
#                                         'source': f'nitter_{instance.split("//")[1]}',
#                                         'username': username
#                                     })
                            
#                             if tweets:
#                                 logger.info(f"✓ Found {len(tweets)} tweets from {instance}")
#                                 return tweets
#                         else:
#                             logger.warning(f"Nitter instance {instance} returned status {response.status}")
                            
#             except asyncio.TimeoutError:
#                 logger.warning(f"Nitter instance {instance} timed out")
#                 continue
#             except Exception as e:
#                 logger.warning(f"Nitter instance {instance} failed: {e}")
#                 continue
        
#         return []
    
#     async def _scrape_rss_feeds(self, username: str, limit: int) -> List[Dict]:
#         """Try scraping from RSS feeds or syndication services"""
#         try:
#             # Try RSS Bridge if available
#             rss_bridge_services = [
#                 f"https://rss-bridge.snopyta.org/?action=display&bridge=Twitter&username={username}&format=Json",
#                 f"https://wtf.roflcopter.fr/rss-bridge/?action=display&bridge=Twitter&username={username}&format=Json"
#             ]
            
#             for service_url in rss_bridge_services:
#                 try:
#                     async with aiohttp.ClientSession() as session:
#                         async with session.get(service_url, timeout=10) as response:
#                             if response.status == 200:
#                                 data = await response.json()
#                                 tweets = []
                                
#                                 for i, item in enumerate(data.get('items', [])[:limit]):
#                                     content = item.get('content_text', item.get('title', ''))
#                                     if content:
#                                         tweets.append({
#                                             'id': f"rss_{i}",
#                                             'content': content,
#                                             'date': item.get('date_published', datetime.now().isoformat()),
#                                             'source': 'rss_bridge',
#                                             'username': username
#                                         })
                                
#                                 if tweets:
#                                     return tweets
#                 except Exception as e:
#                     logger.warning(f"RSS Bridge service failed: {e}")
#                     continue
            
#             logger.info(f"No working RSS feed found for {username}")
#             return []
#         except Exception as e:
#             logger.error(f"RSS feed scraping failed: {e}")
#             return []
    
#     async def _get_profile_info(self, username: str) -> Dict:
#         """Get basic profile information with multiple fallback methods"""
#         try:
#             profile_info = {
#                 'username': username,
#                 'platform': 'twitter/x',
#                 'profile_url': f'https://x.com/{username}',
#                 'scraped_method': 'fallback'
#             }
            
#             # Try to get profile info using Selenium if available
#             if self.driver:
#                 try:
#                     # Extended list of selectors for profile information
#                     selectors = {
#                         'display_name': [
#                             '[data-testid="UserName"]',
#                             'h1[role="heading"]',
#                             '.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1wbh5a2 h1'
#                         ],
#                         'bio': [
#                             '[data-testid="UserDescription"]',
#                             '.css-901oao.r-18jsvk2.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0',
#                             '.profile-description'
#                         ],
#                         'followers': [
#                             '[data-testid="UserFollowers"]',
#                             'a[href$="/followers"]',
#                             '.profile-stat[data-nav="followers"]'
#                         ]
#                     }
                    
#                     for field, field_selectors in selectors.items():
#                         for selector in field_selectors:
#                             try:
#                                 element = self.driver.find_element(By.CSS_SELECTOR, selector)
#                                 if element and element.text:
#                                     profile_info[field] = element.text.strip()
#                                     break
#                             except:
#                                 continue
                        
#                 except Exception as e:
#                     logger.warning(f"Could not extract profile info: {e}")
            
#             return profile_info
            
#         except Exception as e:
#             return {
#                 'username': username, 
#                 'error': str(e),
#                 'platform': 'twitter/x'
#             }

# # Usage example
# async def main():
#     # Use the provided bearer token
#     bearer_token = "AAAAAAAAAAAAAAAAAAAAAOwp3AEAAAAAvicR4BjNfAmLGttFdGU4qEBFsb4%3DSMQtKgAit99ZAx66GsG850XStmFbE9BwNifmqsyXRQ7N9CFCq2"
    
#     scraper = TwitterScraper(bearer_token=bearer_token)
    
#     # Test the scraper
#     username = "elonmusk"
#     result = await scraper.scrape_user(username, limit=50)
    
#     print(f"Scraping result for @{username}:")
#     print(f"Success: {result.get('success', False)}")
#     print(f"Tweets found: {len(result.get('tweets', []))}")
#     print(f"Profile info: {result.get('user_info', {})}")
    
#     # Print first few tweets
#     for i, tweet in enumerate(result.get('tweets', [])[:3]):
#         print(f"\nTweet {i+1}:")
#         print(f"Content: {tweet['content'][:100]}...")
#         print(f"Source: {tweet['source']}")
#         print(f"Date: {tweet['date']}")

# if __name__ == "__main__":
#     asyncio.run(main())

# !above best working 

import asyncio
import aiohttp
import requests
from typing import Dict, List, Optional
from datetime import datetime
import json
import time
import random
from bs4 import BeautifulSoup
import re
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import TimeoutException, WebDriverException
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TwitterScraper:
    def __init__(self, bearer_token: str = None):
        self.bearer_token = bearer_token or os.getenv('TWITTER_BEARER_TOKEN')
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
        })
        self.driver = None
        
        # Setup API headers if bearer token is available
        if self.bearer_token:
            self.api_headers = {
                'Authorization': f'Bearer {self.bearer_token}',
                'Content-Type': 'application/json',
                'User-Agent': 'TwitterScraper/1.0'
            }
            logger.info("✓ Twitter API Bearer token configured")
        else:
            logger.warning("⚠ No Twitter Bearer token provided, API methods will be skipped")
        
    def _setup_selenium_driver(self):
        """Setup Selenium WebDriver with optimal settings"""
        if self.driver is None:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--window-size=1920,1080')
            chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')
            chrome_options.add_argument('--disable-blink-features=AutomationControlled')
            chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
            chrome_options.add_experimental_option('useAutomationExtension', False)
            chrome_options.add_argument('--disable-web-security')
            chrome_options.add_argument('--disable-features=VizDisplayCompositor')
            chrome_options.add_argument('--disable-extensions')
            chrome_options.add_argument('--disable-plugins')
            chrome_options.add_argument('--disable-images')
            chrome_options.add_argument('--disable-javascript')
            
            try:
                self.driver = webdriver.Chrome(options=chrome_options)
                self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
                self.driver.set_page_load_timeout(30)
                logger.info("✓ Selenium WebDriver initialized")
            except Exception as e:
                logger.error(f"Failed to setup Chrome driver: {e}")
                raise

    def _close_driver(self):
        """Close the Selenium driver"""
        if self.driver:
            self.driver.quit()
            self.driver = None

    async def scrape_user(self, username: str, limit: int = 100) -> Dict:
        """Main scraping method with multiple fallback strategies"""
        try:
            tweets = []
            profile_info = {}
            
            # Method 1: Try Twitter API v2 (most reliable)
            if self.bearer_token:
                try:
                    logger.info(f"Attempting Twitter API v2 scraping for {username}")
                    api_result = await self._scrape_with_api_v2(username, limit)
                    if api_result['tweets']:
                        tweets = api_result['tweets']
                        profile_info = api_result.get('profile_info', {})
                        logger.info(f"✓ Successfully scraped {len(tweets)} tweets with API v2")
                except Exception as e:
                    logger.error(f"Twitter API v2 scraping failed: {e}")
            
            # Method 2: Try Selenium scraping
            if not tweets:
                try:
                    logger.info(f"Attempting Selenium scraping for {username}")
                    tweets = await self._scrape_with_selenium(username, limit)
                    if tweets:
                        logger.info(f"✓ Successfully scraped {len(tweets)} tweets with Selenium")
                    else:
                        logger.warning("Selenium scraping returned no tweets")
                except Exception as e:
                    logger.error(f"Selenium scraping failed: {e}")
            
            # Method 3: Try alternative scraping services
            if not tweets:
                try:
                    logger.info(f"Attempting alternative scraping for {username}")
                    tweets = await self._scrape_nitter_instances(username, limit)
                    if tweets:
                        logger.info(f"✓ Successfully scraped {len(tweets)} tweets with alternative method")
                except Exception as e:
                    logger.error(f"Alternative scraping failed: {e}")
            
            # Method 4: Try RSS/syndication feeds
            if not tweets:
                try:
                    logger.info(f"Attempting RSS feed scraping for {username}")
                    tweets = await self._scrape_rss_feeds(username, limit)
                    if tweets:
                        logger.info(f"✓ Successfully scraped {len(tweets)} tweets from RSS feeds")
                except Exception as e:
                    logger.error(f"RSS feed scraping failed: {e}")
            
            # Get profile info if not already obtained
            if not profile_info:
                profile_info = await self._get_profile_info(username)
            
            return {
                'platform': 'twitter',
                'user_info': profile_info,
                'tweets': tweets,
                'total_tweets': len(tweets),
                'scraped_at': datetime.now().isoformat(),
                'success': len(tweets) > 0
            }
            
        except Exception as e:
            logger.error(f"All scraping methods failed: {e}")
            return {
                'platform': 'twitter',
                'error': str(e),
                'scraped_at': datetime.now().isoformat(),
                'success': False
            }
        finally:
            self._close_driver()

    async def _scrape_with_api_v2(self, username: str, limit: int) -> Dict:
        """Scrape using Twitter API v2"""
        try:
            # First, get user ID from username
            user_lookup_url = f"https://api.twitter.com/2/users/by/username/{username}"
            user_params = {
                'user.fields': 'description,public_metrics,created_at,verified,location,url'
            }
            
            async with aiohttp.ClientSession() as session:
                async with session.get(user_lookup_url, headers=self.api_headers, params=user_params) as response:
                    if response.status != 200:
                        error_text = await response.text()
                        logger.error(f"User lookup failed: {response.status} - {error_text}")
                        return {'tweets': [], 'profile_info': {}}
                    
                    user_data = await response.json()
                    if 'data' not in user_data:
                        logger.error(f"User not found: {username}")
                        return {'tweets': [], 'profile_info': {}}
                    
                    user_info = user_data['data']
                    user_id = user_info['id']
                    
                    # Get user's tweets
                    tweets_url = f"https://api.twitter.com/2/users/{user_id}/tweets"
                    tweets_params = {
                        'max_results': min(limit, 100),  # API limit is 100 per request
                        'tweet.fields': 'created_at,public_metrics,context_annotations,lang,reply_settings',
                        'exclude': 'retweets,replies'
                    }
                    
                    async with session.get(tweets_url, headers=self.api_headers, params=tweets_params) as tweets_response:
                        if tweets_response.status != 200:
                            error_text = await tweets_response.text()
                            logger.error(f"Tweets fetch failed: {tweets_response.status} - {error_text}")
                            return {'tweets': [], 'profile_info': self._format_profile_info(user_info, username)}
                        
                        tweets_data = await tweets_response.json()
                        tweets = []
                        
                        if 'data' in tweets_data:
                            for tweet in tweets_data['data']:
                                tweets.append({
                                    'id': tweet['id'],
                                    'content': tweet['text'],
                                    'date': tweet['created_at'],
                                    'source': 'twitter_api_v2',
                                    'username': username,
                                    'metrics': tweet.get('public_metrics', {}),
                                    'lang': tweet.get('lang', 'en')
                                })
                        
                        return {
                            'tweets': tweets,
                            'profile_info': self._format_profile_info(user_info, username)
                        }
                        
        except Exception as e:
            logger.error(f"API v2 scraping error: {e}")
            return {'tweets': [], 'profile_info': {}}

    def _format_profile_info(self, user_info: Dict, username: str) -> Dict:
        """Format profile information from API response"""
        return {
            'username': username,
            'display_name': user_info.get('name', ''),
            'bio': user_info.get('description', ''),
            'followers_count': user_info.get('public_metrics', {}).get('followers_count', 0),
            'following_count': user_info.get('public_metrics', {}).get('following_count', 0),
            'tweet_count': user_info.get('public_metrics', {}).get('tweet_count', 0),
            'verified': user_info.get('verified', False),
            'location': user_info.get('location', ''),
            'url': user_info.get('url', ''),
            'created_at': user_info.get('created_at', ''),
            'platform': 'twitter/x',
            'profile_url': f'https://x.com/{username}'
        }

    async def _scrape_with_selenium(self, username: str, limit: int) -> List[Dict]:
        """Scrape using Selenium WebDriver with improved error handling"""
        self._setup_selenium_driver()
        tweets = []
        
        try:
            url = f"https://x.com/{username}"
            logger.info(f"Navigating to {url}")
            
            self.driver.get(url)
            
            # Wait for page to load with multiple possible selectors
            selectors_to_wait = [
                "article",
                '[data-testid="tweet"]',
                '[data-testid="tweetText"]',
                '.css-1dbjc4n'
            ]
            
            element_found = False
            for selector in selectors_to_wait:
                try:
                    WebDriverWait(self.driver, 15).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, selector))
                    )
                    element_found = True
                    break
                except TimeoutException:
                    continue
            
            if not element_found:
                logger.error("Could not find any tweet elements on page")
                return []
            
            # Scroll and collect tweets
            last_height = self.driver.execute_script("return document.body.scrollHeight")
            tweet_count = 0
            scroll_attempts = 0
            max_scroll_attempts = 10
            
            while tweet_count < limit and scroll_attempts < max_scroll_attempts:
                # Find tweet elements with multiple selectors
                tweet_elements = []
                for selector in ["article", '[data-testid="tweet"]', '.tweet']:
                    try:
                        elements = self.driver.find_elements(By.CSS_SELECTOR, selector)
                        if elements:
                            tweet_elements = elements
                            break
                    except:
                        continue
                
                if not tweet_elements:
                    logger.warning("No tweet elements found")
                    break
                
                # Extract content from new tweets
                current_tweets = len(tweets)
                for element in tweet_elements:
                    if tweet_count >= limit:
                        break
                    
                    try:
                        content = self._extract_tweet_content(element)
                        if content and content not in [t['content'] for t in tweets]:
                            tweets.append({
                                'id': f"tweet_{tweet_count}",
                                'content': content,
                                'date': datetime.now().isoformat(),
                                'source': 'selenium_scrape',
                                'username': username
                            })
                            tweet_count += 1
                    except Exception as e:
                        logger.warning(f"Error extracting tweet: {e}")
                        continue
                
                # If no new tweets were found, scroll down
                if len(tweets) == current_tweets:
                    self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                    time.sleep(random.uniform(3, 5))
                    
                    # Check if new content loaded
                    new_height = self.driver.execute_script("return document.body.scrollHeight")
                    if new_height == last_height:
                        scroll_attempts += 1
                    else:
                        scroll_attempts = 0
                    last_height = new_height
            
            return tweets
            
        except TimeoutException:
            logger.error("Timeout waiting for page to load")
            return []
        except WebDriverException as e:
            logger.error(f"WebDriver error: {e}")
            return []
        except Exception as e:
            logger.error(f"Unexpected error in Selenium scraping: {e}")
            return []

    def _extract_tweet_content(self, element) -> Optional[str]:
        """Extract tweet content from a tweet element with improved selectors"""
        try:
            # Enhanced list of selectors to find tweet text
            selectors = [
                '[data-testid="tweetText"]',
                '[data-testid="tweet-text"]',
                '.tweet-text',
                '.css-901oao.r-18jsvk2.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0',
                'div[lang]',
                '.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0',
                'span.css-901oao.css-16my406.r-poiln3.r-bcqeeo.r-qvutc0'
            ]
            
            for selector in selectors:
                try:
                    text_elements = element.find_elements(By.CSS_SELECTOR, selector)
                    for text_element in text_elements:
                        if text_element and text_element.text:
                            text = text_element.text.strip()
                            if len(text) > 5:  # Avoid short/empty strings
                                return text
                except:
                    continue
            
            # Fallback: get all text from the article element and extract meaningful content
            text = element.text
            if text:
                lines = [line.strip() for line in text.split('\n') if line.strip()]
                # Look for the main tweet content (usually longer lines that aren't metadata)
                for line in lines:
                    if (len(line) > 20 and
                        not line.startswith('@') and
                        not line.isdigit() and
                        not line.startswith('Show this thread') and
                        not line.startswith('Replying to') and
                        not re.match(r'^\d+[hms]$', line)):  # Avoid timestamps
                        return line
            
            return None
        except Exception as e:
            logger.warning(f"Error extracting tweet content: {e}")
            return None

    async def _scrape_nitter_instances(self, username: str, limit: int) -> List[Dict]:
        """Try scraping from Nitter instances with better error handling"""
        nitter_instances = [
            "https://nitter.net",
            "https://nitter.it",
            "https://nitter.cc",
            "https://nitter.unixfox.eu",
            "https://nitter.domain.glass",
            "https://nitter.snopyta.org",
            "https://nitter.fdn.fr"
        ]
        
        for instance in nitter_instances:
            try:
                logger.info(f"Trying Nitter instance: {instance}")
                url = f"{instance}/{username}"
                
                timeout = aiohttp.ClientTimeout(total=15)
                async with aiohttp.ClientSession(timeout=timeout) as session:
                    async with session.get(url, headers=self.session.headers) as response:
                        if response.status == 200:
                            content = await response.text()
                            soup = BeautifulSoup(content, 'html.parser')
                            
                            tweets = []
                            # Try different selectors for Nitter
                            selectors = [
                                '.tweet-content',
                                '.tweet-text',
                                '.tweet-body',
                                '.tweet .tweet-content p'
                            ]
                            
                            for selector in selectors:
                                tweet_elements = soup.select(selector)[:limit]
                                if tweet_elements:
                                    break
                            
                            for i, element in enumerate(tweet_elements):
                                text = element.get_text(strip=True)
                                if text and len(text) > 10:
                                    tweets.append({
                                        'id': f"nitter_{i}",
                                        'content': text,
                                        'date': datetime.now().isoformat(),
                                        'source': f'nitter_{instance.split("//")[1]}',
                                        'username': username
                                    })
                            
                            if tweets:
                                logger.info(f"✓ Found {len(tweets)} tweets from {instance}")
                                return tweets
                        else:
                            logger.warning(f"Nitter instance {instance} returned status {response.status}")
                            
            except asyncio.TimeoutError:
                logger.warning(f"Nitter instance {instance} timed out")
                continue
            except Exception as e:
                logger.warning(f"Nitter instance {instance} failed: {e}")
                continue
        
        return []

    async def _scrape_rss_feeds(self, username: str, limit: int) -> List[Dict]:
        """Try scraping from RSS feeds or syndication services"""
        try:
            # Try RSS Bridge if available
            rss_bridge_services = [
                f"https://rss-bridge.snopyta.org/?action=display&bridge=Twitter&username={username}&format=Json",
                f"https://wtf.roflcopter.fr/rss-bridge/?action=display&bridge=Twitter&username={username}&format=Json"
            ]
            
            for service_url in rss_bridge_services:
                try:
                    async with aiohttp.ClientSession() as session:
                        async with session.get(service_url, timeout=10) as response:
                            if response.status == 200:
                                data = await response.json()
                                tweets = []
                                
                                for i, item in enumerate(data.get('items', [])[:limit]):
                                    content = item.get('content_text', item.get('title', ''))
                                    if content:
                                        tweets.append({
                                            'id': f"rss_{i}",
                                            'content': content,
                                            'date': item.get('date_published', datetime.now().isoformat()),
                                            'source': 'rss_bridge',
                                            'username': username
                                        })
                                
                                if tweets:
                                    return tweets
                except Exception as e:
                    logger.warning(f"RSS Bridge service failed: {e}")
                    continue
            
            logger.info(f"No working RSS feed found for {username}")
            return []
        except Exception as e:
            logger.error(f"RSS feed scraping failed: {e}")
            return []

    async def _get_profile_info(self, username: str) -> Dict:
        """Get basic profile information with multiple fallback methods"""
        try:
            profile_info = {
                'username': username,
                'platform': 'twitter/x',
                'profile_url': f'https://x.com/{username}',
                'scraped_method': 'fallback'
            }
            
            # Try to get profile info using Selenium if available
            if self.driver:
                try:
                    # Extended list of selectors for profile information
                    selectors = {
                        'display_name': [
                            '[data-testid="UserName"]',
                            'h1[role="heading"]',
                            '.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1wbh5a2 h1'
                        ],
                        'bio': [
                            '[data-testid="UserDescription"]',
                            '.css-901oao.r-18jsvk2.r-37j5jr.r-a023e6.r-16dba41.r-rjixqe.r-bcqeeo.r-bnwqim.r-qvutc0',
                            '.profile-description'
                        ],
                        'followers': [
                            '[data-testid="UserFollowers"]',
                            'a[href$="/followers"]',
                            '.profile-stat[data-nav="followers"]'
                        ]
                    }
                    
                    for field, field_selectors in selectors.items():
                        for selector in field_selectors:
                            try:
                                element = self.driver.find_element(By.CSS_SELECTOR, selector)
                                if element and element.text:
                                    profile_info[field] = element.text.strip()
                                    break
                            except:
                                continue
                                
                except Exception as e:
                    logger.warning(f"Could not extract profile info: {e}")
            
            return profile_info
            
        except Exception as e:
            return {
                'username': username, 
                'error': str(e),
                'platform': 'twitter/x'
            }

# Usage example
async def main():
    # Use the provided bearer token
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAOwp3AEAAAAAvicR4BjNfAmLGttFdGU4qEBFsb4%3DSMQtKgAit99ZAx66GsG850XStmFbE9BwNifmqsyXRQ7N9CFCq2"
    
    scraper = TwitterScraper(bearer_token=bearer_token)
    
    # Test the scraper
    username = "elonmusk"
    result = await scraper.scrape_user(username, limit=50)
    
    print(f"Scraping result for @{username}:")
    print(f"Success: {result.get('success', False)}")
    print(f"Tweets found: {len(result.get('tweets', []))}")
    print(f"Profile info: {result.get('user_info', {})}")
    
    # Print first few tweets
    for i, tweet in enumerate(result.get('tweets', [])[:3]):
        print(f"\nTweet {i+1}:")
        print(f"Content: {tweet['content'][:100]}...")
        print(f"Source: {tweet['source']}")
        print(f"Date: {tweet['date']}")

if __name__ == "__main__":
    asyncio.run(main())
