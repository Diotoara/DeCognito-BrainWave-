# from dotenv import load_dotenv
# import os

# load_dotenv()
# import praw
# import asyncio
# from typing import Dict, List
# import os
# from datetime import datetime

# class RedditScraper:
#     def __init__(self):
#         self.reddit = praw.Reddit(
#             client_id=os.getenv('REDDIT_CLIENT_ID'),
#             client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
#             user_agent=os.getenv('REDDIT_USER_AGENT', 'osint-agent')
#         )
    
#     async def scrape_user(self, username: str, limit: int = 100) -> Dict:
#         try:
#             user = self.reddit.redditor(username)
            
#             # Get user info
#             user_info = {
#                 'username': username,
#                 'created_utc': user.created_utc,
#                 'comment_karma': user.comment_karma,
#                 'link_karma': user.link_karma,
#                 'is_verified': user.verified if hasattr(user, 'verified') else False
#             }
            
#             # Get recent comments
#             comments = []
#             try:
#                 for comment in user.comments.new(limit=limit):
#                     comments.append({
#                         'id': comment.id,
#                         'body': comment.body,
#                         'score': comment.score,
#                         'created_utc': comment.created_utc,
#                         'subreddit': str(comment.subreddit),
#                         'permalink': comment.permalink
#                     })
#             except Exception as e:
#                 print(f"Error fetching comments: {e}")
            
#             # Get recent submissions
#             posts = []
#             try:
#                 for submission in user.submissions.new(limit=limit):
#                     posts.append({
#                         'id': submission.id,
#                         'title': submission.title,
#                         'selftext': submission.selftext,
#                         'score': submission.score,
#                         'created_utc': submission.created_utc,
#                         'subreddit': str(submission.subreddit),
#                         'url': submission.url,
#                         'permalink': submission.permalink
#                     })
#             except Exception as e:
#                 print(f"Error fetching posts: {e}")
            
#             return {
#                 'platform': 'reddit',
#                 'user_info': user_info,
#                 'comments': comments,
#                 'posts': posts,
#                 'scraped_at': datetime.now().isoformat()
#             }
            
#         except Exception as e:
#             return {
#                 'platform': 'reddit',
#                 'error': str(e),
#                 'scraped_at': datetime.now().isoformat()
#             }


# from dotenv import load_dotenv
# import os
# import praw
# import asyncio
# from typing import Dict, List
# from datetime import datetime

# # Load environment FIRST
# load_dotenv()

# class RedditScraper:
#     def __init__(self):
#         try:
#             # Verify environment variables exist
#             required_vars = ['REDDIT_CLIENT_ID', 'REDDIT_CLIENT_SECRET']
#             for var in required_vars:
#                 if not os.getenv(var):
#                     raise ValueError(f"Missing required environment variable: {var}")
            
#             self.reddit = praw.Reddit(
#     client_id=os.getenv('REDDIT_CLIENT_ID').strip('"'),
#     client_secret=os.getenv('REDDIT_CLIENT_SECRET').strip('"'),
#     user_agent=os.getenv('REDDIT_USER_AGENT', 'osint-agent').strip('"'),
#     check_for_updates=False  # Add this line
# )
#             # Test connection
#             self.reddit.user.me()  # Will raise exception if auth fails
#         except Exception as e:
#             raise RuntimeError(f"Reddit authentication failed: {str(e)}")

#     async def scrape_user(self, username: str, limit: int = 100) -> Dict:
#         try:
#             user = self.reddit.redditor(username)
            
#             user_info = {
#                 'username': username,
#                 'created_utc': user.created_utc,
#                 'comment_karma': user.comment_karma,
#                 'link_karma': user.link_karma,
#                 'is_verified': getattr(user, 'verified', False)
#             }
            
#             comments = await self._get_comments(user, limit)
#             posts = await self._get_posts(user, limit)
            
#             return {
#                 'platform': 'reddit',
#                 'user_info': user_info,
#                 'comments': comments,
#                 'posts': posts,
#                 'scraped_at': datetime.now().isoformat()
#             }
            
#         except Exception as e:
#             return {
#                 'platform': 'reddit',
#                 'error': str(e),
#                 'scraped_at': datetime.now().isoformat()
#             }

#     async def _get_comments(self, user, limit):
#         comments = []
#         try:
#             for comment in user.comments.new(limit=limit):
#                 comments.append({
#                     'id': comment.id,
#                     'body': comment.body,
#                     'score': comment.score,
#                     'created_utc': comment.created_utc,
#                     'subreddit': str(comment.subreddit),
#                     'permalink': comment.permalink
#                 })
#         except Exception as e:
#             print(f"Comment error: {e}")
#         return comments

#     async def _get_posts(self, user, limit):
#         posts = []
#         try:
#             for submission in user.submissions.new(limit=limit):
#                 posts.append({
#                     'id': submission.id,
#                     'title': submission.title,
#                     'selftext': submission.selftext,
#                     'score': submission.score,
#                     'created_utc': submission.created_utc,
#                     'subreddit': str(submission.subreddit),
#                     'url': submission.url,
#                     'permalink': submission.permalink
#                 })
#         except Exception as e:
#             print(f"Post error: {e}")
#         return posts


# new 


# from dotenv import load_dotenv
# import os
# import praw
# import asyncio
# from typing import Dict, List
# from datetime import datetime

# # Load environment FIRST
# load_dotenv()

# class RedditScraper:
#     def __init__(self):
#         try:
#             # Verify environment variables exist
#             required_vars = ['REDDIT_CLIENT_ID', 'REDDIT_CLIENT_SECRET']
#             for var in required_vars:
#                 if not os.getenv(var):
#                     raise ValueError(f"Missing required environment variable: {var}")
            
