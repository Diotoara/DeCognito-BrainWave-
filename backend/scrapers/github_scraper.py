# from github import Github
# import asyncio
# from typing import Dict, List
# import os
# from datetime import datetime
# import requests
# from bs4 import BeautifulSoup

# class GitHubScraper:
#     def __init__(self):
#         github_token = os.getenv('GITHUB_TOKEN', '')
#         self.github = Github(github_token) if github_token else Github()
#         self.session = requests.Session()
    
#     async def scrape_user(self, username: str) -> Dict:
#         try:
#             # Method 1: GitHub API (primary)
#             try:
#                 user = self.github.get_user(username)
                
#                 user_info = {
#                     'username': username,
#                     'name': user.name,
#                     'bio': user.bio,
#                     'company': user.company,
#                     'location': user.location,
#                     'email': user.email,
#                     'blog': user.blog,
#                     'followers': user.followers,
#                     'following': user.following,
#                     'public_repos': user.public_repos,
#                     'created_at': user.created_at.isoformat() if user.created_at else None,
#                     'updated_at': user.updated_at.isoformat() if user.updated_at else None
#                 }
                
#                 # Get repositories
#                 repos = []
#                 for repo in user.get_repos()[:50]:  # Limit to 50 repos
#                     repos.append({
#                         'name': repo.name,
#                         'description': repo.description,
#                         'language': repo.language,
#                         'stars': repo.stargazers_count,
#                         'forks': repo.forks_count,
#                         'created_at': repo.created_at.isoformat() if repo.created_at else None,
#                         'updated_at': repo.updated_at.isoformat() if repo.updated_at else None,
#                         'url': repo.html_url
#                     })
                
#                 # Get recent activity (commits, issues, etc.)
#                 activity = []
#                 try:
#                     events = user.get_events()[:20]  # Last 20 events
#                     for event in events:
#                         activity.append({
#                             'type': event.type,
#                             'repo': event.repo.name if event.repo else None,
#                             'created_at': event.created_at.isoformat() if event.created_at else None
#                         })
#                 except Exception as e:
#                     print(f"Error fetching activity: {e}")
                
#                 return {
#                     'platform': 'github',
#                     'user_info': user_info,
#                     'repositories': repos,
#                     'activity': activity,
#                     'scraped_at': datetime.now().isoformat()
#                 }
                
#             except Exception as e:
#                 print(f"GitHub API failed: {e}")
#                 # Fallback to web scraping
#                 return await self._scrape_github_web(username)
                
#         except Exception as e:
#             return {
#                 'platform': 'github',
#                 'error': str(e),
#                 'scraped_at': datetime.now().isoformat()
#             }
    
#     async def _scrape_github_web(self, username: str) -> Dict:
#         """Fallback web scraping method"""
#         try:
#             url = f"https://github.com/{username}"
#             response = self.session.get(url)
#             soup = BeautifulSoup(response.content, 'html.parser')
            
#             # Extract basic profile info
#             name_element = soup.find('span', {'class': 'p-name'})
#             bio_element = soup.find('div', {'class': 'p-note'})
            
#             user_info = {
#                 'username': username,
#                 'name': name_element.get_text(strip=True) if name_element else None,
#                 'bio': bio_element.get_text(strip=True) if bio_element else None,
#                 'scraped_method': 'web'
#             }
            
#             # Extract repository names
#             repos = []
#             repo_elements = soup.find_all('a', {'itemprop': 'name codeRepository'})
#             for repo_element in repo_elements[:20]:
#                 repos.append({
#                     'name': repo_element.get_text(strip=True),
#                     'url': f"https://github.com{repo_element.get('href')}"
#                 })
            
#             return {
#                 'platform': 'github',
#                 'user_info': user_info,
#                 'repositories': repos,
#                 'scraped_at': datetime.now().isoformat()
#             }
            
#         except Exception as e:
#             return {
#                 'platform': 'github',
#                 'error': str(e),
#                 'scraped_at': datetime.now().isoformat()
#             }


# new

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
    from github import Github
    PYGITHUB_AVAILABLE = True
    logger.info("✓ PyGithub available")
except ImportError:
    PYGITHUB_AVAILABLE = False
    logger.warning("⚠️ PyGithub not available - using scraper only")

