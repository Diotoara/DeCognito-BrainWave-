from newspaper import Article, Config
import requests
import asyncio
from typing import Dict, List
import os
from datetime import datetime, timedelta
from bs4 import BeautifulSoup

class NewsScraper:
    def __init__(self):
        self.config = Config()
        self.config.browser_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        self.config.request_timeout = 10
        
        # News API configuration
        self.news_api_key = os.getenv('NEWS_API_KEY',None)#your api key here
        self.news_api_url = "https://newsapi.org/v2/everything"
        
        # Indian news sources
        self.indian_sources = [
            'timesofindia.indiatimes.com',
            'indianexpress.com',
            'hindustantimes.com',
            'ndtv.com',
            'thehindu.com',
            'news18.com',
            'indiatoday.in',
            'firstpost.com'
        ]
    
    async def search_mentions(self, query: str, limit: int = 20) -> Dict:
        try:
            results = []
            
            # Method 1: News API (if available)
            if self.news_api_key:
                api_results = await self._search_news_api(query, limit // 2)
                results.extend(api_results)
            
            # Method 2: Direct source scraping
            scrape_results = await self._scrape_news_sources(query, limit // 2)
            results.extend(scrape_results)
            
            # Method 3: Google News scraping (fallback)
            if len(results) < limit:
                google_results = await self._scrape_google_news(query, limit - len(results))
                results.extend(google_results)
            
            return {
                'platform': 'news',
                'query': query,
                'articles': results[:limit],
                'total_found': len(results),
                'scraped_at': datetime.now().isoformat(),
                'sources_checked': len(self.indian_sources)
            }
            
        except Exception as e:
            return {
                'platform': 'news',
                'query': query,
                'error': str(e),
                'scraped_at': datetime.now().isoformat()
            }
    
    async def _search_news_api(self, query: str, limit: int) -> List[Dict]:
        """Search using News API"""
        try:
            if not self.news_api_key:
                return []
            
            # Calculate date range (last 30 days)
            to_date = datetime.now()
            from_date = to_date - timedelta(days=30)
            
            params = {
                'q': query,
                'apiKey': self.news_api_key,
                'language': 'en',
                'sortBy': 'relevancy',
                'pageSize': limit,
                'from': from_date.strftime('%Y-%m-%d'),
                'to': to_date.strftime('%Y-%m-%d')
            }
            
            response = requests.get(self.news_api_url, params=params, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                articles = []
                
                for article in data.get('articles', []):
                    articles.append({
                        'title': article.get('title', ''),
                        'description': article.get('description', ''),
                        'url': article.get('url', ''),
                        'source': article.get('source', {}).get('name', ''),
                        'published_at': article.get('publishedAt', ''),
                        'author': article.get('author', ''),
                        'method': 'news_api'
                    })
                
                return articles
            else:
                print(f"News API error: {response.status_code}")
                return []
                
        except Exception as e:
            print(f"News API search failed: {e}")
            return []
    
    async def _scrape_news_sources(self, query: str, limit: int) -> List[Dict]:
        """Scrape Indian news sources directly"""
        articles = []
        
        for source in self.indian_sources[:5]:  # Limit to first 5 sources
            try:
                # Search on the source website
                search_url = f"https://{source}/search?q={query}"
                
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
                }
                
                response = requests.get(search_url, headers=headers, timeout=10)
                
                if response.status_code == 200:
                    soup = BeautifulSoup(response.content, 'html.parser')
                    
                    # Generic article link extraction
                    links = soup.find_all('a', href=True)
                    article_links = []
                    
                    for link in links:
                        href = link.get('href', '')
                        if any(keyword in href.lower() for keyword in ['article', 'news', 'story']) and source in href:
                            article_links.append(href)
                    
                    # Process first few article links
                    for article_url in article_links[:3]:
                        try:
                            article_data = await self._extract_article_content(article_url)
                            if article_data and query.lower() in article_data.get('content', '').lower():
                                article_data['source'] = source
                                article_data['method'] = 'direct_scrape'
                                articles.append(article_data)
                                
                                if len(articles) >= limit:
                                    return articles
                        except:
                            continue
                            
            except Exception as e:
                print(f"Error scraping {source}: {e}")
                continue
        
        return articles
    
    async def _scrape_google_news(self, query: str, limit: int) -> List[Dict]:
        """Scrape Google News as fallback"""
        try:
            search_url = f"https://news.google.com/search?q={query}&hl=en-IN&gl=IN&ceid=IN:en"
            
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            
            response = requests.get(search_url, headers=headers, timeout=10)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')
                articles = []
                
                # Extract article information from Google News
                article_elements = soup.find_all('article')[:limit]
                
                for element in article_elements:
                    try:
                        title_elem = element.find('h3') or element.find('h4')
                        title = title_elem.get_text(strip=True) if title_elem else ''
                        
                        link_elem = element.find('a', href=True)
                        link = link_elem.get('href', '') if link_elem else ''
                        
                        if title and link:
                            articles.append({
                                'title': title,
                                'url': f"https://news.google.com{link}" if link.startswith('./') else link,
                                'source': 'Google News',
                                'method': 'google_news_scrape',
                                'scraped_at': datetime.now().isoformat()
                            })
                    except:
                        continue
                
                return articles
            else:
                return []
                
        except Exception as e:
            print(f"Google News scraping failed: {e}")
            return []
    
    async def _extract_article_content(self, url: str) -> Dict:
        """Extract content from a news article URL"""
        try:
            article = Article(url, config=self.config)
            article.download()
            article.parse()
            
            return {
                'title': article.title,
                'content': article.text[:1000],  # Limit content length
                'url': url,
                'published_date': article.publish_date.isoformat() if article.publish_date else None,
                'authors': article.authors,
                'summary': article.summary[:200] if article.summary else '',
                'extracted_at': datetime.now().isoformat()
            }
            
        except Exception as e:
            print(f"Article extraction failed for {url}: {e}")
            return None
    
    async def analyze_news_sentiment(self, articles: List[Dict]) -> Dict:
        """Analyze sentiment of news articles about the target"""
        try:
            positive_articles = 0
            negative_articles = 0
            neutral_articles = 0
            
            # Simple keyword-based sentiment analysis
            positive_keywords = ['success', 'achievement', 'award', 'positive', 'good', 'excellent', 'outstanding']
            negative_keywords = ['scandal', 'controversy', 'arrest', 'fraud', 'negative', 'bad', 'terrible', 'criminal']
            
            for article in articles:
                content = (article.get('title', '') + ' ' + article.get('content', '')).lower()
                
                positive_score = sum(1 for keyword in positive_keywords if keyword in content)
                negative_score = sum(1 for keyword in negative_keywords if keyword in content)
                
                if positive_score > negative_score:
                    positive_articles += 1
                elif negative_score > positive_score:
                    negative_articles += 1
                else:
                    neutral_articles += 1
            
            total = len(articles)
            
            return {
                'total_articles': total,
                'positive_articles': positive_articles,
                'negative_articles': negative_articles,
                'neutral_articles': neutral_articles,
                'positive_percentage': (positive_articles / total) * 100 if total > 0 else 0,
                'negative_percentage': (negative_articles / total) * 100 if total > 0 else 0,
                'overall_sentiment': 'POSITIVE' if positive_articles > negative_articles else 'NEGATIVE' if negative_articles > positive_articles else 'NEUTRAL'
            }
            
        except Exception as e:
            return {'error': f'News sentiment analysis failed: {str(e)}'}