#             self.reddit = praw.Reddit(
#                 client_id=os.getenv('REDDIT_CLIENT_ID').strip('"'),
#                 client_secret=os.getenv('REDDIT_CLIENT_SECRET').strip('"'),
#                 user_agent=os.getenv('REDDIT_USER_AGENT', 'osint-agent').strip('"'),
#                 check_for_updates=False  # Add this line
#             )
            
#             # Test connection
#             print("Testing Reddit connection...")
#             # Don't test with user.me() as it requires OAuth, just test basic functionality
#             print("✓ Reddit scraper initialized successfully")
            
#         except Exception as e:
#             print(f"✗ Reddit authentication failed: {str(e)}")
#             raise RuntimeError(f"Reddit authentication failed: {str(e)}")

#     async def scrape_user(self, username: str, limit: int = 100) -> Dict:
#         try:
#             print(f"Scraping Reddit user: {username}")
#             user = self.reddit.redditor(username)
            
#             user_info = {
#                 'username': username,
#                 'created_utc': user.created_utc,
#                 'comment_karma': user.comment_karma,
#                 'link_karma': user.link_karma,
#                 'is_verified': getattr(user, 'verified', False)
#             }
            
#             comments = await self._get_comments(user, limit)
#             posts = await self._get_posts(user, limit)
            
#             print(f"✓ Reddit scraping completed: {len(comments)} comments, {len(posts)} posts")
            
#             return {
#                 'platform': 'reddit',
#                 'user_info': user_info,
#                 'comments': comments,
#                 'posts': posts,
#                 'scraped_at': datetime.now().isoformat()
#             }
            
#         except Exception as e:
#             print(f"✗ Reddit scraping failed: {str(e)}")
#             return {
#                 'platform': 'reddit',
#                 'error': str(e),
#                 'scraped_at': datetime.now().isoformat()
#             }

#     async def _get_comments(self, user, limit):
#         comments = []
#         try:
#             for comment in user.comments.new(limit=limit):
#                 comments.append({
#                     'id': comment.id,
#                     'body': comment.body,
#                     'score': comment.score,
#                     'created_utc': comment.created_utc,
#                     'subreddit': str(comment.subreddit),
#                     'permalink': comment.permalink
#                 })
#         except Exception as e:
#             print(f"Comment error: {e}")
#         return comments

#     async def _get_posts(self, user, limit):
#         posts = []
#         try:
#             for submission in user.submissions.new(limit=limit):
#                 posts.append({
#                     'id': submission.id,
#                     'title': submission.title,
#                     'selftext': submission.selftext,
#                     'score': submission.score,
#                     'created_utc': submission.created_utc,
#                     'subreddit': str(submission.subreddit),
#                     'url': submission.url,
#                     'permalink': submission.permalink
#                 })
#         except Exception as e:
#             print(f"Post error: {e}")
#         return posts


# # new 
# from dotenv import load_dotenv
# import os
# import sys
# import logging
# from pathlib import Path
# from dotenv import load_dotenv
# from typing import Dict, List
# from datetime import datetime
# import asyncio

# # Load environment variables first
# load_dotenv()

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# try:
#     import praw
#     PRAW_AVAILABLE = True
# except ImportError as e:
#     logger.error(f"PRAW not available: {str(e)}")
#     PRAW_AVAILABLE = False

# class RedditScraper:
#     def __init__(self):
#         if not PRAW_AVAILABLE:
#             raise RuntimeError("PRAW not available. Run: pip install praw")
        
#         try:
#             # Check environment variables
#             required_vars = ['REDDIT_CLIENT_ID', 'REDDIT_CLIENT_SECRET']
#             missing_vars = []
            
#             for var in required_vars:
#                 value = os.getenv(var)
#                 if not value:
#                     missing_vars.append(var)
#                 else:
#                     logger.info(f"✓ {var} found")
            
#             if missing_vars:
#                 raise ValueError(f"Missing required environment variables: {', '.join(missing_vars)}")
            
#             # Initialize Reddit client
#             client_id = os.getenv('REDDIT_CLIENT_ID').strip('"\'')
#             client_secret = os.getenv('REDDIT_CLIENT_SECRET').strip('"\'')
#             user_agent = os.getenv('REDDIT_USER_AGENT', 'osint-research-bot/1.0').strip('"\'')
            
#             logger.info(f"Initializing Reddit client with user agent: {user_agent}")
            
#             self.reddit = praw.Reddit(
#                 client_id=client_id,
#                 client_secret=client_secret,
#                 user_agent=user_agent,
#                 check_for_updates=False,
#                 comment_kind="t1",
#                 message_kind="t4",
#                 redditor_kind="t2",
#                 submission_kind="t3",
#                 subreddit_kind="t5",
#                 trophy_kind="t6"
#             )
            
#             # Test the connection
#             logger.info("Testing Reddit connection...")
#             try:
#                 # Test with a simple subreddit request
#                 test_subreddit = self.reddit.subreddit("test")
#                 test_subreddit.display_name  # This will trigger an API call
#                 logger.info("✓ Reddit connection test successful")
#             except Exception as test_error:
#                 logger.warning(f"Reddit connection test failed: {str(test_error)}")
#                 logger.info("Continuing anyway - connection might work for user scraping")
            
#             logger.info("✓ Reddit scraper initialized successfully")
            
