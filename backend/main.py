# import os
# import certifi
# import ssl

# # Set SSL certificates path
# os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
# os.environ['SSL_CERT_FILE'] = certifi.where()

# # Configure default SSL context
# ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

# # Suppress TensorFlow warnings
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
# os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# # Fix fontconfig for WeasyPrint
# os.makedirs('C:/fonts', exist_ok=True)
# with open('C:/fonts/fonts.conf', 'w') as f:
#     f.write('<?xml version="1.0"?><fontconfig><dir>C:\\Windows\\Fonts</dir></fontconfig>')
# os.environ['FONTCONFIG_FILE'] = 'C:/fonts/fonts.conf'


# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from typing import List, Optional
# import asyncio
# import os
# from datetime import datetime

# from scrapers.reddit_scraper import RedditScraper
# from scrapers.twitter_scraper import TwitterScraper
# from scrapers.github_scraper import GitHubScraper
# from scrapers.instagram_scraper import InstagramScraper
# from scrapers.news_scraper import NewsScraper
# from ai_models.sentiment_model import SentimentAnalyzer
# from ai_models.ner_model import NERAnalyzer
# from ai_models.toxicity_model import ToxicityAnalyzer
# from ai_models.summary_gemini import GeminiSummarizer
# from analysis.report_generator import ReportGenerator
# from database.supabase_client import SupabaseClient

# app = FastAPI(title="OSINT Analysis API", version="1.0.0")

# # CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class AnalysisRequest(BaseModel):
#     investigation_id: str
#     username: str
#     platforms: List[str]
#     ai_models: List[str]
#     export_formats: List[str]

# class AnalysisResponse(BaseModel):
#     investigation_id: str
#     status: str
#     results: dict
#     export_urls: List[str]

# # Initialize components
# reddit_scraper = RedditScraper()
# twitter_scraper = TwitterScraper()
# github_scraper = GitHubScraper()
# instagram_scraper = InstagramScraper()
# news_scraper = NewsScraper()

# sentiment_analyzer = SentimentAnalyzer()
# ner_analyzer = NERAnalyzer()
# toxicity_analyzer = ToxicityAnalyzer()
# gemini_summarizer = GeminiSummarizer()

# report_generator = ReportGenerator()
# db_client = SupabaseClient()

# @app.get("/")
# async def root():
#     return {"message": "OSINT Analysis API is running"}

# @app.post("/analyze", response_model=AnalysisResponse)
# async def analyze_target(request: AnalysisRequest):
#     try:
#         results = {}
#         all_content = []
        
#         # Data Collection Phase
#         for platform in request.platforms:
#             platform_data = {}
            
#             if platform == "reddit":
#                 platform_data = await reddit_scraper.scrape_user(request.username)
#             elif platform == "twitter":
#                 platform_data = await twitter_scraper.scrape_user(request.username)
#             elif platform == "github":
#                 platform_data = await github_scraper.scrape_user(request.username)
#             elif platform == "instagram":
#                 platform_data = await instagram_scraper.scrape_user(request.username)
#             elif platform == "news":
#                 platform_data = await news_scraper.search_mentions(request.username)
            
#             results[platform] = platform_data
            
#             # Collect all text content for AI analysis
#             if 'posts' in platform_data:
#                 all_content.extend(platform_data['posts'])
#             if 'comments' in platform_data:
#                 all_content.extend(platform_data['comments'])
        
#         # AI Analysis Phase
#         ai_results = {}
        
#         if "sentiment" in request.ai_models:
#             ai_results['sentiment'] = await sentiment_analyzer.analyze_batch(all_content)
        
#         if "ner" in request.ai_models:
#             ai_results['entities'] = await ner_analyzer.extract_entities_batch(all_content)
        
#         if "toxicity" in request.ai_models:
#             ai_results['toxicity'] = await toxicity_analyzer.analyze_batch(all_content)
        
#         if "summary" in request.ai_models:
#             combined_text = " ".join(all_content[:1000])  # Limit for API
#             ai_results['summary'] = await gemini_summarizer.summarize(combined_text)
        
#         # Store results in database
#         await db_client.store_results(
#             investigation_id=request.investigation_id,
#             platform_results=results,
#             ai_results=ai_results
#         )
        
#         # Generate exports
#         export_urls = []
#         if "csv" in request.export_formats:
#             csv_url = await report_generator.generate_csv(request.investigation_id, results, ai_results)
#             export_urls.append(csv_url)
        
#         if "pdf" in request.export_formats:
#             pdf_url = await report_generator.generate_pdf(request.investigation_id, results, ai_results)
#             export_urls.append(pdf_url)
        
#         if "json" in request.export_formats:
#             json_url = await report_generator.generate_json(request.investigation_id, results, ai_results)
#             export_urls.append(json_url)
        
#         return AnalysisResponse(
#             investigation_id=request.investigation_id,
#             status="completed",
#             results={**results, "ai_analysis": ai_results},
#             export_urls=export_urls
#         )
        
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

# @app.get("/health")
# async def health_check():
#     return {"status": "healthy", "timestamp": datetime.now().isoformat()}

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="0.0.0.0", port=8000)



# new !

# from dotenv import load_dotenv
# load_dotenv()


# import os
# import certifi
# import ssl

# # Set SSL certificates path
# os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
# os.environ['SSL_CERT_FILE'] = certifi.where()

# # Configure default SSL context
# ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

# # Suppress TensorFlow warnings
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
# os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# # Fix fontconfig for WeasyPrint
# os.makedirs('C:/fonts', exist_ok=True)
# with open('C:/fonts/fonts.conf', 'w') as f:
#     f.write('<?xml version="1.0"?><fontconfig><dir>C:\\Windows\\Fonts</dir></fontconfig>')
# os.environ['FONTCONFIG_FILE'] = 'C:/fonts/fonts.conf'

# from fastapi import FastAPI, HTTPException
# from fastapi.middleware.cors import CORSMiddleware
# from pydantic import BaseModel
# from typing import List, Optional
# import asyncio
# import os
# from datetime import datetime

# from scrapers.reddit_scraper import RedditScraper
# from scrapers.twitter_scraper import TwitterScraper
# from scrapers.github_scraper import GitHubScraper
# from scrapers.instagram_scraper import InstagramScraper
# from scrapers.news_scraper import NewsScraper
# from ai_models.sentiment_model import SentimentAnalyzer
# from ai_models.ner_model import NERAnalyzer
# from ai_models.toxicity_model import ToxicityAnalyzer
# from ai_models.summary_gemini import GeminiSummarizer
# from analysis.report_generator import ReportGenerator
# from database.supabase_client import SupabaseClient

# app = FastAPI(title="OSINT Analysis API", version="1.0.0")

# # CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class AnalysisRequest(BaseModel):
#     investigation_id: str
#     username: str
#     platforms: List[str]
#     ai_models: List[str]
#     export_formats: List[str]

# class AnalysisResponse(BaseModel):
#     investigation_id: str
#     status: str
#     results: dict
#     export_urls: List[str]

# # Initialize components
# print("Initializing scrapers...")
# reddit_scraper = RedditScraper()
# twitter_scraper = TwitterScraper()
# github_scraper = GitHubScraper()
# instagram_scraper = InstagramScraper()
# news_scraper = NewsScraper()

# print("Initializing AI models...")
# sentiment_analyzer = SentimentAnalyzer()
# ner_analyzer = NERAnalyzer()
# toxicity_analyzer = ToxicityAnalyzer()
# gemini_summarizer = GeminiSummarizer()

# print("Initializing report generator...")
# report_generator = ReportGenerator()
# db_client = SupabaseClient()

# print("OSINT API initialized successfully!")

# @app.get("/")
# async def root():
#     return {"message": "OSINT Analysis API is running", "status": "healthy"}

# @app.post("/analyze", response_model=AnalysisResponse)
# async def analyze_target(request: AnalysisRequest):
#     try:
#         print(f"Starting analysis for user: {request.username}")
#         print(f"Platforms: {request.platforms}")
#         print(f"AI Models: {request.ai_models}")
        
#         results = {}
#         all_content = []
        
#         # Data Collection Phase
#         for platform in request.platforms:
#             print(f"Scraping {platform}...")
#             platform_data = {}
            
#             try:
#                 if platform == "reddit":
#                     platform_data = await reddit_scraper.scrape_user(request.username)
#                 elif platform == "twitter":
#                     platform_data = await twitter_scraper.scrape_user(request.username)
#                 elif platform == "github":
#                     platform_data = await github_scraper.scrape_user(request.username)
#                 elif platform == "instagram":
#                     platform_data = await instagram_scraper.scrape_user(request.username)
#                 elif platform == "news":
#                     platform_data = await news_scraper.search_mentions(request.username)
                
#                 results[platform] = platform_data
#                 print(f"✓ {platform} scraping completed")
                
#                 # Collect text content for AI analysis
#                 if isinstance(platform_data, dict) and 'error' not in platform_data:
#                     if 'posts' in platform_data:
#                         for post in platform_data['posts']:
#                             content = post.get('content', post.get('title', post.get('body', post.get('selftext', ''))))
#                             if content:
#                                 all_content.append(content)
                    
#                     if 'comments' in platform_data:
#                         for comment in platform_data['comments']:
#                             content = comment.get('content', comment.get('body', ''))
#                             if content:
#                                 all_content.append(content)
                    
#                     if 'tweets' in platform_data:
#                         for tweet in platform_data['tweets']:
#                             content = tweet.get('content', '')
#                             if content:
#                                 all_content.append(content)
                
#             except Exception as e:
#                 print(f"✗ {platform} scraping failed: {str(e)}")
#                 results[platform] = {'error': str(e), 'platform': platform}
        
#         print(f"Collected {len(all_content)} content items for AI analysis")
        
#         # AI Analysis Phase
#         ai_results = {}
        
#         if all_content:
#             if "sentiment" in request.ai_models:
#                 print("Running sentiment analysis...")
#                 try:
#                     ai_results['sentiment'] = await sentiment_analyzer.analyze_batch(all_content)
#                     print("✓ Sentiment analysis completed")
#                 except Exception as e:
#                     print(f"✗ Sentiment analysis failed: {str(e)}")
#                     ai_results['sentiment'] = {'error': str(e)}
            
#             if "ner" in request.ai_models:
#                 print("Running NER analysis...")
#                 try:
#                     ai_results['entities'] = await ner_analyzer.extract_entities_batch(all_content)
#                     print("✓ NER analysis completed")
#                 except Exception as e:
#                     print(f"✗ NER analysis failed: {str(e)}")
#                     ai_results['entities'] = {'error': str(e)}
            
#             if "toxicity" in request.ai_models:
#                 print("Running toxicity analysis...")
#                 try:
#                     ai_results['toxicity'] = await toxicity_analyzer.analyze_batch(all_content)
#                     print("✓ Toxicity analysis completed")
#                 except Exception as e:
#                     print(f"✗ Toxicity analysis failed: {str(e)}")
#                     ai_results['toxicity'] = {'error': str(e)}
            
