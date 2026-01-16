# import instaloader
# import asyncio
# from typing import Dict, List
# import os
# from datetime import datetime
# import requests
# from bs4 import BeautifulSoup

# class InstagramScraper:
#     def __init__(self):
#         self.loader = instaloader.Instaloader()
#         # Configure instaloader settings
#         self.loader.context.log = lambda *args, **kwargs: None  # Disable logging
#         self.session = requests.Session()
#         self.session.headers.update({
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
#         })
    
#     async def scrape_user(self, username: str, limit: int = 50) -> Dict:
#         try:
#             # Method 1: instaloader (primary)
#             try:
#                 profile = instaloader.Profile.from_username(self.loader.context, username)
                
#                 # Get profile information
#                 profile_info = {
#                     'username': username,
#                     'full_name': profile.full_name,
#                     'biography': profile.biography,
#                     'followers': profile.followers,
#                     'followees': profile.followees,
#                     'posts_count': profile.mediacount,
#                     'is_verified': profile.is_verified,
#                     'is_private': profile.is_private,
#                     'external_url': profile.external_url,
#                     'profile_pic_url': profile.profile_pic_url
#                 }
                
#                 # Get recent posts (only if public)
#                 posts = []
#                 if not profile.is_private:
#                     try:
#                         post_count = 0
#                         for post in profile.get_posts():
#                             if post_count >= limit:
#                                 break
                            
#                             posts.append({
#                                 'shortcode': post.shortcode,
#                                 'caption': post.caption if post.caption else '',
#                                 'likes': post.likes,
#                                 'comments': post.comments,
#                                 'date': post.date.isoformat() if post.date else None,
#                                 'is_video': post.is_video,
#                                 'url': f"https://instagram.com/p/{post.shortcode}/",
#                                 'hashtags': list(post.caption_hashtags) if post.caption_hashtags else [],
#                                 'mentions': list(post.caption_mentions) if post.caption_mentions else []
#                             })
#                             post_count += 1
#                     except Exception as e:
#                         print(f"Error fetching posts: {e}")
                
#                 return {
#                     'platform': 'instagram',
#                     'user_info': profile_info,
#                     'posts': posts,
#                     'scraped_at': datetime.now().isoformat(),
#                     'method': 'instaloader'
#                 }
                
#             except Exception as e:
#                 print(f"Instaloader failed: {e}")
#                 # Fallback to web scraping
#                 return await self._scrape_instagram_web(username)
                
#         except Exception as e:
#             return {
#                 'platform': 'instagram',
#                 'error': str(e),
#                 'scraped_at': datetime.now().isoformat()
#             }
    
#     async def _scrape_instagram_web(self, username: str) -> Dict:
#         """Fallback web scraping method"""
#         try:
#             # Note: Instagram heavily restricts web scraping
#             # This is a basic implementation that may not work reliably
#             url = f"https://www.instagram.com/{username}/"
            
#             headers = {
#                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
#                 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#                 'Accept-Language': 'en-US,en;q=0.5',
#                 'Accept-Encoding': 'gzip, deflate',
#                 'Connection': 'keep-alive',
#             }
            
#             response = self.session.get(url, headers=headers)
            
#             if response.status_code == 200:
#                 # Try to extract basic profile info from HTML
#                 soup = BeautifulSoup(response.content, 'html.parser')
                
#                 # Look for JSON data in script tags
#                 scripts = soup.find_all('script', type='application/ld+json')
#                 profile_info = {'username': username, 'method': 'web_scrape'}
                
#                 for script in scripts:
#                     try:
#                         import json
#                         data = json.loads(script.string)
#                         if '@type' in data and data['@type'] == 'Person':
#                             profile_info.update({
#                                 'name': data.get('name', ''),
#                                 'description': data.get('description', ''),
#                                 'url': data.get('url', '')
#                             })
#                             break
#                     except:
#                         continue
                
#                 return {
#                     'platform': 'instagram',
#                     'user_info': profile_info,
#                     'posts': [],
#                     'scraped_at': datetime.now().isoformat(),
#                     'method': 'web_scrape',
#                     'note': 'Limited data due to Instagram restrictions'
#                 }
#             else:
#                 raise Exception(f"HTTP {response.status_code}")
                
#         except Exception as e:
#             return {
#                 'platform': 'instagram',
#                 'error': f'Web scraping failed: {str(e)}',
#                 'scraped_at': datetime.now().isoformat(),
#                 'note': 'Instagram heavily restricts automated access'
#             }
    