#         except Exception as e:
#             logger.error(f"✗ Reddit scraper initialization failed: {str(e)}")
#             raise RuntimeError(f"Reddit authentication failed: {str(e)}")

#     async def scrape_user(self, username: str, limit: int = 50) -> Dict:
#         """
#         Scrape a Reddit user's posts and comments.
        
#         Args:
#             username: Reddit username to scrape
#             limit: Maximum number of items to fetch
            
#         Returns:
#             Dictionary containing user info, posts, and comments
#         """
#         logger.info(f"Starting Reddit scrape for user: {username}")
        
#         try:
#             # Get user object
#             user = self.reddit.redditor(username)
            
#             # Get basic user info
#             logger.info("Fetching user information...")
#             try:
#                 user_info = {
#                     'username': username,
#                     'created_utc': getattr(user, 'created_utc', None),
#                     'comment_karma': getattr(user, 'comment_karma', 0),
#                     'link_karma': getattr(user, 'link_karma', 0),
#                     'is_verified': getattr(user, 'verified', False),
#                     'has_verified_email': getattr(user, 'has_verified_email', None),
#                     'is_gold': getattr(user, 'is_gold', False),
#                     'is_mod': getattr(user, 'is_mod', False)
#                 }
#                 logger.info(f"✓ User info fetched: {user_info['comment_karma']} comment karma, {user_info['link_karma']} link karma")
#             except Exception as user_error:
#                 logger.error(f"Failed to fetch user info: {str(user_error)}")
#                 user_info = {
#                     'username': username,
#                     'error': f'Failed to fetch user info: {str(user_error)}'
#                 }
            
#             # Get comments
#             logger.info("Fetching user comments...")
#             comments = await self._get_comments(user, limit)
#             logger.info(f"✓ Fetched {len(comments)} comments")
            
#             # Get posts
#             logger.info("Fetching user posts...")
#             posts = await self._get_posts(user, limit)
#             logger.info(f"✓ Fetched {len(posts)} posts")
            
#             result = {
#                 'platform': 'reddit',
#                 'user_info': user_info,
#                 'comments': comments,
#                 'posts': posts,
#                 'scraped_at': datetime.now().isoformat(),
#                 'total_items': len(comments) + len(posts)
#             }
            
#             logger.info(f"✓ Reddit scraping completed successfully for {username}")
#             return result
            
#         except Exception as e:
#             logger.error(f"✗ Reddit scraping failed for {username}: {str(e)}")
#             return {
#                 'platform': 'reddit',
#                 'username': username,
#                 'error': str(e),
#                 'error_type': type(e).__name__,
#                 'scraped_at': datetime.now().isoformat()
#             }

#     async def _get_comments(self, user, limit: int) -> List[Dict]:
#         """Fetch user comments with error handling."""
#         comments = []
#         try:
#             comment_count = 0
#             for comment in user.comments.new(limit=limit):
#                 try:
#                     comment_data = {
#                         'id': comment.id,
#                         'body': comment.body if hasattr(comment, 'body') else '',
#                         'score': getattr(comment, 'score', 0),
#                         'created_utc': getattr(comment, 'created_utc', None),
#                         'subreddit': str(comment.subreddit) if hasattr(comment, 'subreddit') else '',
#                         'permalink': getattr(comment, 'permalink', ''),
#                         'is_submitter': getattr(comment, 'is_submitter', False),
#                         'stickied': getattr(comment, 'stickied', False)
#                     }
#                     comments.append(comment_data)
#                     comment_count += 1
                    
#                     if comment_count % 10 == 0:
#                         logger.info(f"Fetched {comment_count} comments...")
                        
#                 except Exception as comment_error:
#                     logger.warning(f"Failed to process comment: {str(comment_error)}")
#                     continue
                    
#         except Exception as e:
#             logger.error(f"Failed to fetch comments: {str(e)}")
            
#         return comments

#     async def _get_posts(self, user, limit: int) -> List[Dict]:
#         """Fetch user posts with error handling."""
#         posts = []
#         try:
#             post_count = 0
#             for submission in user.submissions.new(limit=limit):
#                 try:
#                     post_data = {
#                         'id': submission.id,
#                         'title': getattr(submission, 'title', ''),
#                         'selftext': getattr(submission, 'selftext', ''),
#                         'score': getattr(submission, 'score', 0),
#                         'created_utc': getattr(submission, 'created_utc', None),
#                         'subreddit': str(submission.subreddit) if hasattr(submission, 'subreddit') else '',
#                         'url': getattr(submission, 'url', ''),
#                         'permalink': getattr(submission, 'permalink', ''),
#                         'num_comments': getattr(submission, 'num_comments', 0),
#                         'upvote_ratio': getattr(submission, 'upvote_ratio', 0),
#                         'is_self': getattr(submission, 'is_self', False),
#                         'stickied': getattr(submission, 'stickied', False)
#                     }
#                     posts.append(post_data)
#                     post_count += 1
                    
#                     if post_count % 10 == 0:
#                         logger.info(f"Fetched {post_count} posts...")
                        
#                 except Exception as post_error:
#                     logger.warning(f"Failed to process post: {str(post_error)}")
#                     continue
                    
#         except Exception as e:
#             logger.error(f"Failed to fetch posts: {str(e)}")
            
#         return posts

#     def test_connection(self) -> Dict:
#         """Test Reddit API connection."""
#         try:
#             # Test with a simple API call
#             test_subreddit = self.reddit.subreddit("test")
#             test_subreddit.display_name
#             return {'status': 'success', 'message': 'Reddit API connection successful'}
#         except Exception as e:
#             return {'status': 'error', 'message': str(e)}