#             if "summary" in request.ai_models:
#                 print("Running summarization...")
#                 try:
#                     combined_text = " ".join(all_content[:1000])  # Limit for API
#                     ai_results['summary'] = await gemini_summarizer.summarize(combined_text)
#                     print("✓ Summarization completed")
#                 except Exception as e:
#                     print(f"✗ Summarization failed: {str(e)}")
#                     ai_results['summary'] = {'error': str(e)}
#         else:
#             print("No content found for AI analysis")
        
#         # Generate exports
#         export_urls = []
#         try:
#             if "csv" in request.export_formats:
#                 csv_url = await report_generator.generate_csv(request.investigation_id, results, ai_results)
#                 if csv_url:
#                     export_urls.append(csv_url)
            
#             if "pdf" in request.export_formats:
#                 pdf_url = await report_generator.generate_pdf(request.investigation_id, results, ai_results)
#                 if pdf_url:
#                     export_urls.append(pdf_url)
            
#             if "json" in request.export_formats:
#                 json_url = await report_generator.generate_json(request.investigation_id, results, ai_results)
#                 if json_url:
#                     export_urls.append(json_url)
#         except Exception as e:
#             print(f"Export generation failed: {str(e)}")
        
#         print("Analysis completed successfully!")
        
#         return AnalysisResponse(
#             investigation_id=request.investigation_id,
#             status="completed",
#             results={**results, "ai_analysis": ai_results},
#             export_urls=export_urls
#         )
        
#     except Exception as e:
#         print(f"Analysis failed: {str(e)}")
#         raise HTTPException(status_code=500, detail=f"Analysis failed: {str(e)}")

# @app.get("/health")
# async def health_check():
#     return {"status": "healthy", "timestamp": datetime.now().isoformat()}

# if __name__ == "__main__":
#     import uvicorn
#     print("Starting OSINT API server...")
#     uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)


# new 111

# from dotenv import load_dotenv
# load_dotenv()
# import os
# import sys
# import certifi
# import ssl
# import logging
# from pathlib import Path

# # Configure logging first
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# )
# logger = logging.getLogger(__name__)

# # Set SSL certificates path
# os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
# os.environ['SSL_CERT_FILE'] = certifi.where()

# # Configure default SSL context
# ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

# # Suppress TensorFlow warnings
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
# os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# # Fix fontconfig for WeasyPrint (Windows)
# if os.name == 'nt':  # Windows
#     fonts_dir = Path('C:/fonts')
#     fonts_dir.mkdir(exist_ok=True)
#     fonts_conf = fonts_dir / 'fonts.conf'
#     with open(fonts_conf, 'w') as f:
#         f.write('<?xml version="1.0"?><fontconfig><dir>C:\\Windows\\Fonts</dir></fontconfig>')
#     os.environ['FONTCONFIG_FILE'] = str(fonts_conf)

# from fastapi import FastAPI, HTTPException, Request
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel, ValidationError
# from typing import List, Optional
# import asyncio
# import traceback
# from datetime import datetime

# # Import modules with error handling
# modules_loaded = {}

# def safe_import(module_name, class_name):
#     try:
#         module = __import__(module_name, fromlist=[class_name])
#         cls = getattr(module, class_name)
#         modules_loaded[class_name] = True
#         logger.info(f"✓ Successfully imported {class_name}")
#         return cls
#     except Exception as e:
#         logger.error(f"✗ Failed to import {class_name}: {str(e)}")
#         modules_loaded[class_name] = False
#         return None

# # Import all modules
# RedditScraper = safe_import('scrapers.reddit_scraper', 'RedditScraper')
# TwitterScraper = safe_import('scrapers.twitter_scraper', 'TwitterScraper')
# GitHubScraper = safe_import('scrapers.github_scraper', 'GitHubScraper')
# InstagramScraper = safe_import('scrapers.instagram_scraper', 'InstagramScraper')
# NewsScraper = safe_import('scrapers.news_scraper', 'NewsScraper')

# SentimentAnalyzer = safe_import('ai_models.sentiment_model', 'SentimentAnalyzer')
# NERAnalyzer = safe_import('ai_models.ner_model', 'NERAnalyzer')
# ToxicityAnalyzer = safe_import('ai_models.toxicity_model', 'ToxicityAnalyzer')
# GeminiSummarizer = safe_import('ai_models.summary_gemini', 'GeminiSummarizer')

# ReportGenerator = safe_import('analysis.report_generator', 'ReportGenerator')
# SupabaseClient = safe_import('database.supabase_client', 'SupabaseClient')

# app = FastAPI(title="OSINT Analysis API", version="1.0.0")

# # CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class AnalysisRequest(BaseModel):
#     investigation_id: str
#     username: str
#     platforms: List[str]
#     ai_models: List[str]
#     export_formats: List[str]

# class AnalysisResponse(BaseModel):
#     investigation_id: str
#     status: str
#     results: dict
#     export_urls: List[str]

# # Initialize components with error handling
# components = {}

# def safe_initialize(component_name, component_class):
#     if component_class is None:
#         logger.warning(f"⚠️ {component_name} not available (import failed)")
#         return None
    
#     try:
#         instance = component_class()
#         components[component_name] = instance
#         logger.info(f"✓ {component_name} initialized successfully")
#         return instance
#     except Exception as e:
#         logger.error(f"✗ Failed to initialize {component_name}: {str(e)}")
#         components[component_name] = None
#         return None

# logger.info("=== Initializing OSINT Platform ===")

# # Initialize scrapers
# reddit_scraper = safe_initialize("RedditScraper", RedditScraper)
# twitter_scraper = safe_initialize("TwitterScraper", TwitterScraper)
# github_scraper = safe_initialize("GitHubScraper", GitHubScraper)
# instagram_scraper = safe_initialize("InstagramScraper", InstagramScraper)
# news_scraper = safe_initialize("NewsScraper", NewsScraper)

# # Initialize AI models
# sentiment_analyzer = safe_initialize("SentimentAnalyzer", SentimentAnalyzer)
# ner_analyzer = safe_initialize("NERAnalyzer", NERAnalyzer)
# toxicity_analyzer = safe_initialize("ToxicityAnalyzer", ToxicityAnalyzer)
# gemini_summarizer = safe_initialize("GeminiSummarizer", GeminiSummarizer)

# # Initialize other components
# report_generator = safe_initialize("ReportGenerator", ReportGenerator)
# db_client = safe_initialize("SupabaseClient", SupabaseClient)

# logger.info("=== Initialization Complete ===")

# @app.exception_handler(Exception)
# async def global_exception_handler(request: Request, exc: Exception):
#     logger.error(f"Global exception: {str(exc)}")
#     logger.error(f"Traceback: {traceback.format_exc()}")
    
#     return JSONResponse(
#         status_code=500,
#         content={
#             "error": "Internal server error",
#             "details": str(exc),
#             "type": exc.__class__.__name__,
#             "timestamp": datetime.now().isoformat()
#         }
#     )

# @app.get("/")
# async def root():
#     return {
#         "message": "OSINT Analysis API is running",
#         "status": "healthy",
#         "modules_loaded": modules_loaded,
#         "components_initialized": {k: v is not None for k, v in components.items()},
#         "timestamp": datetime.now().isoformat()
#     }

# @app.get("/health")
# async def health_check():
#     return {
#         "status": "healthy",
#         "timestamp": datetime.now().isoformat(),
#         "modules": modules_loaded,
#         "components": {k: v is not None for k, v in components.items()}
#     }

# @app.post("/analyze", response_model=AnalysisResponse)
# async def analyze_target(request: AnalysisRequest):
#     logger.info(f"=== Starting Analysis ===")
#     logger.info(f"Investigation ID: {request.investigation_id}")
#     logger.info(f"Username: {request.username}")
#     logger.info(f"Platforms: {request.platforms}")
#     logger.info(f"AI Models: {request.ai_models}")
    
#     try:
#         results = {}
#         all_content = []
        
#         # Data Collection Phase
#         for platform in request.platforms:
#             logger.info(f"Processing platform: {platform}")
#             platform_data = {}
            
#             try:
#                 if platform == "reddit" and reddit_scraper:
#                     platform_data = await reddit_scraper.scrape_user(request.username)
#                 elif platform == "twitter" and twitter_scraper:
#                     platform_data = await twitter_scraper.scrape_user(request.username)
#                 elif platform == "github" and github_scraper:
#                     platform_data = await github_scraper.scrape_user(request.username)
#                 elif platform == "instagram" and instagram_scraper:
#                     platform_data = await instagram_scraper.scrape_user(request.username)
#                 elif platform == "news" and news_scraper:
#                     platform_data = await news_scraper.search_mentions(request.username)
#                 else:
#                     platform_data = {
#                         'error': f'{platform} scraper not available',
#                         'platform': platform
#                     }
                
#                 results[platform] = platform_data
#                 logger.info(f"✓ {platform} processing completed")
                
#                 # Collect text content for AI analysis
#                 if isinstance(platform_data, dict) and 'error' not in platform_data:
#                     content_count = 0
                    
#                     if 'posts' in platform_data:
#                         for post in platform_data['posts']:
#                             content = post.get('content', post.get('title', post.get('body', post.get('selftext', ''))))
#                             if content and isinstance(content, str):
#                                 all_content.append(content)
#                                 content_count += 1
                    
#                     if 'comments' in platform_data:
#                         for comment in platform_data['comments']:
#                             content = comment.get('content', comment.get('body', ''))
#                             if content and isinstance(content, str):
#                                 all_content.append(content)
#                                 content_count += 1
                    
#                     if 'tweets' in platform_data:
#                         for tweet in platform_data['tweets']:
#                             content = tweet.get('content', '')
#                             if content and isinstance(content, str):
#                                 all_content.append(content)
#                                 content_count += 1
                    
#                     logger.info(f"Collected {content_count} content items from {platform}")
                
#             except Exception as e:
#                 logger.error(f"✗ {platform} processing failed: {str(e)}")
#                 logger.error(f"Traceback: {traceback.format_exc()}")
#                 results[platform] = {
#                     'error': str(e),
#                     'platform': platform,
#                     'traceback': traceback.format_exc()
#                 }
        
#         logger.info(f"Total content items collected: {len(all_content)}")
        
#         # AI Analysis Phase
#         ai_results = {}
        
#         if all_content:
#             if "sentiment" in request.ai_models and sentiment_analyzer:
#                 logger.info("Running sentiment analysis...")
#                 try:
#                     ai_results['sentiment'] = await sentiment_analyzer.analyze_batch(all_content)
#                     logger.info("✓ Sentiment analysis completed")
#                 except Exception as e:
#                     logger.error(f"✗ Sentiment analysis failed: {str(e)}")
#                     ai_results['sentiment'] = {'error': str(e)}
            
#             if "ner" in request.ai_models and ner_analyzer:
#                 logger.info("Running NER analysis...")
#                 try:
#                     ai_results['entities'] = await ner_analyzer.extract_entities_batch(all_content)
#                     logger.info("✓ NER analysis completed")
#                 except Exception as e:
#                     logger.error(f"✗ NER analysis failed: {str(e)}")
#                     ai_results['entities'] = {'error': str(e)}
            
#             if "toxicity" in request.ai_models and toxicity_analyzer:
#                 logger.info("Running toxicity analysis...")
#                 try:
#                     ai_results['toxicity'] = await toxicity_analyzer.analyze_batch(all_content)
#                     logger.info("✓ Toxicity analysis completed")
#                 except Exception as e:
#                     logger.error(f"✗ Toxicity analysis failed: {str(e)}")
#                     ai_results['toxicity'] = {'error': str(e)}
            