#     async def search_hashtag(self, hashtag: str, limit: int = 20) -> Dict:
#         """Search posts by hashtag"""
#         try:
#             hashtag_obj = instaloader.Hashtag.from_name(self.loader.context, hashtag)
            
#             posts = []
#             post_count = 0
            
#             for post in hashtag_obj.get_posts():
#                 if post_count >= limit:
#                     break
                
#                 posts.append({
#                     'shortcode': post.shortcode,
#                     'caption': post.caption if post.caption else '',
#                     'likes': post.likes,
#                     'comments': post.comments,
#                     'date': post.date.isoformat() if post.date else None,
#                     'owner': post.owner_username,
#                     'url': f"https://instagram.com/p/{post.shortcode}/"
#                 })
#                 post_count += 1
            
#             return {
#                 'hashtag': hashtag,
#                 'posts': posts,
#                 'total_found': len(posts),
#                 'scraped_at': datetime.now().isoformat()
#             }
            
#         except Exception as e:
#             return {
#                 'hashtag': hashtag,
#                 'error': str(e),
#                 'scraped_at': datetime.now().isoformat()
#             }


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
# import re

# # Load environment variables
# load_dotenv()

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# try:
#     import instaloader
#     INSTALOADER_AVAILABLE = True
#     logger.info("✓ Instaloader available")
# except ImportError:
#     INSTALOADER_AVAILABLE = False
#     logger.warning("⚠️ Instaloader not available - using scraper only")

# try:
#     from bs4 import BeautifulSoup
#     BS4_AVAILABLE = True
#     logger.info("✓ BeautifulSoup available")
# except ImportError:
#     BS4_AVAILABLE = False
#     logger.warning("⚠️ BeautifulSoup not available")

# class InstagramScraper:
#     def __init__(self):
#         self.loader = None
#         self.session = requests.Session()
#         self.session.headers.update({
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#             'Accept-Language': 'en-US,en;q=0.5',
#             'Accept-Encoding': 'gzip, deflate',
#             'Connection': 'keep-alive',
#             'Upgrade-Insecure-Requests': '1'
#         })
        
#         # Try to initialize Instaloader
#         if INSTALOADER_AVAILABLE:
#             self._init_instaloader()
        
#         logger.info("✓ Instagram scraper initialized")

#     def _init_instaloader(self):
#         """Initialize Instaloader"""
#         try:
#             self.loader = instaloader.Instaloader()
#             self.loader.context.log = lambda *args, **kwargs: None  # Disable logging
#             logger.info("✓ Instaloader initialized")
#             return True
#         except Exception as e:
#             logger.error(f"✗ Instaloader initialization failed: {e}")
#             self.loader = None
#             return False

#     async def scrape_user(self, username: str, limit: int = 50) -> Dict:
#         """
#         Scrape Instagram user with both API and scraper methods
#         """
#         logger.info(f"🔍 Starting Instagram scrape for user: {username}")
        
#         # Method 1: Try Instaloader first
#         if self.loader:
#             logger.info("📡 Trying Instaloader method...")
#             instaloader_result = await self._scrape_with_instaloader(username, limit)
#             if instaloader_result and 'error' not in instaloader_result:
#                 logger.info("✅ Instaloader method successful")
#                 return instaloader_result
#             else:
#                 logger.warning("⚠️ Instaloader method failed, trying scraper...")
        
#         # Method 2: Web scraping fallback
#         logger.info("🕷️ Trying web scraping method...")
#         scraper_result = await self._scrape_with_web(username, limit)
        
#         if scraper_result and 'error' not in scraper_result:
#             logger.info("✅ Web scraping method successful")
#             return scraper_result
#         else:
#             logger.error("❌ Both methods failed")
#             return {
#                 'platform': 'instagram',
#                 'username': username,
#                 'error': 'Both Instaloader and scraping methods failed',
#                 'instaloader_error': instaloader_result.get('error') if 'instaloader_result' in locals() else 'Instaloader not available',
#                 'scraper_error': scraper_result.get('error') if 'scraper_result' in locals() else 'Scraper failed',
#                 'scraped_at': datetime.now().isoformat()
#             }

#     async def _scrape_with_instaloader(self, username: str, limit: int) -> Dict:
#         """Scrape using Instaloader"""
#         try:
#             profile = instaloader.Profile.from_username(self.loader.context, username)
            