# new 

# import os
# import sys
# import logging
# import requests
# import asyncio
# from typing import Dict, List
# from datetime import datetime
# from dotenv import load_dotenv
# import json
# import time

# # Load environment variables
# load_dotenv()

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# try:
#     import praw
#     PRAW_AVAILABLE = True
#     logger.info("✓ PRAW available")
# except ImportError:
#     PRAW_AVAILABLE = False
#     logger.warning("⚠️ PRAW not available - using scraper only")

# try:
#     from bs4 import BeautifulSoup
#     BS4_AVAILABLE = True
#     logger.info("✓ BeautifulSoup available")
# except ImportError:
#     BS4_AVAILABLE = False
#     logger.warning("⚠️ BeautifulSoup not available")

# class RedditScraper:
#     def __init__(self):
#         self.reddit_api = None
#         self.session = requests.Session()
#         self.session.headers.update({
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
#         })
        
#         # Try to initialize Reddit API
#         if PRAW_AVAILABLE:
#             self._init_reddit_api()
        
#         logger.info("✓ Reddit scraper initialized")

#     def _init_reddit_api(self):
#         """Initialize Reddit API if credentials are available"""
#         try:
#             client_id = os.getenv('REDDIT_CLIENT_ID' , "buDDDHZlsGdxfbpJ1Ib0Q")
#             client_secret = os.getenv('REDDIT_CLIENT_SECRET' , 'Ab13t4Az48jjr4nLkDJr1MnI6ICw')
#             user_agent = os.getenv('REDDIT_USER_AGENT','osint-research-bot/1.0 by u/Background-Fox-448')
            
#             if client_id and client_secret:
#                 self.reddit_api = praw.Reddit(
#                     client_id=client_id.strip('"\''),
#                     client_secret=client_secret.strip('"\''),
#                     user_agent=user_agent.strip('"\''),
#                     check_for_updates=False
#                 )
                
#                 # Test the API
#                 try:
#                     test_sub = self.reddit_api.subreddit("test")
#                     test_sub.display_name
#                     logger.info("✓ Reddit API initialized and tested")
#                     return True
#                 except Exception as e:
#                     logger.warning(f"⚠️ Reddit API test failed: {e}")
#                     self.reddit_api = None
#                     return False
#             else:
#                 logger.warning("⚠️ Reddit API credentials not found")
#                 return False
                
#         except Exception as e:
#             logger.error(f"✗ Reddit API initialization failed: {e}")
#             self.reddit_api = None
#             return False

#     async def scrape_user(self, username: str, limit: int = 50) -> Dict:
#         """
#         Scrape Reddit user with both API and scraper methods
#         """
#         logger.info(f"🔍 Starting Reddit scrape for user: {username}")
        
#         # Method 1: Try Reddit API first
#         if self.reddit_api:
#             logger.info("📡 Trying Reddit API method...")
#             api_result = await self._scrape_with_api(username, limit)
#             if api_result and 'error' not in api_result:
#                 logger.info("✅ Reddit API method successful")
#                 return api_result
#             else:
#                 logger.warning("⚠️ Reddit API method failed, trying scraper...")
        
#         # Method 2: Web scraping fallback
#         logger.info("🕷️ Trying web scraping method...")
#         scraper_result = await self._scrape_with_web(username, limit)
        
#         if scraper_result and 'error' not in scraper_result:
#             logger.info("✅ Web scraping method successful")
#             return scraper_result
#         else:
#             logger.error("❌ Both methods failed")
#             return {
#                 'platform': 'reddit',
#                 'username': username,
#                 'error': 'Both API and scraping methods failed',
#                 'api_error': api_result.get('error') if 'api_result' in locals() else 'API not available',
#                 'scraper_error': scraper_result.get('error') if 'scraper_result' in locals() else 'Scraper failed',
#                 'scraped_at': datetime.now().isoformat()
#             }

#     async def _scrape_with_api(self, username: str, limit: int) -> Dict:
#         """Scrape using Reddit API (PRAW)"""
#         try:
#             user = self.reddit_api.redditor(username)
            
#             # Get user info
#             try:
#                 user_info = {
#                     'username': username,
#                     'created_utc': getattr(user, 'created_utc', None),
#                     'comment_karma': getattr(user, 'comment_karma', 0),
#                     'link_karma': getattr(user, 'link_karma', 0),
#                     'is_verified': getattr(user, 'verified', False),
#                     'has_verified_email': getattr(user, 'has_verified_email', None),
#                     'is_gold': getattr(user, 'is_gold', False),
#                     'is_mod': getattr(user, 'is_mod', False),
#                     'method': 'api'
#                 }
#                 logger.info(f"📊 User karma: {user_info['comment_karma']} comment, {user_info['link_karma']} link")
#             except Exception as e:
#                 logger.error(f"❌ Failed to get user info: {e}")
#                 return {'error': f'User info failed: {str(e)}'}
            
#             # Get comments
#             comments = []
#             try:
#                 comment_count = 0
#                 for comment in user.comments.new(limit=limit):
#                     try:
#                         comment_data = {
#                             'id': comment.id,
#                             'body': getattr(comment, 'body', ''),
#                             'score': getattr(comment, 'score', 0),
#                             'created_utc': getattr(comment, 'created_utc', None),
#                             'subreddit': str(getattr(comment, 'subreddit', '')),
#                             'permalink': getattr(comment, 'permalink', ''),
#                             'is_submitter': getattr(comment, 'is_submitter', False)
#                         }
                        