try:
    from bs4 import BeautifulSoup
    BS4_AVAILABLE = True
    logger.info("✓ BeautifulSoup available")
except ImportError:
    BS4_AVAILABLE = False
    logger.warning("⚠️ BeautifulSoup not available")

class GitHubScraper:
    def __init__(self):
        self.github_api = None
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
            'Accept': 'application/vnd.github.v3+json'
        })
        
        # Try to initialize GitHub API
        if PYGITHUB_AVAILABLE:
            self._init_github_api()
        
        logger.info("✓ GitHub scraper initialized")

    def _init_github_api(self):
        """Initialize GitHub API if token is available"""
        try:
            github_token = os.getenv('GITHUB_TOKEN')
            
            if github_token:
                self.github_api = Github(github_token.strip('"\''))
                
                # Test the API
                try:
                    user = self.github_api.get_user()
                    logger.info(f"✓ GitHub API initialized for user: {user.login}")
                    return True
                except Exception as e:
                    logger.warning(f"⚠️ GitHub API test failed: {e}")
                    # Try without authentication
                    self.github_api = Github()
                    test_user = self.github_api.get_user("octocat")
                    logger.info("✓ GitHub API initialized without authentication")
                    return True
            else:
                logger.info("ℹ️ No GitHub token found, using unauthenticated API")
                self.github_api = Github()
                return True
                
        except Exception as e:
            logger.error(f"✗ GitHub API initialization failed: {e}")
            self.github_api = None
            return False

    async def scrape_user(self, username: str, limit: int = 50) -> Dict:
        """
        Scrape GitHub user with both API and scraper methods
        """
        logger.info(f"🔍 Starting GitHub scrape for user: {username}")
        
        # Method 1: Try GitHub API first
        if self.github_api:
            logger.info("📡 Trying GitHub API method...")
            api_result = await self._scrape_with_api(username, limit)
            if api_result and 'error' not in api_result:
                logger.info("✅ GitHub API method successful")
                return api_result
            else:
                logger.warning("⚠️ GitHub API method failed, trying scraper...")
        
        # Method 2: Web scraping fallback
        logger.info("🕷️ Trying web scraping method...")
        scraper_result = await self._scrape_with_web(username, limit)
        
        if scraper_result and 'error' not in scraper_result:
            logger.info("✅ Web scraping method successful")
            return scraper_result
        else:
            logger.error("❌ Both methods failed")
            return {
                'platform': 'github',
                'username': username,
                'error': 'Both API and scraping methods failed',
                'api_error': api_result.get('error') if 'api_result' in locals() else 'API not available',
                'scraper_error': scraper_result.get('error') if 'scraper_result' in locals() else 'Scraper failed',
                'scraped_at': datetime.now().isoformat()
            }

    async def _scrape_with_api(self, username: str, limit: int) -> Dict:
        """Scrape using GitHub API"""
        try:
            user = self.github_api.get_user(username)
            
            # Get user info
            user_info = {
                'username': username,
                'name': user.name,
                'bio': user.bio,
                'company': user.company,
                'location': user.location,
                'email': user.email,
                'blog': user.blog,
                'followers': user.followers,
                'following': user.following,
                'public_repos': user.public_repos,
                'created_at': user.created_at.isoformat() if user.created_at else None,
                'updated_at': user.updated_at.isoformat() if user.updated_at else None,
                'method': 'api'
            }
            
            logger.info(f"👤 User: {user_info['name']} ({user_info['public_repos']} repos)")
            
            # Get repositories
            repositories = []
            try:
                repo_count = 0
                for repo in user.get_repos():
                    if repo_count >= limit:
                        break
                        
                    repo_data = {
                        'name': repo.name,
                        'description': repo.description,
                        'language': repo.language,
                        'stars': repo.stargazers_count,
                        'forks': repo.forks_count,
                        'created_at': repo.created_at.isoformat() if repo.created_at else None,
                        'updated_at': repo.updated_at.isoformat() if repo.updated_at else None,
                        'url': repo.html_url,
                        'size': repo.size,
                        'default_branch': repo.default_branch
                    }
                    
                    repositories.append(repo_data)
                    repo_count += 1
                    
                logger.info(f"📁 Collected {len(repositories)} repositories")
                    
            except Exception as e:
                logger.error(f"❌ Failed to fetch repositories: {e}")
            
            # Get recent activity/events
            activity = []
            try:
                event_count = 0
                for event in user.get_events():
                    if event_count >= 20:  # Limit events
                        break
                        
                    activity_data = {
                        'type': event.type,
                        'repo': event.repo.name if event.repo else None,
                        'created_at': event.created_at.isoformat() if event.created_at else None,
                        'public': event.public
                    }
                    
                    activity.append(activity_data)
                    event_count += 1
                    
                logger.info(f"📊 Collected {len(activity)} activity events")
                    
            except Exception as e:
                logger.warning(f"⚠️ Failed to fetch activity: {e}")
            
            # Get commit messages from recent repos for content analysis
            commits = []
            try:
                for repo_data in repositories[:5]:  # Check top 5 repos
                    try:
                        repo = self.github_api.get_repo(f"{username}/{repo_data['name']}")
                        commit_count = 0
                        
                        for commit in repo.get_commits():
                            if commit_count >= 10:  # Limit commits per repo
                                break
                                
                            if commit.commit.message:
                                commit_data = {
                                    'message': commit.commit.message,
                                    'repo': repo_data['name'],
                                    'date': commit.commit.author.date.isoformat() if commit.commit.author.date else None,
                                    'sha': commit.sha[:8]
                                }
                                
                                commits.append(commit_data)
                                commit_count += 1
                                
                    except Exception as e:
                        logger.warning(f"⚠️ Failed to get commits for {repo_data['name']}: {e}")
                        continue
                        
                logger.info(f"💬 Collected {len(commits)} commit messages")
                        
            except Exception as e:
                logger.warning(f"⚠️ Failed to fetch commits: {e}")
            
            return {
                'platform': 'github',
                'user_info': user_info,
                'repositories': repositories,
                'activity': activity,
                'commits': commits,
                'scraped_at': datetime.now().isoformat(),
                'total_items': len(repositories) + len(commits),
                'method': 'api'
            }
            
        except Exception as e:
            logger.error(f"❌ GitHub API scraping failed: {e}")
            return {'error': f'GitHub API failed: {str(e)}'}

    async def _scrape_with_web(self, username: str, limit: int) -> Dict:
        """Scrape using web scraping"""
        try:
            # Method 1: Try GitHub REST API without authentication
            api_result = await self._scrape_github_rest_api(username, limit)
            if api_result and 'error' not in api_result:
                return api_result
            
            # Method 2: Try HTML scraping
            if BS4_AVAILABLE:
                html_result = await self._scrape_github_html(username, limit)
                if html_result and 'error' not in html_result:
                    return html_result
            
            return {'error': 'All web scraping methods failed'}
            
        except Exception as e:
            logger.error(f"❌ Web scraping failed: {e}")
            return {'error': f'Web scraping failed: {str(e)}'}

    async def _scrape_github_rest_api(self, username: str, limit: int) -> Dict:
        """Scrape using GitHub REST API without authentication"""
        try:
            logger.info("🔗 Trying GitHub REST API...")
            
            # Get user info
            user_url = f"https://api.github.com/users/{username}"
            user_response = self.session.get(user_url, timeout=10)
            
            if user_response.status_code != 200:
                return {'error': f'User API returned {user_response.status_code}'}
            
            user_data = user_response.json()
            
            user_info = {
                'username': username,
                'name': user_data.get('name'),
                'bio': user_data.get('bio'),
                'company': user_data.get('company'),
                'location': user_data.get('location'),
                'email': user_data.get('email'),
                'blog': user_data.get('blog'),
                'followers': user_data.get('followers', 0),
                'following': user_data.get('following', 0),
                'public_repos': user_data.get('public_repos', 0),
                'created_at': user_data.get('created_at'),
                'updated_at': user_data.get('updated_at'),
                'method': 'rest_api'
            }
            
            logger.info(f"👤 User: {user_info['name']} ({user_info['public_repos']} repos)")
            
            # Get repositories
            repos_url = f"https://api.github.com/users/{username}/repos?per_page={limit}&sort=updated"
            repos_response = self.session.get(repos_url, timeout=10)
            
            repositories = []
            if repos_response.status_code == 200:
                repos_data = repos_response.json()
                
                for repo in repos_data:
                    repo_data = {
                        'name': repo.get('name'),
                        'description': repo.get('description'),
                        'language': repo.get('language'),
                        'stars': repo.get('stargazers_count', 0),
                        'forks': repo.get('forks_count', 0),
                        'created_at': repo.get('created_at'),
                        'updated_at': repo.get('updated_at'),
                        'url': repo.get('html_url'),
                        'size': repo.get('size', 0),
                        'default_branch': repo.get('default_branch')
                    }
                    
                    repositories.append(repo_data)
                    
                logger.info(f"📁 Collected {len(repositories)} repositories")
            
            # Get recent commits from top repos
            commits = []
            for repo in repositories[:3]:  # Top 3 repos
                try:
                    commits_url = f"https://api.github.com/repos/{username}/{repo['name']}/commits?per_page=5"
                    commits_response = self.session.get(commits_url, timeout=10)
                    
                    if commits_response.status_code == 200:
                        commits_data = commits_response.json()
                        
                        for commit in commits_data:
                            if commit.get('commit', {}).get('message'):
                                commit_data = {
                                    'message': commit['commit']['message'],
                                    'repo': repo['name'],
                                    'date': commit['commit']['author']['date'],
                                    'sha': commit['sha'][:8]
                                }
                                
                                commits.append(commit_data)
                                
                except Exception as e:
                    logger.warning(f"⚠️ Failed to get commits for {repo['name']}: {e}")
                    continue
            
            logger.info(f"💬 Collected {len(commits)} commit messages")
            
            return {
                'platform': 'github',
                'user_info': user_info,
                'repositories': repositories,
                'commits': commits,
                'scraped_at': datetime.now().isoformat(),
                'total_items': len(repositories) + len(commits),
                'method': 'rest_api'
            }
            
        except Exception as e:
            logger.error(f"❌ REST API scraping failed: {e}")
            return {'error': f'REST API failed: {str(e)}'}

    async def _scrape_github_html(self, username: str, limit: int) -> Dict:
        """Scrape using HTML parsing"""
        try:
            logger.info("🕸️ Trying GitHub HTML scraping...")
            
            url = f"https://github.com/{username}"
            response = self.session.get(url, timeout=10)
            
            if response.status_code != 200:
                return {'error': f'GitHub page returned {response.status_code}'}
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # Extract user info
            user_info = {
                'username': username,
                'method': 'html_scraping'
            }
            
            # Try to get name
            name_elem = soup.find('span', {'class': 'p-name'})
            if name_elem:
                user_info['name'] = name_elem.get_text(strip=True)
            
            # Try to get bio
            bio_elem = soup.find('div', {'class': 'p-note'})
            if bio_elem:
                user_info['bio'] = bio_elem.get_text(strip=True)
            
            # Get repositories from the page
            repositories = []
            repo_elements = soup.find_all('a', {'itemprop': 'name codeRepository'})
            
            for repo_elem in repo_elements[:limit]:
                repo_name = repo_elem.get_text(strip=True)
                repo_url = f"https://github.com{repo_elem.get('href', '')}"
                
                repositories.append({
                    'name': repo_name,
                    'url': repo_url,
                    'method': 'html_scraping'
                })
            
            logger.info(f"📁 Collected {len(repositories)} repositories from HTML")
            
            return {
                'platform': 'github',
                'user_info': user_info,
                'repositories': repositories,
                'scraped_at': datetime.now().isoformat(),
                'total_items': len(repositories),
                'method': 'html_scraping'
            }
            
        except Exception as e:
            logger.error(f"❌ HTML scraping failed: {e}")
            return {'error': f'HTML scraping failed: {str(e)}'}

    def test_connection(self) -> Dict:
        """Test GitHub connection"""
        if self.github_api:
            try:
                user = self.github_api.get_user("octocat")
                return {'status': 'success', 'method': 'api', 'message': f'GitHub API working, user: {user.login}'}
            except Exception as e:
                return {'status': 'error', 'method': 'api', 'message': str(e)}
        else:
            # Test REST API
            try:
                response = self.session.get("https://api.github.com/users/octocat", timeout=5)
                if response.status_code == 200:
                    return {'status': 'success', 'method': 'rest_api', 'message': 'GitHub REST API working'}
                else:
                    return {'status': 'error', 'method': 'rest_api', 'message': f'HTTP {response.status_code}'}
            except Exception as e:
                return {'status': 'error', 'method': 'rest_api', 'message': str(e)}