#             # Get profile information
#             profile_info = {
#                 'username': username,
#                 'full_name': profile.full_name,
#                 'biography': profile.biography,
#                 'followers': profile.followers,
#                 'followees': profile.followees,
#                 'posts_count': profile.mediacount,
#                 'is_verified': profile.is_verified,
#                 'is_private': profile.is_private,
#                 'external_url': profile.external_url,
#                 'profile_pic_url': profile.profile_pic_url,
#                 'method': 'instaloader'
#             }
            
#             logger.info(f"👤 Profile: {profile_info['full_name']} ({profile_info['followers']} followers)")
            
#             # Get recent posts (only if public)
#             posts = []
#             if not profile.is_private:
#                 try:
#                     post_count = 0
#                     for post in profile.get_posts():
#                         if post_count >= limit:
#                             break
                        
#                         # Extract hashtags and mentions
#                         hashtags = []
#                         mentions = []
                        
#                         if post.caption:
#                             hashtags = re.findall(r'#(\w+)', post.caption)
#                             mentions = re.findall(r'@(\w+)', post.caption)
                        
#                         post_data = {
#                             'shortcode': post.shortcode,
#                             'caption': post.caption if post.caption else '',
#                             'likes': post.likes,
#                             'comments': post.comments,
#                             'date': post.date.isoformat() if post.date else None,
#                             'is_video': post.is_video,
#                             'url': f"https://instagram.com/p/{post.shortcode}/",
#                             'hashtags': hashtags,
#                             'mentions': mentions,
#                             'location': post.location.name if post.location else None
#                         }
                        
#                         posts.append(post_data)
#                         post_count += 1
                        
#                     logger.info(f"📸 Collected {len(posts)} posts")
                        
#                 except Exception as e:
#                     logger.error(f"❌ Error fetching posts: {e}")
#             else:
#                 logger.info("🔒 Profile is private, cannot fetch posts")
            
#             return {
#                 'platform': 'instagram',
#                 'user_info': profile_info,
#                 'posts': posts,
#                 'scraped_at': datetime.now().isoformat(),
#                 'total_items': len(posts),
#                 'method': 'instaloader'
#             }
            
#         except Exception as e:
#             logger.error(f"❌ Instaloader scraping failed: {e}")
#             return {'error': f'Instaloader failed: {str(e)}'}

#     async def _scrape_with_web(self, username: str, limit: int) -> Dict:
#         """Scrape using web scraping methods"""
#         try:
#             # Method 1: Try Instagram web interface
#             web_result = await self._scrape_instagram_web(username, limit)
#             if web_result and 'error' not in web_result:
#                 return web_result
            
#             # Method 2: Try alternative methods
#             alt_result = await self._scrape_instagram_alternative(username, limit)
#             if alt_result and 'error' not in alt_result:
#                 return alt_result
            
#             return {'error': 'All web scraping methods failed'}
            
#         except Exception as e:
#             logger.error(f"❌ Web scraping failed: {e}")
#             return {'error': f'Web scraping failed: {str(e)}'}

#     async def _scrape_instagram_web(self, username: str, limit: int) -> Dict:
#         """Scrape Instagram web interface"""
#         try:
#             logger.info("🌐 Trying Instagram web interface...")
            
#             url = f"https://www.instagram.com/{username}/"
            
#             # Add Instagram-specific headers
#             headers = {
#                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
#                 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#                 'Accept-Language': 'en-US,en;q=0.9',
#                 'Accept-Encoding': 'gzip, deflate, br',
#                 'Connection': 'keep-alive',
#                 'Upgrade-Insecure-Requests': '1',
#                 'Sec-Fetch-Dest': 'document',
#                 'Sec-Fetch-Mode': 'navigate',
#                 'Sec-Fetch-Site': 'none'
#             }
            
#             response = self.session.get(url, headers=headers, timeout=15)
            
#             if response.status_code == 200:
#                 # Try to extract JSON data from the page
#                 content = response.text
                
#                 # Look for JSON data in script tags
#                 json_data = None
                
#                 # Pattern 1: window._sharedData
#                 shared_data_match = re.search(r'window\._sharedData\s*=\s*({.+?});', content)
#                 if shared_data_match:
#                     try:
#                         json_data = json.loads(shared_data_match.group(1))
#                         logger.info("📊 Found _sharedData")
#                     except:
#                         pass
                