#             if "summary" in request.ai_models and gemini_summarizer:
#                 logger.info("Running summarization...")
#                 try:
#                     combined_text = " ".join(all_content[:1000])  # Limit for API
#                     ai_results['summary'] = await gemini_summarizer.summarize(combined_text)
#                     logger.info("✓ Summarization completed")
#                 except Exception as e:
#                     logger.error(f"✗ Summarization failed: {str(e)}")
#                     ai_results['summary'] = {'error': str(e)}
#         else:
#             logger.warning("No content found for AI analysis")
#             ai_results['warning'] = 'No content available for AI analysis'
        
#         # Generate exports
#         export_urls = []
#         if report_generator:
#             try:
#                 if "csv" in request.export_formats:
#                     csv_url = await report_generator.generate_csv(request.investigation_id, results, ai_results)
#                     if csv_url:
#                         export_urls.append(csv_url)
                
#                 if "pdf" in request.export_formats:
#                     pdf_url = await report_generator.generate_pdf(request.investigation_id, results, ai_results)
#                     if pdf_url:
#                         export_urls.append(pdf_url)
                
#                 if "json" in request.export_formats:
#                     json_url = await report_generator.generate_json(request.investigation_id, results, ai_results)
#                     if json_url:
#                         export_urls.append(json_url)
#             except Exception as e:
#                 logger.error(f"Export generation failed: {str(e)}")
        
#         logger.info("=== Analysis Completed Successfully ===")
        
#         return AnalysisResponse(
#             investigation_id=request.investigation_id,
#             status="completed",
#             results={**results, "ai_analysis": ai_results},
#             export_urls=export_urls
#         )
        
#     except Exception as e:
#         logger.error(f"=== Analysis Failed ===")
#         logger.error(f"Error: {str(e)}")
#         logger.error(f"Traceback: {traceback.format_exc()}")
#         raise HTTPException(
#             status_code=500, 
#             detail={
#                 "error": str(e),
#                 "type": e.__class__.__name__,
#                 "traceback": traceback.format_exc(),
#                 "investigation_id": request.investigation_id
#             }
#         )

# if __name__ == "__main__":
#     import uvicorn
#     logger.info("=== Starting OSINT API Server ===")
#     logger.info("Server will be available at: http://localhost:8000")
#     logger.info("Health check: http://localhost:8000/health")
#     logger.info("API docs: http://localhost:8000/docs")
    
#     try:
#         uvicorn.run(
#             app, 
#             host="0.0.0.0", 
#             port=8000, 
#             reload=False,  # Disable reload for stability
#             log_level="info"
#         )
#     except Exception as e:
#         logger.error(f"Failed to start server: {str(e)}")
#         sys.exit(1)



# !above woring best 


# import os
# import sys
# import certifi
# import ssl
# import logging
# from pathlib import Path

# # Configure logging first
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# )
# logger = logging.getLogger(__name__)

# # Set SSL certificates path
# os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
# os.environ['SSL_CERT_FILE'] = certifi.where()

# # Configure default SSL context
# ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

# # Suppress TensorFlow warnings
# os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
# os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

# # Fix fontconfig for WeasyPrint (Windows)
# if os.name == 'nt':  # Windows
#     fonts_dir = Path('C:/fonts')
#     fonts_dir.mkdir(exist_ok=True)
#     fonts_conf = fonts_dir / 'fonts.conf'
#     with open(fonts_conf, 'w') as f:
#         f.write('<?xml version="1.0"?><fontconfig><dir>C:\\Windows\\Fonts</dir></fontconfig>')
#     os.environ['FONTCONFIG_FILE'] = str(fonts_conf)

# from fastapi import FastAPI, HTTPException, Request
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel, ValidationError
# from typing import List, Optional
# import asyncio
# import traceback
# from datetime import datetime

# # Import modules with error handling
# modules_loaded = {}

# def safe_import(module_name, class_name):
#     try:
#         module = __import__(module_name, fromlist=[class_name])
#         cls = getattr(module, class_name)
#         modules_loaded[class_name] = True
#         logger.info(f"✓ Successfully imported {class_name}")
#         return cls
#     except Exception as e:
#         logger.error(f"✗ Failed to import {class_name}: {str(e)}")
#         modules_loaded[class_name] = False
#         return None

# # Import all modules
# RedditScraper = safe_import('scrapers.reddit_scraper', 'RedditScraper')
# TwitterScraper = safe_import('scrapers.twitter_scraper', 'TwitterScraper')
# GitHubScraper = safe_import('scrapers.github_scraper', 'GitHubScraper')
# InstagramScraper = safe_import('scrapers.instagram_scraper', 'InstagramScraper')
# NewsScraper = safe_import('scrapers.news_scraper', 'NewsScraper')

# SentimentAnalyzer = safe_import('ai_models.sentiment_model', 'SentimentAnalyzer')
# NERAnalyzer = safe_import('ai_models.ner_model', 'NERAnalyzer')
# ToxicityAnalyzer = safe_import('ai_models.toxicity_model', 'ToxicityAnalyzer')
# GeminiSummarizer = safe_import('ai_models.summary_gemini', 'GeminiSummarizer')

# ReportGenerator = safe_import('analysis.report_generator', 'ReportGenerator')
# SupabaseClient = safe_import('database.supabase_client', 'SupabaseClient')

# app = FastAPI(title="OSINT Analysis API", version="1.0.0")

# # CORS middleware
# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# class AnalysisRequest(BaseModel):
#     investigation_id: str
#     username: str
#     platforms: List[str]
#     ai_models: List[str]
#     export_formats: List[str]

# class AnalysisResponse(BaseModel):
#     investigation_id: str
#     status: str
#     results: dict
#     export_urls: List[str]

# # Initialize components with error handling
# components = {}

# def safe_initialize(component_name, component_class):
#     if component_class is None:
#         logger.warning(f"⚠️ {component_name} not available (import failed)")
#         return None
    
#     try:
#         instance = component_class()
#         components[component_name] = instance
#         logger.info(f"✓ {component_name} initialized successfully")
#         return instance
#     except Exception as e:
#         logger.error(f"✗ Failed to initialize {component_name}: {str(e)}")
#         components[component_name] = None
#         return None

# logger.info("=== Initializing OSINT Platform ===")

# # Initialize scrapers
# reddit_scraper = safe_initialize("RedditScraper", RedditScraper)
# twitter_scraper = safe_initialize("TwitterScraper", TwitterScraper)
# github_scraper = safe_initialize("GitHubScraper", GitHubScraper)
# instagram_scraper = safe_initialize("InstagramScraper", InstagramScraper)
# news_scraper = safe_initialize("NewsScraper", NewsScraper)

# # Initialize AI models
# sentiment_analyzer = safe_initialize("SentimentAnalyzer", SentimentAnalyzer)
# ner_analyzer = safe_initialize("NERAnalyzer", NERAnalyzer)
# toxicity_analyzer = safe_initialize("ToxicityAnalyzer", ToxicityAnalyzer)
# gemini_summarizer = safe_initialize("GeminiSummarizer", GeminiSummarizer)

# # Initialize other components
# report_generator = safe_initialize("ReportGenerator", ReportGenerator)
# db_client = safe_initialize("SupabaseClient", SupabaseClient)

# logger.info("=== Initialization Complete ===")

# def extract_content_from_platform_data(platform_data: dict) -> List[str]:
#     """Extract all text content from platform data for AI analysis"""
#     content = []
    
#     if not isinstance(platform_data, dict) or 'error' in platform_data:
#         return content
    
#     # Extract from posts
#     if 'posts' in platform_data:
#         for post in platform_data['posts']:
#             # Try different content fields
#             text = (post.get('content') or 
#                    post.get('caption') or 
#                    post.get('title') or 
#                    post.get('body') or 
#                    post.get('selftext') or '')
            
#             if text and isinstance(text, str) and len(text.strip()) > 5:
#                 content.append(text.strip())
    
#     # Extract from comments
#     if 'comments' in platform_data:
#         for comment in platform_data['comments']:
#             text = comment.get('content') or comment.get('body') or ''
            
#             if text and isinstance(text, str) and len(text.strip()) > 5:
#                 content.append(text.strip())
    
#     # Extract from tweets
#     if 'tweets' in platform_data:
#         for tweet in platform_data['tweets']:
#             text = tweet.get('content') or ''
            
#             if text and isinstance(text, str) and len(text.strip()) > 5:
#                 content.append(text.strip())
    
#     # Extract from commits (GitHub)
#     if 'commits' in platform_data:
#         for commit in platform_data['commits']:
#             text = commit.get('message') or ''
            
#             if text and isinstance(text, str) and len(text.strip()) > 5:
#                 content.append(text.strip())
    
#     # Extract from repositories (GitHub)
#     if 'repositories' in platform_data:
#         for repo in platform_data['repositories']:
#             text = repo.get('description') or ''
            
#             if text and isinstance(text, str) and len(text.strip()) > 5:
#                 content.append(text.strip())
    
#     return content

# @app.exception_handler(Exception)
# async def global_exception_handler(request: Request, exc: Exception):
#     logger.error(f"Global exception: {str(exc)}")
#     logger.error(f"Traceback: {traceback.format_exc()}")
    
#     return JSONResponse(
#         status_code=500,
#         content={
#             "error": "Internal server error",
#             "details": str(exc),
#             "type": exc.__class__.__name__,
#             "timestamp": datetime.now().isoformat()
#         }
#     )

# @app.get("/")
# async def root():
#     return {
#         "message": "OSINT Analysis API is running",
#         "status": "healthy",
#         "modules_loaded": modules_loaded,
#         "components_initialized": {k: v is not None for k, v in components.items()},
#         "timestamp": datetime.now().isoformat()
#     }

# @app.get("/health")
# async def health_check():
#     return {
#         "status": "healthy",
#         "timestamp": datetime.now().isoformat(),
#         "modules": modules_loaded,
#         "components": {k: v is not None for k, v in components.items()}
#     }

# @app.post("/analyze", response_model=AnalysisResponse)
# async def analyze_target(request: AnalysisRequest):
#     logger.info(f"=== Starting Analysis ===")
#     logger.info(f"Investigation ID: {request.investigation_id}")
#     logger.info(f"Username: {request.username}")
#     logger.info(f"Platforms: {request.platforms}")
#     logger.info(f"AI Models: {request.ai_models}")
    
#     try:
#         results = {}
#         all_content = []
        
#         # Data Collection Phase
#         for platform in request.platforms:
#             logger.info(f"Processing platform: {platform}")
#             platform_data = {}
            
#             try:
#                 if platform == "reddit" and reddit_scraper:
#                     platform_data = await reddit_scraper.scrape_user(request.username)
#                 elif platform == "twitter" and twitter_scraper:
#                     platform_data = await twitter_scraper.scrape_user(request.username)
#                 elif platform == "github" and github_scraper:
#                     platform_data = await github_scraper.scrape_user(request.username)
#                 elif platform == "instagram" and instagram_scraper:
#                     platform_data = await instagram_scraper.scrape_user(request.username)
#                 elif platform == "news" and news_scraper:
#                     platform_data = await news_scraper.search_mentions(request.username)
#                 else:
#                     platform_data = {
#                         'error': f'{platform} scraper not available',
#                         'platform': platform
#                     }
                