#                         if comment_data['body'] and comment_data['body'] != '[deleted]':
#                             comments.append(comment_data)
#                             comment_count += 1
                            
#                         if comment_count >= limit:
#                             break
                            
#                     except Exception as e:
#                         logger.warning(f"⚠️ Failed to process comment: {e}")
#                         continue
                        
#                 logger.info(f"📝 Collected {len(comments)} comments")
                        
#             except Exception as e:
#                 logger.error(f"❌ Failed to fetch comments: {e}")
            
#             # Get posts
#             posts = []
#             try:
#                 post_count = 0
#                 for submission in user.submissions.new(limit=limit):
#                     try:
#                         post_data = {
#                             'id': submission.id,
#                             'title': getattr(submission, 'title', ''),
#                             'selftext': getattr(submission, 'selftext', ''),
#                             'score': getattr(submission, 'score', 0),
#                             'created_utc': getattr(submission, 'created_utc', None),
#                             'subreddit': str(getattr(submission, 'subreddit', '')),
#                             'url': getattr(submission, 'url', ''),
#                             'permalink': getattr(submission, 'permalink', ''),
#                             'num_comments': getattr(submission, 'num_comments', 0),
#                             'upvote_ratio': getattr(submission, 'upvote_ratio', 0)
#                         }
                        
#                         if post_data['title']:
#                             posts.append(post_data)
#                             post_count += 1
                            
#                         if post_count >= limit:
#                             break
                            
#                     except Exception as e:
#                         logger.warning(f"⚠️ Failed to process post: {e}")
#                         continue
                        
#                 logger.info(f"📄 Collected {len(posts)} posts")
                        
#             except Exception as e:
#                 logger.error(f"❌ Failed to fetch posts: {e}")
            
#             return {
#                 'platform': 'reddit',
#                 'user_info': user_info,
#                 'comments': comments,
#                 'posts': posts,
#                 'scraped_at': datetime.now().isoformat(),
#                 'total_items': len(comments) + len(posts),
#                 'method': 'api'
#             }
            
#         except Exception as e:
#             logger.error(f"❌ Reddit API scraping failed: {e}")
#             return {'error': f'Reddit API failed: {str(e)}'}

#     async def _scrape_with_web(self, username: str, limit: int) -> Dict:
#         """Scrape using web scraping"""
#         try:
#             # Method 1: Try Reddit JSON API
#             json_result = await self._scrape_reddit_json(username, limit)
#             if json_result and 'error' not in json_result:
#                 return json_result
            
#             # Method 2: Try old.reddit.com
#             old_result = await self._scrape_old_reddit(username, limit)
#             if old_result and 'error' not in old_result:
#                 return old_result
            
#             return {'error': 'All web scraping methods failed'}
            
#         except Exception as e:
#             logger.error(f"❌ Web scraping failed: {e}")
#             return {'error': f'Web scraping failed: {str(e)}'}

#     async def _scrape_reddit_json(self, username: str, limit: int) -> Dict:
#         """Scrape using Reddit's JSON API"""
#         try:
#             logger.info("🔗 Trying Reddit JSON API...")
            
#             comments = []
#             posts = []
            
#             # Get user overview (comments and posts mixed)
#             url = f"https://www.reddit.com/user/{username}.json?limit={limit}"
            
#             response = self.session.get(url, timeout=10)
            
#             if response.status_code == 200:
#                 data = response.json()
                
#                 if 'data' in data and 'children' in data['data']:
#                     for item in data['data']['children']:
#                         try:
#                             item_data = item['data']
                            
#                             if item['kind'] == 't1':  # Comment
#                                 comment = {
#                                     'id': item_data.get('id', ''),
#                                     'body': item_data.get('body', ''),
#                                     'score': item_data.get('score', 0),
#                                     'created_utc': item_data.get('created_utc', None),
#                                     'subreddit': item_data.get('subreddit', ''),
#                                     'permalink': item_data.get('permalink', ''),
#                                     'link_title': item_data.get('link_title', '')
#                                 }
                                
#                                 if comment['body'] and comment['body'] != '[deleted]':
#                                     comments.append(comment)
                                    
#                             elif item['kind'] == 't3':  # Post
#                                 post = {
#                                     'id': item_data.get('id', ''),
#                                     'title': item_data.get('title', ''),
#                                     'selftext': item_data.get('selftext', ''),
#                                     'score': item_data.get('score', 0),
#                                     'created_utc': item_data.get('created_utc', None),
#                                     'subreddit': item_data.get('subreddit', ''),
#                                     'url': item_data.get('url', ''),
#                                     'permalink': item_data.get('permalink', ''),
#                                     'num_comments': item_data.get('num_comments', 0)
#                                 }
                                
#                                 if post['title']:
#                                     posts.append(post)
                                    
#                         except Exception as e:
#                             logger.warning(f"⚠️ Failed to process item: {e}")
#                             continue
                    
#                     logger.info(f"📊 JSON API: {len(comments)} comments, {len(posts)} posts")
                    
#                     return {
#                         'platform': 'reddit',
#                         'user_info': {
#                             'username': username,
#                             'method': 'json_api'
#                         },
#                         'comments': comments,
#                         'posts': posts,
#                         'scraped_at': datetime.now().isoformat(),
#                         'total_items': len(comments) + len(posts),
#                         'method': 'json_api'
#                     }
#                 else:
#                     logger.warning("⚠️ No data found in JSON response")
#                     return {'error': 'No data in JSON response'}
#             else:
#                 logger.warning(f"⚠️ JSON API returned {response.status_code}")
#                 return {'error': f'JSON API returned {response.status_code}'}
                