#                 # Pattern 2: Look for profile data in script tags
#                 if not json_data:
#                     script_matches = re.findall(r'<script[^>]*>([^<]*)</script>', content)
#                     for script in script_matches:
#                         if 'ProfilePage' in script or 'graphql' in script:
#                             try:
#                                 # Try to extract JSON from the script
#                                 json_match = re.search(r'({.*"ProfilePage".*})', script)
#                                 if json_match:
#                                     json_data = json.loads(json_match.group(1))
#                                     logger.info("📊 Found ProfilePage data")
#                                     break
#                             except:
#                                 continue
                
#                 if json_data:
#                     return await self._parse_instagram_json(json_data, username)
#                 else:
#                     # Fallback to HTML parsing
#                     if BS4_AVAILABLE:
#                         return await self._parse_instagram_html(content, username)
#                     else:
#                         return {'error': 'No JSON data found and BeautifulSoup not available'}
#             else:
#                 logger.warning(f"⚠️ Instagram returned {response.status_code}")
#                 return {'error': f'Instagram returned {response.status_code}'}
                
#         except Exception as e:
#             logger.error(f"❌ Instagram web scraping failed: {e}")
#             return {'error': f'Instagram web scraping failed: {str(e)}'}

#     async def _parse_instagram_json(self, json_data: dict, username: str) -> Dict:
#         """Parse Instagram JSON data"""
#         try:
#             logger.info("🔍 Parsing Instagram JSON data...")
            
#             profile_info = {
#                 'username': username,
#                 'method': 'web_json'
#             }
            
#             posts = []
            
#             # Try to find user data in various locations
#             user_data = None
            
#             # Look in entry_data.ProfilePage
#             if 'entry_data' in json_data and 'ProfilePage' in json_data['entry_data']:
#                 profile_page = json_data['entry_data']['ProfilePage'][0]
#                 if 'graphql' in profile_page and 'user' in profile_page['graphql']:
#                     user_data = profile_page['graphql']['user']
            
#             # Look in other locations
#             if not user_data and 'graphql' in json_data and 'user' in json_data['graphql']:
#                 user_data = json_data['graphql']['user']
            
#             if user_data:
#                 profile_info.update({
#                     'full_name': user_data.get('full_name', ''),
#                     'biography': user_data.get('biography', ''),
#                     'followers': user_data.get('edge_followed_by', {}).get('count', 0),
#                     'following': user_data.get('edge_follow', {}).get('count', 0),
#                     'posts_count': user_data.get('edge_owner_to_timeline_media', {}).get('count', 0),
#                     'is_verified': user_data.get('is_verified', False),
#                     'is_private': user_data.get('is_private', False),
#                     'external_url': user_data.get('external_url', ''),
#                     'profile_pic_url': user_data.get('profile_pic_url', '')
#                 })
                
#                 # Extract posts
#                 if 'edge_owner_to_timeline_media' in user_data:
#                     media_edges = user_data['edge_owner_to_timeline_media'].get('edges', [])
                    
#                     for edge in media_edges[:50]:  # Limit posts
#                         node = edge.get('node', {})
                        
#                         # Extract caption
#                         caption = ''
#                         if 'edge_media_to_caption' in node:
#                             caption_edges = node['edge_media_to_caption'].get('edges', [])
#                             if caption_edges:
#                                 caption = caption_edges[0].get('node', {}).get('text', '')
                        
#                         # Extract hashtags and mentions
#                         hashtags = re.findall(r'#(\w+)', caption) if caption else []
#                         mentions = re.findall(r'@(\w+)', caption) if caption else []
                        
#                         post_data = {
#                             'shortcode': node.get('shortcode', ''),
#                             'caption': caption,
#                             'likes': node.get('edge_liked_by', {}).get('count', 0),
#                             'comments': node.get('edge_media_to_comment', {}).get('count', 0),
#                             'date': datetime.fromtimestamp(node.get('taken_at_timestamp', 0)).isoformat() if node.get('taken_at_timestamp') else None,
#                             'is_video': node.get('is_video', False),
#                             'url': f"https://instagram.com/p/{node.get('shortcode', '')}/",
#                             'hashtags': hashtags,
#                             'mentions': mentions,
#                             'display_url': node.get('display_url', '')
#                         }
                        
#                         posts.append(post_data)
                
#                 logger.info(f"📊 Parsed profile: {profile_info.get('full_name')} ({len(posts)} posts)")
            
#             return {
#                 'platform': 'instagram',
#                 'user_info': profile_info,
#                 'posts': posts,
#                 'scraped_at': datetime.now().isoformat(),
#                 'total_items': len(posts),
#                 'method': 'web_json'
#             }
            