#                 results[platform] = platform_data
#                 logger.info(f"✓ {platform} processing completed")
                
#                 # Extract content for AI analysis
#                 platform_content = extract_content_from_platform_data(platform_data)
#                 all_content.extend(platform_content)
                
#                 logger.info(f"Collected {len(platform_content)} content items from {platform}")
                
#             except Exception as e:
#                 logger.error(f"✗ {platform} processing failed: {str(e)}")
#                 logger.error(f"Traceback: {traceback.format_exc()}")
#                 results[platform] = {
#                     'error': str(e),
#                     'platform': platform,
#                     'traceback': traceback.format_exc()
#                 }
        
#         logger.info(f"Total content items collected: {len(all_content)}")
        
#         # AI Analysis Phase
#         ai_results = {}
        
#         if all_content:
#             if "sentiment" in request.ai_models and sentiment_analyzer:
#                 logger.info("Running sentiment analysis...")
#                 try:
#                     ai_results['sentiment'] = await sentiment_analyzer.analyze_batch(all_content)
#                     logger.info("✓ Sentiment analysis completed")
#                 except Exception as e:
#                     logger.error(f"✗ Sentiment analysis failed: {str(e)}")
#                     ai_results['sentiment'] = {'error': str(e)}
            
#             if "ner" in request.ai_models and ner_analyzer:
#                 logger.info("Running NER analysis...")
#                 try:
#                     ai_results['entities'] = await ner_analyzer.extract_entities_batch(all_content)
#                     logger.info("✓ NER analysis completed")
#                 except Exception as e:
#                     logger.error(f"✗ NER analysis failed: {str(e)}")
#                     ai_results['entities'] = {'error': str(e)}
            
#             if "toxicity" in request.ai_models and toxicity_analyzer:
#                 logger.info("Running toxicity analysis...")
#                 try:
#                     ai_results['toxicity'] = await toxicity_analyzer.analyze_batch(all_content)
#                     logger.info("✓ Toxicity analysis completed")
#                 except Exception as e:
#                     logger.error(f"✗ Toxicity analysis failed: {str(e)}")
#                     ai_results['toxicity'] = {'error': str(e)}
            
#             if "summary" in request.ai_models and gemini_summarizer:
#                 logger.info("Running summarization...")
#                 try:
#                     combined_text = " ".join(all_content[:1000])  # Limit for API
#                     ai_results['summary'] = await gemini_summarizer.summarize(combined_text)
                    
#                     # Also run profile analysis
#                     ai_results['profile_analysis'] = await gemini_summarizer.analyze_profile(results)
                    
#                     logger.info("✓ Summarization completed")
#                 except Exception as e:
#                     logger.error(f"✗ Summarization failed: {str(e)}")
#                     ai_results['summary'] = {'error': str(e)}
#         else:
#             logger.warning("No content found for AI analysis")
#             ai_results['warning'] = 'No content available for AI analysis'
        
#         # Generate exports
#         export_urls = []
#         if report_generator:
#             try:
#                 if "csv" in request.export_formats:
#                     csv_url = await report_generator.generate_csv(request.investigation_id, results, ai_results)
#                     if csv_url:
#                         export_urls.append(csv_url)
                
#                 if "pdf" in request.export_formats:
#                     pdf_url = await report_generator.generate_pdf(request.investigation_id, results, ai_results)
#                     if pdf_url:
#                         export_urls.append(pdf_url)
                
#                 if "json" in request.export_formats:
#                     json_url = await report_generator.generate_json(request.investigation_id, results, ai_results)
#                     if json_url:
#                         export_urls.append(json_url)
#             except Exception as e:
#                 logger.error(f"Export generation failed: {str(e)}")
        
#         logger.info("=== Analysis Completed Successfully ===")
        
#         return AnalysisResponse(
#             investigation_id=request.investigation_id,
#             status="completed",
#             results={**results, "ai_analysis": ai_results},
#             export_urls=export_urls
#         )
        
#     except Exception as e:
#         logger.error(f"=== Analysis Failed ===")
#         logger.error(f"Error: {str(e)}")
#         logger.error(f"Traceback: {traceback.format_exc()}")
#         raise HTTPException(
#             status_code=500, 
#             detail={
#                 "error": str(e),
#                 "type": e.__class__.__name__,
#                 "traceback": traceback.format_exc(),
#                 "investigation_id": request.investigation_id
#             }
#         )

# if __name__ == "__main__":
#     import uvicorn
#     logger.info("=== Starting OSINT API Server ===")
#     logger.info("Server will be available at: http://localhost:8000")
#     logger.info("Health check: http://localhost:8000/health")
#     logger.info("API docs: http://localhost:8000/docs")
    
#     try:
#         uvicorn.run(
#             app, 
#             host="0.0.0.0", 
#             port=8000, 
#             reload=False,  # Disable reload for stability
#             log_level="info"
#         )
#     except Exception as e:
#         logger.error(f"Failed to start server: {str(e)}")
#         sys.exit(1)



# !!!!above best woeking use 

# import os
# import sys
# import asyncio
# import logging
# import json
# from datetime import datetime
# from typing import Dict, List, Optional, Any
# from fastapi import FastAPI, HTTPException, BackgroundTasks
# from fastapi.middleware.cors import CORSMiddleware
# from fastapi.responses import JSONResponse
# from pydantic import BaseModel
# import uvicorn

# # Configure logging
# logging.basicConfig(
#     level=logging.INFO,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
# )
# logger = logging.getLogger(__name__)

# # Import our modules
# try:
#     from scrapers.twitter_scraper import TwitterScraper
#     from scrapers.reddit_scraper import RedditScraper
#     from scrapers.github_scraper import GitHubScraper
#     from scrapers.instagram_scraper import InstagramScraper
#     from scrapers.news_scraper import NewsScraper
#     from ai_models.sentiment_model import SentimentAnalyzer
#     from ai_models.summary_gemini import GeminiSummarizer
#     from ai_models.ner_model import NERAnalyzer

#     from ai_models.toxicity_model import ToxicityAnalyzer
#     from analysis.report_generator import ReportGenerator

#     from facial_recognition.face_analyzer import FacialRecognitionAnalyzer
#     logger.info("✅ All modules imported successfully")
# except ImportError as e:
#     logger.error(f"❌ Failed to import modules: {e}")
#     sys.exit(1)

# # Initialize FastAPI app
# app = FastAPI(
#     title="OSINT Analysis Platform",
#     description="Advanced OSINT platform with AI-powered analysis",
#     version="2.0.0"
# )

# # CORS middleware
# origins = [
#     "http://localhost",
#     "http://localhost:3000",
#     "http://localhost:8000",
#     "*",  # REMOVE IN PRODUCTION
# ]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

# # Initialize components
# scrapers = {
#     'twitter': TwitterScraper(),
#     'reddit': RedditScraper(),
#     'github': GitHubScraper(),
#     'instagram': InstagramScraper(),
#     'news': NewsScraper()
# }

# # AI Models
# gemini_summarizer = GeminiSummarizer()
# sentiment_analyzer = SentimentAnalyzer()
# ner_model = NERModel()
# toxicity_analyzer = ToxicityAnalyzer()
# report_generator = ReportGenerator()
# face_analyzer = FacialRecognitionAnalyzer()

# # Pydantic models
# class AnalysisRequest(BaseModel):
#     target_user: str
#     platforms: List[str]
#     ai_models: Optional[List[str]] = ["sentiment", "summary", "ner", "toxicity"]
#     export_formats: Optional[List[str]] = ["json"]

# class ChatAnalysisRequest(BaseModel):
#     message: str
#     context: Optional[Dict[str, Any]] = {}

# class FacialRecognitionRequest(BaseModel):
#     image_data: str  # Base64 encoded image
#     search_platforms: Optional[List[str]] = ["twitter", "instagram", "linkedin"]

# class TextAnalysisRequest(BaseModel):
#     text: str

# class SentimentAnalysisRequest(BaseModel):
#     text: str

# class NERRequest(BaseModel):
#     text: str

# class ToxicityAnalysisRequest(BaseModel):
#     text: str

# class ReportGenerationRequest(BaseModel):
#     data: dict

# # Global storage for investigations
# investigations_storage = {}

# @app.get("/")
# async def root():
#     """Root endpoint with system status"""
#     return {
#         "message": "🔍 OSINT Analysis Platform API",
#         "version": "2.0.0",
#         "status": "operational",
#         "timestamp": datetime.now().isoformat(),
#         "available_endpoints": [
#             "/analyze",
#             "/test-scrapers", 
#             "/test-ai",
#             "/chat-analysis",
#             "/facial-recognition",
#             "/health",
#             "/summarize",
#             "/sentiment",
#             "/ner",
#             "/toxicity",
#             "/report"
#         ]
#     }

# @app.get("/health")
# async def health_check():
#     """Health check endpoint"""
#     try:
#         # Test Gemini connection
#         gemini_status = gemini_summarizer.test_connection()
        
#         return {
#             "status": "healthy",
#             "timestamp": datetime.now().isoformat(),
#             "components": {
#                 "scrapers": {name: "operational" for name in scrapers.keys()},
#                 "ai_models": {
#                     "gemini": gemini_status.get("status", "error"),
#                     "sentiment": "operational",
#                     "ner": "operational", 
#                     "toxicity": "operational"
#                 }
#             },
#             "gemini_details": gemini_status
#         }
#     except Exception as e:
#         logger.error(f"Health check failed: {e}")
#         return JSONResponse(
#             status_code=500,
#             content={
#                 "status": "unhealthy",
#                 "error": str(e),
#                 "timestamp": datetime.now().isoformat()
#             }
#         )

# @app.post("/analyze")
# async def analyze_target(request: AnalysisRequest, background_tasks: BackgroundTasks):
#     """Main analysis endpoint"""
#     investigation_id = f"inv_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{request.target_user}"
    
#     try:
#         logger.info(f"🎯 Starting analysis for: {request.target_user}")
#         logger.info(f"📱 Platforms: {request.platforms}")
#         logger.info(f"🤖 AI Models: {request.ai_models}")
        
#         # Initialize investigation
#         investigation = {
#             "id": investigation_id,
#             "target_user": request.target_user,
#             "platforms": request.platforms,
#             "ai_models": request.ai_models,
#             "status": "running",
#             "started_at": datetime.now().isoformat(),
#             "results": {},
#             "ai_analysis": {},
#             "errors": []
#         }
        
#         investigations_storage[investigation_id] = investigation
        
#         # Scrape data from each platform
#         for platform in request.platforms:
#             if platform in scrapers:
#                 try:
#                     logger.info(f"🔍 Scraping {platform} for {request.target_user}")
#                     scraper = scrapers[platform]
                    
#                     if platform == 'twitter':
#                         data = await scraper.scrape_user_data(request.target_user)
#                     elif platform == 'reddit':
#                         data = await scraper.scrape_user_data(request.target_user)
#                     elif platform == 'github':
#                         data = await scraper.scrape_user_data(request.target_user)
#                     elif platform == 'instagram':
#                         data = await scraper.scrape_user_data(request.target_user)
#                     elif platform == 'news':
#                         data = await scraper.search_news(request.target_user)
                    