#         except Exception as e:
#             logger.error(f"❌ JSON API scraping failed: {e}")
#             return {'error': f'JSON API failed: {str(e)}'}

#     async def _scrape_old_reddit(self, username: str, limit: int) -> Dict:
#         """Scrape using old.reddit.com"""
#         try:
#             if not BS4_AVAILABLE:
#                 return {'error': 'BeautifulSoup not available'}
            
#             logger.info("🕸️ Trying old.reddit.com...")
            
#             url = f"https://old.reddit.com/user/{username}"
#             response = self.session.get(url, timeout=10)
            
#             if response.status_code == 200:
#                 soup = BeautifulSoup(response.content, 'html.parser')
                
#                 comments = []
#                 posts = []
                
#                 # Find all entries
#                 entries = soup.find_all('div', class_='entry')
                
#                 for entry in entries[:limit]:
#                     try:
#                         # Check if it's a comment or post
#                         if entry.find('div', class_='md'):  # Comment
#                             comment_text = entry.find('div', class_='md')
#                             if comment_text:
#                                 comment = {
#                                     'body': comment_text.get_text(strip=True),
#                                     'score': 0,  # Hard to extract from old reddit
#                                     'subreddit': '',
#                                     'method': 'old_reddit'
#                                 }
                                
#                                 if comment['body'] and len(comment['body']) > 10:
#                                     comments.append(comment)
                        
#                         # Look for post titles
#                         title_elem = entry.find('a', class_='title')
#                         if title_elem:
#                             post = {
#                                 'title': title_elem.get_text(strip=True),
#                                 'url': title_elem.get('href', ''),
#                                 'score': 0,
#                                 'method': 'old_reddit'
#                             }
                            
#                             if post['title']:
#                                 posts.append(post)
                                
#                     except Exception as e:
#                         logger.warning(f"⚠️ Failed to process entry: {e}")
#                         continue
                
#                 logger.info(f"📊 Old Reddit: {len(comments)} comments, {len(posts)} posts")
                
#                 return {
#                     'platform': 'reddit',
#                     'user_info': {
#                         'username': username,
#                         'method': 'old_reddit'
#                     },
#                     'comments': comments,
#                     'posts': posts,
#                     'scraped_at': datetime.now().isoformat(),
#                     'total_items': len(comments) + len(posts),
#                     'method': 'old_reddit'
#                 }
#             else:
#                 return {'error': f'Old Reddit returned {response.status_code}'}
                
#         except Exception as e:
#             logger.error(f"❌ Old Reddit scraping failed: {e}")
#             return {'error': f'Old Reddit failed: {str(e)}'}

#     def test_connection(self) -> Dict:
#         """Test Reddit connection"""
#         if self.reddit_api:
#             try:
#                 test_sub = self.reddit_api.subreddit("test")
#                 test_sub.display_name
#                 return {'status': 'success', 'method': 'api', 'message': 'Reddit API working'}
#             except Exception as e:
#                 return {'status': 'error', 'method': 'api', 'message': str(e)}
#         else:
#             # Test web scraping
#             try:
#                 response = self.session.get("https://www.reddit.com/r/test.json", timeout=5)
#                 if response.status_code == 200:
#                     return {'status': 'success', 'method': 'scraper', 'message': 'Reddit scraping working'}
#                 else:
#                     return {'status': 'error', 'method': 'scraper', 'message': f'HTTP {response.status_code}'}
#             except Exception as e:
#                 return {'status': 'error', 'method': 'scraper', 'message': str(e)}




# !new above best 

import os
import sys
import logging
import requests
import asyncio
from typing import Dict, List
from datetime import datetime
from dotenv import load_dotenv
import json
import time

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    import praw
    PRAW_AVAILABLE = True
    logger.info("✓ PRAW available")
except ImportError:
    PRAW_AVAILABLE = False
    logger.warning("⚠️ PRAW not available - using scraper only")

try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
    logger.info("✓ BeautifulSoup available")
except ImportError:
    BS4_AVAILABLE = False
    logger.warning("⚠️ BeautifulSoup not available")