#         except Exception as e:
#             logger.error(f"❌ JSON parsing failed: {e}")
#             return {'error': f'JSON parsing failed: {str(e)}'}

#     async def _parse_instagram_html(self, content: str, username: str) -> Dict:
#         """Parse Instagram HTML content"""
#         try:
#             logger.info("🕸️ Parsing Instagram HTML...")
            
#             soup = BeautifulSoup(content, 'html.parser')
            
#             profile_info = {
#                 'username': username,
#                 'method': 'html_parsing'
#             }
            
#             # Try to extract basic info from meta tags
#             meta_description = soup.find('meta', {'name': 'description'})
#             if meta_description:
#                 desc_content = meta_description.get('content', '')
#                 # Try to extract follower count from description
#                 follower_match = re.search(r'(\d+(?:,\d+)*)\s+Followers', desc_content)
#                 if follower_match:
#                     follower_count = follower_match.group(1).replace(',', '')
#                     profile_info['followers'] = int(follower_count)
            
#             # Try to extract title
#             title_tag = soup.find('title')
#             if title_tag:
#                 title_text = title_tag.get_text()
#                 # Extract name from title
#                 name_match = re.search(r'^([^(]+)', title_text)
#                 if name_match:
#                     profile_info['full_name'] = name_match.group(1).strip()
            
#             logger.info(f"📊 HTML parsed: {profile_info.get('full_name', username)}")
            
#             return {
#                 'platform': 'instagram',
#                 'user_info': profile_info,
#                 'posts': [],  # HTML parsing doesn't easily get posts
#                 'scraped_at': datetime.now().isoformat(),
#                 'total_items': 0,
#                 'method': 'html_parsing',
#                 'note': 'Limited data due to Instagram restrictions'
#             }
            
#         except Exception as e:
#             logger.error(f"❌ HTML parsing failed: {e}")
#             return {'error': f'HTML parsing failed: {str(e)}'}

#     async def _scrape_instagram_alternative(self, username: str, limit: int) -> Dict:
#         """Try alternative Instagram scraping methods"""
#         try:
#             logger.info("🔄 Trying alternative methods...")
            
#             # This is a placeholder for alternative methods
#             # In practice, you might use other services or APIs
            
#             return {
#                 'platform': 'instagram',
#                 'user_info': {
#                     'username': username,
#                     'method': 'alternative',
#                     'note': 'Instagram heavily restricts automated access'
#                 },
#                 'posts': [],
#                 'scraped_at': datetime.now().isoformat(),
#                 'total_items': 0,
#                 'method': 'alternative'
#             }
            
#         except Exception as e:
#             logger.error(f"❌ Alternative methods failed: {e}")
#             return {'error': f'Alternative methods failed: {str(e)}'}

#     def test_connection(self) -> Dict:
#         """Test Instagram connection"""
#         if self.loader:
#             try:
#                 # Test with a known public profile
#                 profile = instaloader.Profile.from_username(self.loader.context, "instagram")
#                 return {'status': 'success', 'method': 'instaloader', 'message': f'Instaloader working, found profile: {profile.username}'}
#             except Exception as e:
#                 return {'status': 'error', 'method': 'instaloader', 'message': str(e)}
#         else:
#             # Test web scraping
#             try:
#                 response = self.session.get("https://www.instagram.com/instagram/", timeout=10)
#                 if response.status_code == 200:
#                     return {'status': 'success', 'method': 'web_scraping', 'message': 'Instagram web access working'}
#                 else:
#                     return {'status': 'error', 'method': 'web_scraping', 'message': f'HTTP {response.status_code}'}
#             except Exception as e:
#                 return {'status': 'error', 'method': 'web_scraping', 'message': str(e)}




# !aboveworking best 


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
import re

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    import instaloader
    INSTALOADER_AVAILABLE = True
    logger.info("✓ Instaloader available")
except ImportError:
    INSTALOADER_AVAILABLE = False
    logger.warning("⚠️ Instaloader not available - using scraper only")

try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
    logger.info("✓ BeautifulSoup available")
except ImportError:
    BS4_AVAILABLE = False
    logger.warning("⚠️ BeautifulSoup not available")