#                     investigation["results"][platform] = data
#                     logger.info(f"✅ {platform} scraping completed")
                    
#                 except Exception as e:
#                     error_msg = f"❌ {platform} scraping failed: {str(e)}"
#                     logger.error(error_msg)
#                     investigation["errors"].append(error_msg)
#                     investigation["results"][platform] = {"error": str(e)}
#             else:
#                 error_msg = f"❌ Unknown platform: {platform}"
#                 logger.warning(error_msg)
#                 investigation["errors"].append(error_msg)
        
#         # AI Analysis
#         if request.ai_models:
#             logger.info("🤖 Starting AI analysis...")
#             ai_results = {}
            
#             # Collect all text content for analysis
#             all_content = []
#             for platform, data in investigation["results"].items():
#                 if isinstance(data, dict) and "error" not in data:
#                     # Extract text from posts
#                     for post in data.get("posts", []):
#                         content = (post.get("content") or 
#                                  post.get("caption") or 
#                                  post.get("title") or 
#                                  post.get("body") or 
#                                  post.get("selftext") or "")
#                         if content:
#                             all_content.append(content)
                    
#                     # Extract text from comments
#                     for comment in data.get("comments", []):
#                         content = comment.get("content") or comment.get("body") or ""
#                         if content:
#                             all_content.append(content)
                    
#                     # Extract text from tweets
#                     for tweet in data.get("tweets", []):
#                         content = tweet.get("content") or ""
#                         if content:
#                             all_content.append(content)
            
#             logger.info(f"📝 Collected {len(all_content)} text items for AI analysis")
            
#             # Summary Analysis
#             if "summary" in request.ai_models and all_content:
#                 try:
#                     logger.info("📊 Generating summary...")
#                     combined_text = "\n".join(all_content[:50])  # Limit content
#                     summary_result = await gemini_summarizer.summarize(combined_text)
#                     ai_results["summary"] = summary_result
#                     logger.info("✅ Summary analysis completed")
#                 except Exception as e:
#                     error_msg = f"❌ Summary analysis failed: {str(e)}"
#                     logger.error(error_msg)
#                     ai_results["summary"] = {"error": str(e)}
            
#             # Profile Analysis
#             if "profile_analysis" in request.ai_models:
#                 try:
#                     logger.info("👤 Generating profile analysis...")
#                     profile_result = await gemini_summarizer.analyze_profile(investigation["results"])
#                     ai_results["profile_analysis"] = profile_result
#                     logger.info("✅ Profile analysis completed")
#                 except Exception as e:
#                     error_msg = f"❌ Profile analysis failed: {str(e)}"
#                     logger.error(error_msg)
#                     ai_results["profile_analysis"] = {"error": str(e)}
            
#             # Sentiment Analysis
#             if "sentiment" in request.ai_models and all_content:
#                 try:
#                     logger.info("😊 Analyzing sentiment...")
#                     sentiment_result = await gemini_summarizer.analyze_sentiment_and_emotions(all_content[:20])
#                     ai_results["sentiment"] = sentiment_result
#                     logger.info("✅ Sentiment analysis completed")
#                 except Exception as e:
#                     error_msg = f"❌ Sentiment analysis failed: {str(e)}"
#                     logger.error(error_msg)
#                     ai_results["sentiment"] = {"error": str(e)}
            
#             # NER Analysis
#             if "ner" in request.ai_models and all_content:
#                 try:
#                     logger.info("🏷️ Extracting named entities...")
#                     ner_result = await ner_model.extract_entities_batch(all_content[:10])
#                     ai_results["ner"] = ner_result
#                     logger.info("✅ NER analysis completed")
#                 except Exception as e:
#                     error_msg = f"❌ NER analysis failed: {str(e)}"
#                     logger.error(error_msg)
#                     ai_results["ner"] = {"error": str(e)}
            
#             # Toxicity Analysis
#             if "toxicity" in request.ai_models and all_content:
#                 try:
#                     logger.info("⚠️ Analyzing toxicity...")
#                     toxicity_result = await toxicity_analyzer.analyze_batch(all_content[:15])
#                     ai_results["toxicity"] = toxicity_result
#                     logger.info("✅ Toxicity analysis completed")
#                 except Exception as e:
#                     error_msg = f"❌ Toxicity analysis failed: {str(e)}"
#                     logger.error(error_msg)
#                     ai_results["toxicity"] = {"error": str(e)}
            
#             investigation["ai_analysis"] = ai_results
        
#         # Update investigation status
#         investigation["status"] = "completed"
#         investigation["completed_at"] = datetime.now().isoformat()
#         investigations_storage[investigation_id] = investigation
        
#         logger.info(f"✅ Analysis completed for {request.target_user}")
        
#         return {
#             "investigation_id": investigation_id,
#             "status": "completed",
#             "target_user": request.target_user,
#             "platforms_analyzed": len([p for p in request.platforms if p in investigation["results"] and "error" not in investigation["results"][p]]),
#             "total_platforms": len(request.platforms),
#             "ai_models_used": len(request.ai_models) if request.ai_models else 0,
#             "errors": investigation["errors"],
#             "results": investigation["results"],
#             "ai_analysis": investigation["ai_analysis"],
#             "completed_at": investigation["completed_at"]
#         }
        
#     except Exception as e:
#         error_msg = f"❌ Analysis failed: {str(e)}"
#         logger.error(error_msg)
        
#         # Update investigation with error
#         if investigation_id in investigations_storage:
#             investigations_storage[investigation_id]["status"] = "failed"
#             investigations_storage[investigation_id]["error"] = str(e)
        
#         raise HTTPException(status_code=500, detail=error_msg)

# @app.post("/chat-analysis")
# async def chat_analysis(request: ChatAnalysisRequest):
#     """AI-powered chat analysis using Gemini"""
#     try:
#         logger.info(f"💬 Processing chat message: {request.message[:50]}...")
        
#         # Create context-aware prompt
#         context = request.context or {}
        
#         prompt = f"""
#         You are an expert OSINT analyst assistant. A user is asking about their investigation data.
        
#         **User Question:** {request.message}
        
#         **Current Context:**
#         - Selected User: {context.get('selectedUser', 'All users')}
#         - Total Posts: {context.get('totalPosts', 0)}
#         - High Risk Posts: {context.get('highRiskPosts', 0)}
#         - Active Investigations: {context.get('investigations', 0)}
#         - Emotion Distribution: {json.dumps(context.get('emotionDistribution', []))}
        
#         Please provide a helpful, professional response as an OSINT analysis expert. 
#         Be specific, actionable, and reference the context data when relevant.
#         Use emojis and formatting to make the response engaging.
        
#         If the user asks about:
#         - Summary/Overview: Provide analysis statistics and key insights
#         - Risk Assessment: Focus on high-risk content and security concerns
#         - User Profiles: Give detailed behavioral analysis
#         - Trends/Patterns: Discuss temporal and emotional patterns
#         - Recommendations: Suggest next steps for investigation
        
#         Keep responses concise but informative (max 500 words).
#         """
        
#         # Use Gemini for intelligent response
#         if gemini_summarizer.enabled:
#             response_data = await gemini_summarizer.model.generate_content_async(prompt)
#             response_text = response_data.text.strip()
#         else:
#             # Fallback response
#             response_text = generate_fallback_response(request.message, context)
        
#         logger.info("✅ Chat analysis completed")
        
#         return {
#             "response": response_text,
#             "model": "gemini-1.5-flash",
#             "timestamp": datetime.now().isoformat()
#         }
        
#     except Exception as e:
#         logger.error(f"❌ Chat analysis failed: {str(e)}")
        
#         # Fallback response
#         fallback_response = generate_fallback_response(request.message, request.context)
        
#         return {
#             "response": fallback_response,
#             "model": "fallback",
#             "error": str(e),
#             "timestamp": datetime.now().isoformat()
#         }

# def generate_fallback_response(message: str, context: Dict) -> str:
#     """Generate fallback response when Gemini is unavailable"""
#     message_lower = message.lower()
    
#     if "summary" in message_lower or "overview" in message_lower:
#         return f"""📊 **OSINT Analysis Summary**
        
# **Current Investigation Status:**
# - Total Posts Analyzed: {context.get('totalPosts', 0)}
# - High Risk Content: {context.get('highRiskPosts', 0)} posts
# - Active Investigations: {context.get('investigations', 0)}
# - Selected User: {context.get('selectedUser', 'All users')}

# **Key Insights:**
# - The analysis covers multiple social media platforms
# - Emotional patterns are tracked over time
# - Risk assessment is performed on all content
# - User behavior patterns are identified

# **Recommendations:**
# - Review high-risk content for security concerns
# - Monitor emotional trends for behavioral changes
# - Cross-reference findings across platforms
# - Generate detailed reports for documentation

# Would you like me to focus on any specific aspect of the analysis?"""

#     elif "risk" in message_lower or "dangerous" in message_lower:
#         return f"""⚠️ **Risk Assessment Report**
        
# **High Risk Content Detected:**
# - Critical/High Risk Posts: {context.get('highRiskPosts', 0)}
# - Risk Categories: Threatening, Hateful, Harmful content
# - Monitoring Status: Active surveillance recommended

# **Risk Mitigation:**
# - Flag concerning content for review
# - Monitor user behavior patterns
# - Document evidence for potential escalation
# - Consider platform reporting if necessary

# **Next Steps:**
# - Review individual high-risk posts
# - Analyze user connections and networks
# - Generate comprehensive risk report
# - Implement monitoring protocols

# The system continuously monitors for concerning patterns and behaviors."""

#     elif "user" in message_lower or "profile" in message_lower:
#         selected_user = context.get('selectedUser')
#         if selected_user:
#             return f"""👤 **User Profile Analysis: {selected_user}**
            
# **Digital Footprint:**
# - Platform Activity: Multi-platform presence detected
# - Content Volume: {context.get('totalPosts', 0)} posts analyzed
# - Risk Assessment: Ongoing evaluation
# - Behavioral Patterns: Under analysis

# **Analysis Areas:**
# - Communication style and tone
# - Topic interests and focus areas
# - Social connections and networks
# - Temporal activity patterns
# - Emotional expression patterns

# **Investigation Status:**
# - Data collection: Complete
# - AI analysis: In progress
# - Risk evaluation: Ongoing
# - Report generation: Available

# Click on specific posts in the timeline to see detailed analysis."""
#         else:
#             return f"""👥 **User Analysis Overview**
            
# **Available Profiles:**
# - Total users in database: Multiple profiles
# - Analysis depth: Comprehensive behavioral profiling
# - Risk assessment: Individual and collective
# - Pattern recognition: Cross-platform analysis

# **Analysis Capabilities:**
# - Individual user deep-dive analysis
# - Cross-platform behavior correlation
# - Social network mapping
# - Risk pattern identification
# - Temporal behavior analysis

# Select a specific user from the timeline to get detailed profile analysis."""

#     else:
#         return f"""🤖 **OSINT Analysis Assistant**
        
# I can help you analyze:

# 📊 **Data Overview**: Current investigation statistics and insights
# ⚠️ **Risk Assessment**: High-risk content and security concerns
# 👤 **User Profiles**: Individual behavioral analysis and patterns
# 📈 **Trends**: Temporal and emotional pattern analysis
# 🔍 **Investigation**: Detailed findings and recommendations

# **Current Context:**
# - Posts: {context.get('totalPosts', 0)}
# - High Risk: {context.get('highRiskPosts', 0)}
# - Investigations: {context.get('investigations', 0)}
# - Focus: {context.get('selectedUser', 'All users')}

# What specific aspect would you like me to analyze?"""

# @app.post("/facial-recognition")
# async def facial_recognition_analysis(request: FacialRecognitionRequest):
#     """Facial recognition and social media lookup feature"""
#     try:
#         logger.info("🔍 Starting facial recognition analysis...")
        
#         # Step 1: Identify person from image
#         identification_result = await face_analyzer.identify_person(request.image_data)
        
#         if identification_result.get("error"):
#             return {
#                 "status": "error",
#                 "error": identification_result["error"],
#                 "timestamp": datetime.now().isoformat()
#             }
        
#         identified_person = identification_result.get("identified_person")
        
#         if not identified_person:
#             return {
#                 "status": "no_match",
#                 "message": "No matching person found in database",
#                 "faces_detected": identification_result.get("faces_detected", 0),
#                 "timestamp": datetime.now().isoformat()
#             }
        
#         logger.info(f"✅ Person identified: {identified_person['name']}")
        
#         # Step 2: Find social media profiles
#         social_profiles = await face_analyzer.find_social_media_profiles(
#             identified_person["name"], 
#             request.search_platforms
#         )
        
#         # Step 3: Fetch news articles
#         news_articles = await face_analyzer.fetch_news_articles(identified_person["name"])
        
#         # Step 4: Generate AI summary using Gemini
#         ai_summary = {}
#         if gemini_summarizer.enabled and news_articles:
#             try:
#                 # Combine news content for summarization
#                 news_content = "\n".join([
#                     f"Title: {article['title']}\nDescription: {article['description']}"
#                     for article in news_articles
#                 ])
                
#                 summary_result = await gemini_summarizer.summarize(
#                     f"News about {identified_person['name']}:\n{news_content}",
#                     max_length=800
#                 )
#                 ai_summary = summary_result
#                 logger.info("✅ AI summary generated")
#             except Exception as e:
#                 logger.error(f"❌ AI summary failed: {str(e)}")
#                 ai_summary = {"error": str(e)}
        
#         # Step 5: Generate comprehensive report
#         report_data = {
#             "identified_person": identified_person,
#             "social_profiles": social_profiles,
#             "news_articles": news_articles,
#             "ai_summary": ai_summary
#         }
        
#         comprehensive_report = await face_analyzer.generate_comprehensive_report(report_data)
        
#         # Return complete analysis
#         return {
#             "status": "success",
#             "identified_person": identified_person,
#             "social_media_profiles": social_profiles,
#             "news_articles": news_articles,
#             "ai_summary": ai_summary,
#             "comprehensive_report": comprehensive_report,
#             "analysis_metadata": {
#                 "faces_detected": identification_result.get("faces_detected", 0),
#                 "platforms_searched": len(request.search_platforms),
#                 "news_articles_found": len(news_articles),
#                 "ai_analysis_status": "completed" if ai_summary and "error" not in ai_summary else "failed"
#             },
#             "timestamp": datetime.now().isoformat()
#         }
        
#     except Exception as e:
#         logger.error(f"❌ Facial recognition analysis failed: {str(e)}")
#         raise HTTPException(status_code=500, detail=str(e))

# @app.post("/summarize")
# async def summarize_text(request: TextAnalysisRequest):
#     """Summarize text using Gemini."""
#     try:
#         if not gemini_summarizer.enabled:
#             raise HTTPException(status_code=503, detail="Gemini summarization is currently disabled.")
        
#         result = await gemini_summarizer.summarize(request.text)
#         return {"status": "success", "summary": result, "timestamp": datetime.now().isoformat()}
#     except Exception as e:
#         logger.error(f"Summarization failed: {str(e)}")
#         raise HTTPException(status_code=500, detail=str(e))

# @app.post("/sentiment")
# async def analyze_sentiment(request: SentimentAnalysisRequest):
#     """Analyze sentiment of text."""
#     try:
#         result = await sentiment_analyzer.analyze_sentiment(request.text)
#         return {"status": "success", "sentiment": result, "timestamp": datetime.now().isoformat()}
#     except Exception as e:
#         logger.error(f"Sentiment analysis failed: {str(e)}")
#         raise HTTPException(status_code=500, detail=str(e))

# @app.post("/ner")
# async def recognize_entities(request: NERRequest):
#     """Recognize named entities in text."""
#     try:
#         result = await ner_model.recognize_entities(request.text)
#         return {"status": "success", "entities": result, "timestamp": datetime.now().isoformat()}
#     except Exception as e:
#         logger.error(f"NER failed: {str(e)}")
#         raise HTTPException(status_code=500, detail=str(e))

# @app.post("/toxicity")
# async def analyze_toxicity(request: ToxicityAnalysisRequest):
#     """Analyze toxicity of text."""
#     try:
#         result = await toxicity_analyzer.analyze_toxicity(request.text)
#         return {"status": "success", "toxicity": result, "timestamp": datetime.now().isoformat()}
#     except Exception as e:
#         logger.error(f"Toxicity analysis failed: {str(e)}")
#         raise HTTPException(status_code=500, detail=str(e))

# @app.post("/report")
# async def generate_report(request: ReportGenerationRequest):
#     """Generate a report from given data."""
#     try:
#         result = await report_generator.generate_report(request.data)
#         return {"status": "success", "report": result, "timestamp": datetime.now().isoformat()}
#     except Exception as e:
#         logger.error(f"Report generation failed: {str(e)}")
#         raise HTTPException(status_code=500, detail=str(e))

# @app.get("/test-scrapers")
# async def test_scrapers():
#     """Test all scrapers"""
#     results = {}
    
#     for name, scraper in scrapers.items():
#         try:
#             logger.info(f"Testing {name} scraper...")
            
#             if name == 'twitter':
#                 result = await scraper.scrape_user_data("elonmusk")
#             elif name == 'reddit':
#                 result = await scraper.scrape_user_data("spez")
#             elif name == 'github':
#                 result = await scraper.scrape_user_data("torvalds")
#             elif name == 'instagram':
#                 result = await scraper.scrape_user_data("instagram")
#             elif name == 'news':
#                 result = await scraper.search_news("technology")
            
#             results[name] = {
#                 "status": "success",
#                 "data_points": len(result.get("posts", [])) + len(result.get("comments", [])) + len(result.get("tweets", [])),
#                 "sample": str(result)[:200] + "..." if result else "No data"
#             }
#             logger.info(f"✅ {name} scraper test passed")
            
#         except Exception as e:
#             logger.error(f"❌ {name} scraper test failed: {e}")
#             results[name] = {
#                 "status": "error",
#                 "error": str(e)
#             }
    
#     return {
#         "timestamp": datetime.now().isoformat(),
#         "results": results,
#         "summary": f"{sum(1 for r in results.values() if r['status'] == 'success')}/{len(results)} scrapers working"
#     }

# @app.get("/test-ai")
# async def test_ai_models():
#     """Test all AI models"""
#     results = {}
    
#     # Test Gemini
#     try:
#         logger.info("Testing Gemini summarizer...")
#         gemini_test = gemini_summarizer.test_connection()
#         results["gemini"] = gemini_test
#         logger.info("✅ Gemini test completed")
#     except Exception as e:
#         logger.error(f"❌ Gemini test failed: {e}")
#         results["gemini"] = {"status": "error", "error": str(e)}
    
#     # Test other AI models
#     test_text = "This is a test message for AI analysis."
    
#     try:
#         logger.info("Testing sentiment analyzer...")
#         sentiment_result = await sentiment_analyzer.analyze_text(test_text)
#         results["sentiment"] = {"status": "success", "result": sentiment_result}
#         logger.info("✅ Sentiment analyzer test passed")
#     except Exception as e:
#         logger.error(f"❌ Sentiment analyzer test failed: {e}")
#         results["sentiment"] = {"status": "error", "error": str(e)}
    
#     try:
#         logger.info("Testing NER model...")
#         ner_result = await ner_model.extract_entities(test_text)
#         results["ner"] = {"status": "success", "result": ner_result}
#         logger.info("✅ NER model test passed")
#     except Exception as e:
#         logger.error(f"❌ NER model test failed: {e}")
#         results["ner"] = {"status": "error", "error": str(e)}
    
#     try:
#         logger.info("Testing toxicity analyzer...")
#         toxicity_result = await toxicity_analyzer.analyze_text(test_text)
#         results["toxicity"] = {"status": "success", "result": toxicity_result}
#         logger.info("✅ Toxicity analyzer test passed")
#     except Exception as e:
#         logger.error(f"❌ Toxicity analyzer test failed: {e}")
#         results["toxicity"] = {"status": "error", "error": str(e)}
    
#     return {
#         "timestamp": datetime.now().isoformat(),
#         "results": results,
#         "summary": f"{sum(1 for r in results.values() if r.get('status') == 'success')}/{len(results)} AI models working"
#     }

# if __name__ == "__main__":
#     logger.info("🚀 Starting OSINT Analysis Platform...")
#     uvicorn.run(
#         "main:app",
#         host="0.0.0.0",
#         port=8000,
#         reload=True,
#         log_level="info"
#     )


# new 

import os
import sys
import asyncio
import logging
import json
from datetime import datetime
from typing import Dict, List, Optional, Any
from fastapi import FastAPI, HTTPException, BackgroundTasks
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import uvicorn

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Import our modules
try:
    from scrapers.twitter_scraper import TwitterScraper
    from scrapers.reddit_scraper import RedditScraper
    from scrapers.github_scraper import GitHubScraper
    from scrapers.instagram_scraper import InstagramScraper
    from scrapers.news_scraper import NewsScraper
    from ai_models.sentiment_model import SentimentAnalyzer
    from ai_models.summary_gemini import GeminiSummarizer
    from ai_models.ner_model import NERAnalyzer  # Fixed: Changed from NERModel to NERAnalyzer
    from ai_models.toxicity_model import ToxicityAnalyzer
    from analysis.report_generator import ReportGenerator
    from facial_recognition.face_analyzer import FacialRecognitionAnalyzer
    logger.info("✅ All modules imported successfully")
except ImportError as e:
    logger.error(f"❌ Failed to import modules: {e}")
    sys.exit(1)

# Initialize FastAPI app
app = FastAPI(
    title="OSINT Analysis Platform",
    description="Advanced OSINT platform with AI-powered analysis",
    version="2.0.0"
)

# CORS middleware
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8000",
    "*",  # REMOVE IN PRODUCTION
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize components
scrapers = {
    'twitter': TwitterScraper(),
    'reddit': RedditScraper(),
    'github': GitHubScraper(),
    'instagram': InstagramScraper(),
    'news': NewsScraper()
}

# AI Models
gemini_summarizer = GeminiSummarizer()
sentiment_analyzer = SentimentAnalyzer()
ner_analyzer = NERAnalyzer()  # Fixed: Changed from ner_model to ner_analyzer
toxicity_analyzer = ToxicityAnalyzer()
report_generator = ReportGenerator()
face_analyzer = FacialRecognitionAnalyzer()