class RedditScraper:
    def __init__(self):
        self.reddit_api = None
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        })
        
        # Try to initialize Reddit API
        if PRAW_AVAILABLE:
            self._init_reddit_api()
        
        logger.info("✓ Reddit scraper initialized")

    def _init_reddit_api(self):
        """Initialize Reddit API if credentials are available"""
        try:
            client_id = os.getenv('REDDIT_CLIENT_ID', "buDDDHZlsGdxfbpJ1Ib0Q")
            client_secret = os.getenv('REDDIT_CLIENT_SECRET', 'Ab13t4Az48jjr4nLkDJr1MnI6ICw')
            user_agent = os.getenv('REDDIT_USER_AGENT', 'osint-research-bot/1.0 by u/Background-Fox-448')
            
            if client_id and client_secret:
                self.reddit_api = praw.Reddit(
                    client_id=client_id.strip('"\''),
                    client_secret=client_secret.strip('"\''),
                    user_agent=user_agent.strip('"\''),
                    check_for_updates=False
                )
                
                # Test the API
                try:
                    test_sub = self.reddit_api.subreddit("test")
                    test_sub.display_name
                    logger.info("✓ Reddit API initialized and tested")
                    return True
                except Exception as e:
                    logger.warning(f"⚠️ Reddit API test failed: {e}")
                    self.reddit_api = None
                    return False
            else:
                logger.warning("⚠️ Reddit API credentials not found")
                return False
                
        except Exception as e:
            logger.error(f"✗ Reddit API initialization failed: {e}")
            self.reddit_api = None
            return False

    async def scrape_user(self, username: str, limit: int = 50) -> Dict:
        """
        Scrape Reddit user with both API and scraper methods
        """
        logger.info(f"🔍 Starting Reddit scrape for user: {username}")
        
        # Method 1: Try Reddit API first
        if self.reddit_api:
            logger.info("📡 Trying Reddit API method...")
            api_result = await self._scrape_with_api(username, limit)
            if api_result and 'error' not in api_result:
                logger.info("✅ Reddit API method successful")
                return api_result
            else:
                logger.warning("⚠️ Reddit API method failed, trying scraper...")
        
        # Method 2: Web scraping fallback
        logger.info("🕷️ Trying web scraping method...")
        scraper_result = await self._scrape_with_web(username, limit)
        
        if scraper_result and 'error' not in scraper_result:
            logger.info("✅ Web scraping method successful")
            return scraper_result
        else:
            logger.error("❌ Both methods failed")
            return {
                'platform': 'reddit',
                'username': username,
                'error': 'Both API and scraping methods failed',
                'api_error': api_result.get('error') if 'api_result' in locals() else 'API not available',
                'scraper_error': scraper_result.get('error') if 'scraper_result' in locals() else 'Scraper failed',
                'scraped_at': datetime.now().isoformat()
            }

    async def _scrape_with_api(self, username: str, limit: int) -> Dict:
        """Scrape using Reddit API (PRAW)"""
        try:
            user = self.reddit_api.redditor(username)
            
            # Get user info
            try:
                user_info = {
                    'username': username,
                    'created_utc': getattr(user, 'created_utc', None),
                    'comment_karma': getattr(user, 'comment_karma', 0),
                    'link_karma': getattr(user, 'link_karma', 0),
                    'is_verified': getattr(user, 'verified', False),
                    'has_verified_email': getattr(user, 'has_verified_email', None),
                    'is_gold': getattr(user, 'is_gold', False),
                    'is_mod': getattr(user, 'is_mod', False),
                    'method': 'api'
                }
                logger.info(f"📊 User karma: {user_info['comment_karma']} comment, {user_info['link_karma']} link")
            except Exception as e:
                logger.error(f"❌ Failed to get user info: {e}")
                return {'error': f'User info failed: {str(e)}'}
            
            # Get comments
            comments = []
            try:
                comment_count = 0
                for comment in user.comments.new(limit=limit):
                    try:
                        comment_data = {
                            'id': comment.id,
                            'body': getattr(comment, 'body', ''),
                            'score': getattr(comment, 'score', 0),
                            'created_utc': getattr(comment, 'created_utc', None),
                            'subreddit': str(getattr(comment, 'subreddit', '')),
                            'permalink': getattr(comment, 'permalink', ''),
                            'is_submitter': getattr(comment, 'is_submitter', False)
                        }
                        
                        if comment_data['body'] and comment_data['body'] != '[deleted]':
                            comments.append(comment_data)
                            comment_count += 1
                            
                        if comment_count >= limit:
                            break
                            
                    except Exception as e:
                        logger.warning(f"⚠️ Failed to process comment: {e}")
                        continue
                        
                logger.info(f"📝 Collected {len(comments)} comments")
                        
            except Exception as e:
                logger.error(f"❌ Failed to fetch comments: {e}")
            
            # Get posts
            posts = []
            try:
                post_count = 0
                for submission in user.submissions.new(limit=limit):
                    try:
                        post_data = {
                            'id': submission.id,
                            'title': getattr(submission, 'title', ''),
                            'selftext': getattr(submission, 'selftext', ''),
                            'score': getattr(submission, 'score', 0),
                            'created_utc': getattr(submission, 'created_utc', None),
                            'subreddit': str(getattr(submission, 'subreddit', '')),
                            'url': getattr(submission, 'url', ''),
                            'permalink': getattr(submission, 'permalink', ''),
                            'num_comments': getattr(submission, 'num_comments', 0),
                            'upvote_ratio': getattr(submission, 'upvote_ratio', 0)
                        }
                        
                        if post_data['title']:
                            posts.append(post_data)
                            post_count += 1
                            
                        if post_count >= limit:
                            break
                            
                    except Exception as e:
                        logger.warning(f"⚠️ Failed to process post: {e}")
                        continue
                        
                logger.info(f"📄 Collected {len(posts)} posts")
                        
            except Exception as e:
                logger.error(f"❌ Failed to fetch posts: {e}")
            
            return {
                'platform': 'reddit',
                'user_info': user_info,
                'comments': comments,
                'posts': posts,
                'scraped_at': datetime.now().isoformat(),
                'total_items': len(comments) + len(posts),
                'method': 'api'
            }
            
        except Exception as e:
            logger.error(f"❌ Reddit API scraping failed: {e}")
            return {'error': f'Reddit API failed: {str(e)}'}

    async def _scrape_with_web(self, username: str, limit: int) -> Dict:
        """Scrape using web scraping"""
        try:
            # Method 1: Try Reddit JSON API
            json_result = await self._scrape_reddit_json(username, limit)
            if json_result and 'error' not in json_result:
                return json_result
            
            # Method 2: Try old.reddit.com
            old_result = await self._scrape_old_reddit(username, limit)
            if old_result and 'error' not in old_result:
                return old_result
            
            return {'error': 'All web scraping methods failed'}
            
        except Exception as e:
            logger.error(f"❌ Web scraping failed: {e}")
            return {'error': f'Web scraping failed: {str(e)}'}

    async def _scrape_reddit_json(self, username: str, limit: int) -> Dict:
        """Scrape using Reddit's JSON API"""
        try:
            logger.info("🔗 Trying Reddit JSON API...")
            
            comments = []
            posts = []
            
            # Get user overview (comments and posts mixed)
            url = f"https://www.reddit.com/user/{username}.json?limit={limit}"
            
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                
                if 'data' in data and 'children' in data['data']:
                    for item in data['data']['children']:
                        try:
                            item_data = item['data']
                            
                            if item['kind'] == 't1':  # Comment
                                comment = {
                                    'id': item_data.get('id', ''),
                                    'body': item_data.get('body', ''),
                                    'score': item_data.get('score', 0),
                                    'created_utc': item_data.get('created_utc', None),
                                    'subreddit': item_data.get('subreddit', ''),
                                    'permalink': item_data.get('permalink', ''),
                                    'link_title': item_data.get('link_title', '')
                                }
                                
                                if comment['body'] and comment['body'] != '[deleted]':
                                    comments.append(comment)
                                    
                            elif item['kind'] == 't3':  # Post
                                post = {
                                    'id': item_data.get('id', ''),
                                    'title': item_data.get('title', ''),
                                    'selftext': item_data.get('selftext', ''),
                                    'score': item_data.get('score', 0),
                                    'created_utc': item_data.get('created_utc', None),
                                    'subreddit': item_data.get('subreddit', ''),
                                    'url': item_data.get('url', ''),
                                    'permalink': item_data.get('permalink', ''),
                                    'num_comments': item_data.get('num_comments', 0)
                                }
                                
                                if post['title']:
                                    posts.append(post)
                                    
                        except Exception as e:
                            logger.warning(f"⚠️ Failed to process item: {e}")
                            continue
                    
                    logger.info(f"📊 JSON API: {len(comments)} comments, {len(posts)} posts")
                    
                    return {
                        'platform': 'reddit',
                        'user_info': {
                            'username': username,
                            'method': 'json_api'
                        },
                        'comments': comments,
                        'posts': posts,
                        'scraped_at': datetime.now().isoformat(),
                        'total_items': len(comments) + len(posts),
                        'method': 'json_api'
                    }
                else:
                    logger.warning("⚠️ No data found in JSON response")
                    return {'error': 'No data in JSON response'}
            else:
                logger.warning(f"⚠️ JSON API returned {response.status_code}")
                return {'error': f'JSON API returned {response.status_code}'}
                
        except Exception as e:
            logger.error(f"❌ JSON API scraping failed: {e}")
            return {'error': f'JSON API failed: {str(e)}'}

    async def _scrape_old_reddit(self, username: str, limit: int) -> Dict:
        """Scrape using old.reddit.com"""
        try:
            if not BS4_AVAILABLE:
                return {'error': 'BeautifulSoup not available'}
            
            logger.info("🕸️ Trying old.reddit.com...")
            
            url = f"https://old.reddit.com/user/{username}"
            response = self.session.get(url, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                
                comments = []
                posts = []
                
                # Find all entries
                entries = soup.find_all('div', class_='entry')
                
                for entry in entries[:limit]:
                    try:
                        # Check if it's a comment or post
                        if entry.find('div', class_='md'):  # Comment
                            comment_text = entry.find('div', class_='md')
                            if comment_text:
                                comment = {
                                    'body': comment_text.get_text(strip=True),
                                    'score': 0,  # Hard to extract from old reddit
                                    'subreddit': '',
                                    'method': 'old_reddit'
                                }
                                
                                if comment['body'] and len(comment['body']) > 10:
                                    comments.append(comment)
                        
                        # Look for post titles
                        title_elem = entry.find('a', class_='title')
                        if title_elem:
                            post = {
                                'title': title_elem.get_text(strip=True),
                                'url': title_elem.get('href', ''),
                                'score': 0,
                                'method': 'old_reddit'
                            }
                            
                            if post['title']:
                                posts.append(post)
                                
                    except Exception as e:
                        logger.warning(f"⚠️ Failed to process entry: {e}")
                        continue
                
                logger.info(f"📊 Old Reddit: {len(comments)} comments, {len(posts)} posts")
                
                return {
                    'platform': 'reddit',
                    'user_info': {
                        'username': username,
                        'method': 'old_reddit'
                    },
                    'comments': comments,
                    'posts': posts,
                    'scraped_at': datetime.now().isoformat(),
                    'total_items': len(comments) + len(posts),
                    'method': 'old_reddit'
                }
            else:
                return {'error': f'Old Reddit returned {response.status_code}'}
                
        except Exception as e:
            logger.error(f"❌ Old Reddit scraping failed: {e}")
            return {'error': f'Old Reddit failed: {str(e)}'}

    def test_connection(self) -> Dict:
        """Test Reddit connection"""
        if self.reddit_api:
            try:
                test_sub = self.reddit_api.subreddit("test")
                test_sub.display_name
                return {'status': 'success', 'method': 'api', 'message': 'Reddit API working'}
            except Exception as e:
                return {'status': 'error', 'method': 'api', 'message': str(e)}
        else:
            # Test web scraping
            try:
                response = self.session.get("https://www.reddit.com/r/test.json", timeout=5)
                if response.status_code == 200:
                    return {'status': 'success', 'method': 'scraper', 'message': 'Reddit scraping working'}
                else:
                    return {'status': 'error', 'method': 'scraper', 'message': f'HTTP {response.status_code}'}
            except Exception as e:
                return {'status': 'error', 'method': 'scraper', 'message': str(e)}