class InstagramScraper:
    def __init__(self):
        self.loader = None
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1'
        })
        
        # Try to initialize Instaloader
        if INSTALOADER_AVAILABLE:
            self._init_instaloader()
        
        logger.info("✓ Instagram scraper initialized")

    def _init_instaloader(self):
        """Initialize Instaloader"""
        try:
            self.loader = instaloader.Instaloader()
            self.loader.context.log = lambda *args, **kwargs: None  # Disable logging
            logger.info("✓ Instaloader initialized")
            return True
        except Exception as e:
            logger.error(f"✗ Instaloader initialization failed: {e}")
            self.loader = None
            return False

    async def scrape_user(self, username: str, limit: int = 50) -> Dict:
        """
        Scrape Instagram user with both API and scraper methods
        """
        logger.info(f"🔍 Starting Instagram scrape for user: {username}")
        
        # Method 1: Try Instaloader first
        if self.loader:
            logger.info("📡 Trying Instaloader method...")
            instaloader_result = await self._scrape_with_instaloader(username, limit)
            if instaloader_result and 'error' not in instaloader_result:
                logger.info("✅ Instaloader method successful")
                return instaloader_result
            else:
                logger.warning("⚠️ Instaloader method failed, trying scraper...")
        
        # Method 2: Web scraping fallback
        logger.info("🕷️ Trying web scraping method...")
        scraper_result = await self._scrape_with_web(username, limit)
        
        if scraper_result and 'error' not in scraper_result:
            logger.info("✅ Web scraping method successful")
            return scraper_result
        else:
            logger.error("❌ Both methods failed")
            return {
                'platform': 'instagram',
                'username': username,
                'error': 'Both Instaloader and scraping methods failed',
                'instaloader_error': instaloader_result.get('error') if 'instaloader_result' in locals() else 'Instaloader not available',
                'scraper_error': scraper_result.get('error') if 'scraper_result' in locals() else 'Scraper failed',
                'scraped_at': datetime.now().isoformat()
            }

    async def _scrape_with_instaloader(self, username: str, limit: int) -> Dict:
        """Scrape using Instaloader"""
        try:
            profile = instaloader.Profile.from_username(self.loader.context, username)
            
            # Get profile information
            profile_info = {
                'username': username,
                'full_name': profile.full_name,
                'biography': profile.biography,
                'followers': profile.followers,
                'followees': profile.followees,
                'posts_count': profile.mediacount,
                'is_verified': profile.is_verified,
                'is_private': profile.is_private,
                'external_url': profile.external_url,
                'profile_pic_url': profile.profile_pic_url,
                'method': 'instaloader'
            }
            
            logger.info(f"👤 Profile: {profile_info['full_name']} ({profile_info['followers']} followers)")
            
            # Get recent posts (only if public)
            posts = []
            if not profile.is_private:
                try:
                    post_count = 0
                    for post in profile.get_posts():
                        if post_count >= limit:
                            break
                        
                        # Extract hashtags and mentions
                        hashtags = []
                        mentions = []
                        
                        if post.caption:
                            hashtags = re.findall(r'#(\w+)', post.caption)
                            mentions = re.findall(r'@(\w+)', post.caption)
                        
                        post_data = {
                            'shortcode': post.shortcode,
                            'caption': post.caption if post.caption else '',
                            'likes': post.likes,
                            'comments': post.comments,
                            'date': post.date.isoformat() if post.date else None,
                            'is_video': post.is_video,
                            'url': f"https://instagram.com/p/{post.shortcode}/",
                            'hashtags': hashtags,
                            'mentions': mentions,
                            'location': post.location.name if post.location else None
                        }
                        
                        posts.append(post_data)
                        post_count += 1
                        
                    logger.info(f"📸 Collected {len(posts)} posts")
                        
                except Exception as e:
                    logger.error(f"❌ Error fetching posts: {e}")
            else:
                logger.info("🔒 Profile is private, cannot fetch posts")
            
            return {
                'platform': 'instagram',
                'user_info': profile_info,
                'posts': posts,
                'scraped_at': datetime.now().isoformat(),
                'total_items': len(posts),
                'method': 'instaloader'
            }
            
        except Exception as e:
            logger.error(f"❌ Instaloader scraping failed: {e}")
            return {'error': f'Instaloader failed: {str(e)}'}

    async def _scrape_with_web(self, username: str, limit: int) -> Dict:
        """Scrape using web scraping methods"""
        try:
            # Method 1: Try Instagram web interface
            web_result = await self._scrape_instagram_web(username, limit)
            if web_result and 'error' not in web_result:
                return web_result
            
            # Method 2: Try alternative methods
            alt_result = await self._scrape_instagram_alternative(username, limit)
            if alt_result and 'error' not in alt_result:
                return alt_result
            
            return {'error': 'All web scraping methods failed'}
            
        except Exception as e:
            logger.error(f"❌ Web scraping failed: {e}")
            return {'error': f'Web scraping failed: {str(e)}'}

    async def _scrape_instagram_web(self, username: str, limit: int) -> Dict:
        """Scrape Instagram web interface"""
        try:
            logger.info("🌐 Trying Instagram web interface...")
            
            url = f"https://www.instagram.com/{username}/"
            
            # Add Instagram-specific headers
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.9',
                'Accept-Encoding': 'gzip, deflate, br',
                'Connection': 'keep-alive',
                'Upgrade-Insecure-Requests': '1',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'none'
            }
            
            response = self.session.get(url, headers=headers, timeout=15)
            
            if response.status_code == 200:
                # Try to extract JSON data from the page
                content = response.text
                
                # Look for JSON data in script tags
                json_data = None
                
                # Pattern 1: window._sharedData
                shared_data_match = re.search(r'window\._sharedData\s*=\s*({.+?});', content)
                if shared_data_match:
                    try:
                        json_data = json.loads(shared_data_match.group(1))
                        logger.info("📊 Found _sharedData")
                    except:
                        pass
                
                # Pattern 2: Look for profile data in script tags
                if not json_data:
                    script_matches = re.findall(r'<script[^>]*>([^<]*)</script>', content)
                    for script in script_matches:
                        if 'ProfilePage' in script or 'graphql' in script:
                            try:
                                # Try to extract JSON from the script
                                json_match = re.search(r'({.*"ProfilePage".*})', script)
                                if json_match:
                                    json_data = json.loads(json_match.group(1))
                                    logger.info("📊 Found ProfilePage data")
                                    break
                            except:
                                continue
                
                if json_data:
                    return await self._parse_instagram_json(json_data, username)
                else:
                    # Fallback to HTML parsing
                    if BS4_AVAILABLE:
                        return await self._parse_instagram_html(content, username)
                    else:
                        return {'error': 'No JSON data found and BeautifulSoup not available'}
            else:
                logger.warning(f"⚠️ Instagram returned {response.status_code}")
                return {'error': f'Instagram returned {response.status_code}'}
                
        except Exception as e:
            logger.error(f"❌ Instagram web scraping failed: {e}")
            return {'error': f'Instagram web scraping failed: {str(e)}'}

    async def _parse_instagram_json(self, json_data: dict, username: str) -> Dict:
        """Parse Instagram JSON data"""
        try:
            logger.info("🔍 Parsing Instagram JSON data...")
            
            profile_info = {
                'username': username,
                'method': 'web_json'
            }
            
            posts = []
            
            # Try to find user data in various locations
            user_data = None
            
            # Look in entry_data.ProfilePage
            if 'entry_data' in json_data and 'ProfilePage' in json_data['entry_data']:
                profile_page = json_data['entry_data']['ProfilePage'][0]
                if 'graphql' in profile_page and 'user' in profile_page['graphql']:
                    user_data = profile_page['graphql']['user']
            
            # Look in other locations
            if not user_data and 'graphql' in json_data and 'user' in json_data['graphql']:
                user_data = json_data['graphql']['user']
            
            if user_data:
                profile_info.update({
                    'full_name': user_data.get('full_name', ''),
                    'biography': user_data.get('biography', ''),
                    'followers': user_data.get('edge_followed_by', {}).get('count', 0),
                    'following': user_data.get('edge_follow', {}).get('count', 0),
                    'posts_count': user_data.get('edge_owner_to_timeline_media', {}).get('count', 0),
                    'is_verified': user_data.get('is_verified', False),
                    'is_private': user_data.get('is_private', False),
                    'external_url': user_data.get('external_url', ''),
                    'profile_pic_url': user_data.get('profile_pic_url', '')
                })
                
                # Extract posts
                if 'edge_owner_to_timeline_media' in user_data:
                    media_edges = user_data['edge_owner_to_timeline_media'].get('edges', [])
                    
                    for edge in media_edges[:50]:  # Limit posts
                        node = edge.get('node', {})
                        
                        # Extract caption
                        caption = ''
                        if 'edge_media_to_caption' in node:
                            caption_edges = node['edge_media_to_caption'].get('edges', [])
                            if caption_edges:
                                caption = caption_edges[0].get('node', {}).get('text', '')
                        
                        # Extract hashtags and mentions
                        hashtags = re.findall(r'#(\w+)', caption) if caption else []
                        mentions = re.findall(r'@(\w+)', caption) if caption else []
                        
                        post_data = {
                            'shortcode': node.get('shortcode', ''),
                            'caption': caption,
                            'likes': node.get('edge_liked_by', {}).get('count', 0),
                            'comments': node.get('edge_media_to_comment', {}).get('count', 0),
                            'date': datetime.fromtimestamp(node.get('taken_at_timestamp', 0)).isoformat() if node.get('taken_at_timestamp') else None,
                            'is_video': node.get('is_video', False),
                            'url': f"https://instagram.com/p/{node.get('shortcode', '')}/",
                            'hashtags': hashtags,
                            'mentions': mentions,
                            'display_url': node.get('display_url', '')
                        }
                        
                        posts.append(post_data)
                
                logger.info(f"📊 Parsed profile: {profile_info.get('full_name')} ({len(posts)} posts)")
            
            return {
                'platform': 'instagram',
                'user_info': profile_info,
                'posts': posts,
                'scraped_at': datetime.now().isoformat(),
                'total_items': len(posts),
                'method': 'web_json'
            }
            
        except Exception as e:
            logger.error(f"❌ JSON parsing failed: {e}")
            return {'error': f'JSON parsing failed: {str(e)}'}

    async def _parse_instagram_html(self, content: str, username: str) -> Dict:
        """Parse Instagram HTML content"""
        try:
            logger.info("🕸️ Parsing Instagram HTML...")
            
            soup = BeautifulSoup(content, 'html.parser')
            
            profile_info = {
                'username': username,
                'method': 'html_parsing'
            }
            
            # Try to extract basic info from meta tags
            meta_description = soup.find('meta', {'name': 'description'})
            if meta_description:
                desc_content = meta_description.get('content', '')
                # Try to extract follower count from description
                follower_match = re.search(r'(\d+(?:,\d+)*)\s+Followers', desc_content)
                if follower_match:
                    follower_count = follower_match.group(1).replace(',', '')
                    profile_info['followers'] = int(follower_count)
            
            # Try to extract title
            title_tag = soup.find('title')
            if title_tag:
                title_text = title_tag.get_text()
                # Extract name from title
                name_match = re.search(r'^([^(]+)', title_text)
                if name_match:
                    profile_info['full_name'] = name_match.group(1).strip()
            
            logger.info(f"📊 HTML parsed: {profile_info.get('full_name', username)}")
            
            return {
                'platform': 'instagram',
                'user_info': profile_info,
                'posts': [],  # HTML parsing doesn't easily get posts
                'scraped_at': datetime.now().isoformat(),
                'total_items': 0,
                'method': 'html_parsing',
                'note': 'Limited data due to Instagram restrictions'
            }
            
        except Exception as e:
            logger.error(f"❌ HTML parsing failed: {e}")
            return {'error': f'HTML parsing failed: {str(e)}'}

    async def _scrape_instagram_alternative(self, username: str, limit: int) -> Dict:
        """Try alternative Instagram scraping methods"""
        try:
            logger.info("🔄 Trying alternative methods...")
            
            # This is a placeholder for alternative methods
            # In practice, you might use other services or APIs
            
            return {
                'platform': 'instagram',
                'user_info': {
                    'username': username,
                    'method': 'alternative',
                    'note': 'Instagram heavily restricts automated access'
                },
                'posts': [],
                'scraped_at': datetime.now().isoformat(),
                'total_items': 0,
                'method': 'alternative'
            }
            
        except Exception as e:
            logger.error(f"❌ Alternative methods failed: {e}")
            return {'error': f'Alternative methods failed: {str(e)}'}

    def test_connection(self) -> Dict:
        """Test Instagram connection"""
        if self.loader:
            try:
                # Test with a known public profile
                profile = instaloader.Profile.from_username(self.loader.context, "instagram")
                return {'status': 'success', 'method': 'instaloader', 'message': f'Instaloader working, found profile: {profile.username}'}
            except Exception as e:
                return {'status': 'error', 'method': 'instaloader', 'message': str(e)}
        else:
            # Test web scraping
            try:
                response = self.session.get("https://www.instagram.com/instagram/", timeout=10)
                if response.status_code == 200:
                    return {'status': 'success', 'method': 'web_scraping', 'message': 'Instagram web access working'}
                else:
                    return {'status': 'error', 'method': 'web_scraping', 'message': f'HTTP {response.status_code}'}
            except Exception as e:
                return {'status': 'error', 'method': 'web_scraping', 'message': str(e)}