# Pydantic models
class AnalysisRequest(BaseModel):
    target_user: str
    platforms: List[str]
    ai_models: Optional[List[str]] = ["sentiment", "summary", "ner", "toxicity"]
    export_formats: Optional[List[str]] = ["json"]

class ChatAnalysisRequest(BaseModel):
    message: str
    context: Optional[Dict[str, Any]] = {}

class FacialRecognitionRequest(BaseModel):
    image_data: str  # Base64 encoded image
    search_platforms: Optional[List[str]] = ["twitter", "instagram", "linkedin"]

class TextAnalysisRequest(BaseModel):
    text: str

class SentimentAnalysisRequest(BaseModel):
    text: str

class NERRequest(BaseModel):
    text: str

class ToxicityAnalysisRequest(BaseModel):
    text: str

class ReportGenerationRequest(BaseModel):
    data: dict

# Global storage for investigations
investigations_storage = {}

@app.get("/")
async def root():
    """Root endpoint with system status"""
    return {
        "message": "🔍 OSINT Analysis Platform API",
        "version": "2.0.0",
        "status": "operational",
        "timestamp": datetime.now().isoformat(),
        "available_endpoints": [
            "/analyze",
            "/test-scrapers", 
            "/test-ai",
            "/chat-analysis",
            "/facial-recognition",
            "/health",
            "/summarize",
            "/sentiment",
            "/ner",
            "/toxicity",
            "/report"
        ]
    }

@app.get("/health")
async def health_check():
    """Health check endpoint"""
    try:
        # Test Gemini connection
        gemini_status = gemini_summarizer.test_connection()
        
        return {
            "status": "healthy",
            "timestamp": datetime.now().isoformat(),
            "components": {
                "scrapers": {name: "operational" for name in scrapers.keys()},
                "ai_models": {
                    "gemini": gemini_status.get("status", "error"),
                    "sentiment": "operational",
                    "ner": "operational", 
                    "toxicity": "operational"
                }
            },
            "gemini_details": gemini_status
        }
    except Exception as e:
        logger.error(f"Health check failed: {e}")
        return JSONResponse(
            status_code=500,
            content={
                "status": "unhealthy",
                "error": str(e),
                "timestamp": datetime.now().isoformat()
            }
        )

@app.post("/analyze")
async def analyze_target(request: AnalysisRequest, background_tasks: BackgroundTasks):
    """Main analysis endpoint"""
    investigation_id = f"inv_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{request.target_user}"
    
    try:
        logger.info(f"🎯 Starting analysis for: {request.target_user}")
        logger.info(f"📱 Platforms: {request.platforms}")
        logger.info(f"🤖 AI Models: {request.ai_models}")
        
        # Initialize investigation
        investigation = {
            "id": investigation_id,
            "target_user": request.target_user,
            "platforms": request.platforms,
            "ai_models": request.ai_models,
            "status": "running",
            "started_at": datetime.now().isoformat(),
            "results": {},
            "ai_analysis": {},
            "errors": []
        }
        
        investigations_storage[investigation_id] = investigation
        
        # Scrape data from each platform
        for platform in request.platforms:
            if platform in scrapers:
                try:
                    logger.info(f"🔍 Scraping {platform} for {request.target_user}")
                    scraper = scrapers[platform]
                    
                    if platform == 'twitter':
                        data = await scraper.scrape_user_data(request.target_user)
                    elif platform == 'reddit':
                        data = await scraper.scrape_user_data(request.target_user)
                    elif platform == 'github':
                        data = await scraper.scrape_user_data(request.target_user)
                    elif platform == 'instagram':
                        data = await scraper.scrape_user_data(request.target_user)
                    elif platform == 'news':
                        data = await scraper.search_news(request.target_user)
                    
                    investigation["results"][platform] = data
                    logger.info(f"✅ {platform} scraping completed")
                    
                except Exception as e:
                    error_msg = f"❌ {platform} scraping failed: {str(e)}"
                    logger.error(error_msg)
                    investigation["errors"].append(error_msg)
                    investigation["results"][platform] = {"error": str(e)}
            else:
                error_msg = f"❌ Unknown platform: {platform}"
                logger.warning(error_msg)
                investigation["errors"].append(error_msg)
        
        # AI Analysis
        if request.ai_models:
            logger.info("🤖 Starting AI analysis...")
            ai_results = {}
            
            # Collect all text content for analysis
            all_content = []
            for platform, data in investigation["results"].items():
                if isinstance(data, dict) and "error" not in data:
                    # Extract text from posts
                    for post in data.get("posts", []):
                        content = (post.get("content") or 
                                 post.get("caption") or 
                                 post.get("title") or 
                                 post.get("body") or 
                                 post.get("selftext") or "")
                        if content:
                            all_content.append(content)
                    
                    # Extract text from comments
                    for comment in data.get("comments", []):
                        content = comment.get("content") or comment.get("body") or ""
                        if content:
                            all_content.append(content)
                    
                    # Extract text from tweets
                    for tweet in data.get("tweets", []):
                        content = tweet.get("content") or ""
                        if content:
                            all_content.append(content)
            
            logger.info(f"📝 Collected {len(all_content)} text items for AI analysis")
            
            # Summary Analysis
            if "summary" in request.ai_models and all_content:
                try:
                    logger.info("📊 Generating summary...")
                    combined_text = "\n".join(all_content[:50])  # Limit content
                    summary_result = await gemini_summarizer.summarize(combined_text)
                    ai_results["summary"] = summary_result
                    logger.info("✅ Summary analysis completed")
                except Exception as e:
                    error_msg = f"❌ Summary analysis failed: {str(e)}"
                    logger.error(error_msg)
                    ai_results["summary"] = {"error": str(e)}
            
            # Profile Analysis
            if "profile_analysis" in request.ai_models:
                try:
                    logger.info("👤 Generating profile analysis...")
                    profile_result = await gemini_summarizer.analyze_profile(investigation["results"])
                    ai_results["profile_analysis"] = profile_result
                    logger.info("✅ Profile analysis completed")
                except Exception as e:
                    error_msg = f"❌ Profile analysis failed: {str(e)}"
                    logger.error(error_msg)
                    ai_results["profile_analysis"] = {"error": str(e)}
            
            # Sentiment Analysis
            if "sentiment" in request.ai_models and all_content:
                try:
                    logger.info("😊 Analyzing sentiment...")
                    sentiment_result = await gemini_summarizer.analyze_sentiment_and_emotions(all_content[:20])
                    ai_results["sentiment"] = sentiment_result
                    logger.info("✅ Sentiment analysis completed")
                except Exception as e:
                    error_msg = f"❌ Sentiment analysis failed: {str(e)}"
                    logger.error(error_msg)
                    ai_results["sentiment"] = {"error": str(e)}
            
            # NER Analysis - Fixed method call
            if "ner" in request.ai_models and all_content:
                try:
                    logger.info("🏷️ Extracting named entities...")
                    ner_result = await ner_analyzer.extract_entities_batch(all_content[:10])
                    ai_results["ner"] = ner_result
                    logger.info("✅ NER analysis completed")
                except Exception as e:
                    error_msg = f"❌ NER analysis failed: {str(e)}"
                    logger.error(error_msg)
                    ai_results["ner"] = {"error": str(e)}
            
            # Toxicity Analysis
            if "toxicity" in request.ai_models and all_content:
                try:
                    logger.info("⚠️ Analyzing toxicity...")
                    toxicity_result = await toxicity_analyzer.analyze_batch(all_content[:15])
                    ai_results["toxicity"] = toxicity_result
                    logger.info("✅ Toxicity analysis completed")
                except Exception as e:
                    error_msg = f"❌ Toxicity analysis failed: {str(e)}"
                    logger.error(error_msg)
                    ai_results["toxicity"] = {"error": str(e)}
            
            investigation["ai_analysis"] = ai_results
        
        # Update investigation status
        investigation["status"] = "completed"
        investigation["completed_at"] = datetime.now().isoformat()
        investigations_storage[investigation_id] = investigation
        
        logger.info(f"✅ Analysis completed for {request.target_user}")
        
        return {
            "investigation_id": investigation_id,
            "status": "completed",
            "target_user": request.target_user,
            "platforms_analyzed": len([p for p in request.platforms if p in investigation["results"] and "error" not in investigation["results"][p]]),
            "total_platforms": len(request.platforms),
            "ai_models_used": len(request.ai_models) if request.ai_models else 0,
            "errors": investigation["errors"],
            "results": investigation["results"],
            "ai_analysis": investigation["ai_analysis"],
            "completed_at": investigation["completed_at"]
        }
        
    except Exception as e:
        error_msg = f"❌ Analysis failed: {str(e)}"
        logger.error(error_msg)
        
        # Update investigation with error
        if investigation_id in investigations_storage:
            investigations_storage[investigation_id]["status"] = "failed"
            investigations_storage[investigation_id]["error"] = str(e)
        
        raise HTTPException(status_code=500, detail=error_msg)

@app.post("/chat-analysis")
async def chat_analysis(request: ChatAnalysisRequest):
    """AI-powered chat analysis using Gemini"""
    try:
        logger.info(f"💬 Processing chat message: {request.message[:50]}...")
        
        # Create context-aware prompt
        context = request.context or {}
        
        prompt = f"""
        You are an expert OSINT analyst assistant. A user is asking about their investigation data.
        
        **User Question:** {request.message}
        
        **Current Context:**
        - Selected User: {context.get('selectedUser', 'All users')}
        - Total Posts: {context.get('totalPosts', 0)}
        - High Risk Posts: {context.get('highRiskPosts', 0)}
        - Active Investigations: {context.get('investigations', 0)}
        - Emotion Distribution: {json.dumps(context.get('emotionDistribution', []))}
        
        Please provide a helpful, professional response as an OSINT analysis expert. 
        Be specific, actionable, and reference the context data when relevant.
        Use emojis and formatting to make the response engaging.
        
        If the user asks about:
        - Summary/Overview: Provide analysis statistics and key insights
        - Risk Assessment: Focus on high-risk content and security concerns
        - User Profiles: Give detailed behavioral analysis
        - Trends/Patterns: Discuss temporal and emotional patterns
        - Recommendations: Suggest next steps for investigation
        
        Keep responses concise but informative (max 500 words).
        """
        
        # Use Gemini for intelligent response
        if gemini_summarizer.enabled:
            response_data = await gemini_summarizer.model.generate_content_async(prompt)
            response_text = response_data.text.strip()
        else:
            # Fallback response
            response_text = generate_fallback_response(request.message, context)
        
        logger.info("✅ Chat analysis completed")
        
        return {
            "response": response_text,
            "model": "gemini-1.5-flash",
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"❌ Chat analysis failed: {str(e)}")
        
        # Fallback response
        fallback_response = generate_fallback_response(request.message, request.context)
        
        return {
            "response": fallback_response,
            "model": "fallback",
            "error": str(e),
            "timestamp": datetime.now().isoformat()
        }

def generate_fallback_response(message: str, context: Dict) -> str:
    """Generate fallback response when Gemini is unavailable"""
    message_lower = message.lower()
    
    if "summary" in message_lower or "overview" in message_lower:
        return f"""📊 **OSINT Analysis Summary**
        
**Current Investigation Status:**
- Total Posts Analyzed: {context.get('totalPosts', 0)}
- High Risk Content: {context.get('highRiskPosts', 0)} posts
- Active Investigations: {context.get('investigations', 0)}
- Selected User: {context.get('selectedUser', 'All users')}

**Key Insights:**
- The analysis covers multiple social media platforms
- Emotional patterns are tracked over time
- Risk assessment is performed on all content
- User behavior patterns are identified

**Recommendations:**
- Review high-risk content for security concerns
- Monitor emotional trends for behavioral changes
- Cross-reference findings across platforms
- Generate detailed reports for documentation

Would you like me to focus on any specific aspect of the analysis?"""

    elif "risk" in message_lower or "dangerous" in message_lower:
        return f"""⚠️ **Risk Assessment Report**
        
**High Risk Content Detected:**
- Critical/High Risk Posts: {context.get('highRiskPosts', 0)}
- Risk Categories: Threatening, Hateful, Harmful content
- Monitoring Status: Active surveillance recommended

**Risk Mitigation:**
- Flag concerning content for review
- Monitor user behavior patterns
- Document evidence for potential escalation
- Consider platform reporting if necessary

**Next Steps:**
- Review individual high-risk posts
- Analyze user connections and networks
- Generate comprehensive risk report
- Implement monitoring protocols

The system continuously monitors for concerning patterns and behaviors."""

    elif "user" in message_lower or "profile" in message_lower:
        selected_user = context.get('selectedUser')
        if selected_user:
            return f"""👤 **User Profile Analysis: {selected_user}**
            
**Digital Footprint:**
- Platform Activity: Multi-platform presence detected
- Content Volume: {context.get('totalPosts', 0)} posts analyzed
- Risk Assessment: Ongoing evaluation
- Behavioral Patterns: Under analysis

**Analysis Areas:**
- Communication style and tone
- Topic interests and focus areas
- Social connections and networks
- Temporal activity patterns
- Emotional expression patterns

**Investigation Status:**
- Data collection: Complete
- AI analysis: In progress
- Risk evaluation: Ongoing
- Report generation: Available

Click on specific posts in the timeline to see detailed analysis."""
        else:
            return f"""👥 **User Analysis Overview**
            
**Available Profiles:**
- Total users in database: Multiple profiles
- Analysis depth: Comprehensive behavioral profiling
- Risk assessment: Individual and collective
- Pattern recognition: Cross-platform analysis

**Analysis Capabilities:**
- Individual user deep-dive analysis
- Cross-platform behavior correlation
- Social network mapping
- Risk pattern identification
- Temporal behavior analysis

Select a specific user from the timeline to get detailed profile analysis."""

    else:
        return f"""🤖 **OSINT Analysis Assistant**
        
I can help you analyze:

📊 **Data Overview**: Current investigation statistics and insights
⚠️ **Risk Assessment**: High-risk content and security concerns
👤 **User Profiles**: Individual behavioral analysis and patterns
📈 **Trends**: Temporal and emotional pattern analysis
🔍 **Investigation**: Detailed findings and recommendations

**Current Context:**
- Posts: {context.get('totalPosts', 0)}
- High Risk: {context.get('highRiskPosts', 0)}
- Investigations: {context.get('investigations', 0)}
- Focus: {context.get('selectedUser', 'All users')}

What specific aspect would you like me to analyze?"""

@app.post("/facial-recognition")
async def facial_recognition_analysis(request: FacialRecognitionRequest):
    """Facial recognition and social media lookup feature"""
    try:
        logger.info("🔍 Starting facial recognition analysis...")
        
        # Step 1: Identify person from image
        identification_result = await face_analyzer.identify_person(request.image_data)
        
        if identification_result.get("error"):
            return {
                "status": "error",
                "error": identification_result["error"],
                "timestamp": datetime.now().isoformat()
            }
        
        identified_person = identification_result.get("identified_person")
        
        if not identified_person:
            return {
                "status": "no_match",
                "message": "No matching person found in database",
                "faces_detected": identification_result.get("faces_detected", 0),
                "timestamp": datetime.now().isoformat()
            }
        
        logger.info(f"✅ Person identified: {identified_person['name']}")
        
        # Step 2: Find social media profiles
        social_profiles = await face_analyzer.find_social_media_profiles(
            identified_person["name"], 
            request.search_platforms
        )
        
        # Step 3: Fetch news articles
        news_articles = await face_analyzer.fetch_news_articles(identified_person["name"])
        
        # Step 4: Generate AI summary using Gemini
        ai_summary = {}
        if gemini_summarizer.enabled and news_articles:
            try:
                # Combine news content for summarization
                news_content = "\n".join([
                    f"Title: {article['title']}\nDescription: {article['description']}"
                    for article in news_articles
                ])
                
                summary_result = await gemini_summarizer.summarize(
                    f"News about {identified_person['name']}:\n{news_content}",
                    max_length=800
                )
                ai_summary = summary_result
                logger.info("✅ AI summary generated")
            except Exception as e:
                logger.error(f"❌ AI summary failed: {str(e)}")
                ai_summary = {"error": str(e)}
        
        # Step 5: Generate comprehensive report
        report_data = {
            "identified_person": identified_person,
            "social_profiles": social_profiles,
            "news_articles": news_articles,
            "ai_summary": ai_summary
        }
        
        comprehensive_report = await face_analyzer.generate_comprehensive_report(report_data)
        
        # Return complete analysis
        return {
            "status": "success",
            "identified_person": identified_person,
            "social_media_profiles": social_profiles,
            "news_articles": news_articles,
            "ai_summary": ai_summary,
            "comprehensive_report": comprehensive_report,
            "analysis_metadata": {
                "faces_detected": identification_result.get("faces_detected", 0),
                "platforms_searched": len(request.search_platforms),
                "news_articles_found": len(news_articles),
                "ai_analysis_status": "completed" if ai_summary and "error" not in ai_summary else "failed"
            },
            "timestamp": datetime.now().isoformat()
        }
        
    except Exception as e:
        logger.error(f"❌ Facial recognition analysis failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/summarize")
async def summarize_text(request: TextAnalysisRequest):
    """Summarize text using Gemini."""
    try:
        if not gemini_summarizer.enabled:
            raise HTTPException(status_code=503, detail="Gemini summarization is currently disabled.")
        
        result = await gemini_summarizer.summarize(request.text)
        return {"status": "success", "summary": result, "timestamp": datetime.now().isoformat()}
    except Exception as e:
        logger.error(f"Summarization failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/sentiment")
async def analyze_sentiment(request: SentimentAnalysisRequest):
    """Analyze sentiment of text."""
    try:
        result = await sentiment_analyzer.analyze_sentiment(request.text)
        return {"status": "success", "sentiment": result, "timestamp": datetime.now().isoformat()}
    except Exception as e:
        logger.error(f"Sentiment analysis failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/ner")
async def recognize_entities(request: NERRequest):
    """Recognize named entities in text."""
    try:
        result = await ner_analyzer.extract_entities_single(request.text)  # Fixed method call
        return {"status": "success", "entities": result, "timestamp": datetime.now().isoformat()}
    except Exception as e:
        logger.error(f"NER failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/toxicity")
async def analyze_toxicity(request: ToxicityAnalysisRequest):
    """Analyze toxicity of text."""
    try:
        result = await toxicity_analyzer.analyze_toxicity(request.text)
        return {"status": "success", "toxicity": result, "timestamp": datetime.now().isoformat()}
    except Exception as e:
        logger.error(f"Toxicity analysis failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/report")
async def generate_report(request: ReportGenerationRequest):
    """Generate a report from given data."""
    try:
        result = await report_generator.generate_report(request.data)
        return {"status": "success", "report": result, "timestamp": datetime.now().isoformat()}
    except Exception as e:
        logger.error(f"Report generation failed: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/test-scrapers")
async def test_scrapers():
    """Test all scrapers"""
    results = {}
    
    for name, scraper in scrapers.items():
        try:
            logger.info(f"Testing {name} scraper...")
            
            if name == 'twitter':
                result = await scraper.scrape_user_data("elonmusk")
            elif name == 'reddit':
                result = await scraper.scrape_user_data("spez")
            elif name == 'github':
                result = await scraper.scrape_user_data("torvalds")
            elif name == 'instagram':
                result = await scraper.scrape_user_data("instagram")
            elif name == 'news':
                result = await scraper.search_news("technology")
            
            results[name] = {
                "status": "success",
                "data_points": len(result.get("posts", [])) + len(result.get("comments", [])) + len(result.get("tweets", [])),
                "sample": str(result)[:200] + "..." if result else "No data"
            }
            logger.info(f"✅ {name} scraper test passed")
            
        except Exception as e:
            logger.error(f"❌ {name} scraper test failed: {e}")
            results[name] = {
                "status": "error",
                "error": str(e)
            }
    
    return {
        "timestamp": datetime.now().isoformat(),
        "results": results,
        "summary": f"{sum(1 for r in results.values() if r['status'] == 'success')}/{len(results)} scrapers working"
    }

@app.get("/test-ai")
async def test_ai_models():
    """Test all AI models"""
    results = {}
    
    # Test Gemini
    try:
        logger.info("Testing Gemini summarizer...")
        gemini_test = gemini_summarizer.test_connection()
        results["gemini"] = gemini_test
        logger.info("✅ Gemini test completed")
    except Exception as e:
        logger.error(f"❌ Gemini test failed: {e}")
        results["gemini"] = {"status": "error", "error": str(e)}
    
    # Test other AI models
    test_text = "This is a test message for AI analysis."
    
    try:
        logger.info("Testing sentiment analyzer...")
        sentiment_result = await sentiment_analyzer.analyze_text(test_text)
        results["sentiment"] = {"status": "success", "result": sentiment_result}
        logger.info("✅ Sentiment analyzer test passed")
    except Exception as e:
        logger.error(f"❌ Sentiment analyzer test failed: {e}")
        results["sentiment"] = {"status": "error", "error": str(e)}
    
    try:
        logger.info("Testing NER analyzer...")
        ner_result = await ner_analyzer.extract_entities_single(test_text)  # Fixed method call
        results["ner"] = {"status": "success", "result": ner_result}
        logger.info("✅ NER analyzer test passed")
    except Exception as e:
        logger.error(f"❌ NER analyzer test failed: {e}")
        results["ner"] = {"status": "error", "error": str(e)}
    
    try:
        logger.info("Testing toxicity analyzer...")
        toxicity_result = await toxicity_analyzer.analyze_text(test_text)
        results["toxicity"] = {"status": "success", "result": toxicity_result}
        logger.info("✅ Toxicity analyzer test passed")
    except Exception as e:
        logger.error(f"❌ Toxicity analyzer test failed: {e}")
        results["toxicity"] = {"status": "error", "error": str(e)}
    
    return {
        "timestamp": datetime.now().isoformat(),
        "results": results,
        "summary": f"{sum(1 for r in results.values() if r.get('status') == 'success')}/{len(results)} AI models working"
    }

if __name__ == "__main__":
    logger.info("🚀 Starting OSINT Analysis Platform...")
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )