# import google.generativeai as genai
# import asyncio
# from typing import Dict, List
# import os
# from datetime import datetime

# class GeminiSummarizer:
#     def __init__(self):
#         api_key = os.getenv('GEMINI_API_KEY')
#         if api_key:
#             genai.configure(api_key=api_key)
#             self.model = genai.GenerativeModel("gemini-1.5-flash")
#             self.enabled = True
#         else:
#             print("Gemini API key not found. Summarization will be disabled.")
#             self.enabled = False
    
#     async def summarize(self, text: str, max_length: int = 500) -> Dict:
#         if not self.enabled:
#             return {'error': 'Gemini API not configured'}
        
#         try:
#             if not text or len(text.strip()) == 0:
#                 return {'error': 'Empty text provided'}
            
#             # Limit input text to avoid API limits
#             input_text = text[:8000] if len(text) > 8000 else text
            
#             prompt = f"""
#             Analyze the following social media content and provide:
#             1. A concise summary (max {max_length} words)
#             2. Key themes and topics
#             3. Notable patterns or behaviors
#             4. Risk assessment (if any concerning content)
#             5. Overall tone and sentiment
            
#             Content to analyze:
#             {input_text}
            
#             Please format your response as a structured analysis.
#             """
            
#             response = self.model.generate_content(prompt)
            
#             return {
#                 'summary': response.text,
#                 'input_length': len(input_text),
#                 'generated_at': datetime.now().isoformat(),
#                 'model': 'gemini-1.5-flash'
#             }
            
#         except Exception as e:
#             return {'error': f'Gemini summarization failed: {str(e)}'}
    
#     async def analyze_profile(self, profile_data: Dict) -> Dict:
#         if not self.enabled:
#             return {'error': 'Gemini API not configured'}
        
#         try:
#             # Combine all text content from profile
#             all_content = []
            
#             for platform, data in profile_data.items():
#                 if isinstance(data, dict):
#                     if 'posts' in data:
#                         all_content.extend([post.get('content', '') for post in data['posts']])
#                     if 'comments' in data:
#                         all_content.extend([comment.get('content', '') for comment in data['comments']])
#                     if 'tweets' in data:
#                         all_content.extend([tweet.get('content', '') for tweet in data['tweets']])
            
#             combined_text = ' '.join(all_content)[:10000]  # Limit to 10k chars
            
#             prompt = f"""
#             Analyze this user's social media activity across multiple platforms and provide:
            
#             1. BEHAVIORAL PROFILE:
#                - Communication style and patterns
#                - Interests and topics of focus
#                - Activity levels and engagement patterns
            
#             2. CONTENT ANALYSIS:
#                - Main themes and subjects discussed
#                - Sentiment and emotional patterns
#                - Language use and tone
            
#             3. RISK ASSESSMENT:
#                - Any concerning patterns or content
#                - Potential security or safety considerations
#                - Overall risk level (LOW/MEDIUM/HIGH)
            
#             4. SUMMARY:
#                - Key findings and insights
#                - Notable characteristics
#                - Recommendations for further investigation
            
#             User content:
#             {combined_text}
            
#             Provide a professional OSINT analysis report.
#             """
            
#             response = self.model.generate_content(prompt)
            
#             return {
#                 'profile_analysis': response.text,
#                 'platforms_analyzed': list(profile_data.keys()),
#                 'content_volume': len(combined_text),
#                 'generated_at': datetime.now().isoformat(),
#                 'model': 'gemini-1.5-flash'
#             }
            
#         except Exception as e:
#             return {'error': f'Profile analysis failed: {str(e)}'}
    
#     async def generate_threat_assessment(self, analysis_results: Dict) -> Dict:
#         if not self.enabled:
#             return {'error': 'Gemini API not configured'}
        
#         try:
#             # Extract key information from analysis results
#             sentiment_data = analysis_results.get('sentiment', {})
#             toxicity_data = analysis_results.get('toxicity', {})
#             entities_data = analysis_results.get('entities', {})
            
#             prompt = f"""
#             Based on the following OSINT analysis results, provide a comprehensive threat assessment:
            
#             SENTIMENT ANALYSIS:
#             - Overall sentiment: {sentiment_data.get('overall_sentiment', 'Unknown')}
#             - Negative percentage: {sentiment_data.get('negative_percentage', 0)}%
#             - Positive percentage: {sentiment_data.get('positive_percentage', 0)}%
            
#             TOXICITY ANALYSIS:
#             - Toxicity percentage: {toxicity_data.get('toxicity_percentage', 0)}%
#             - Risk level: {toxicity_data.get('risk_level', 'Unknown')}
#             - High-risk content count: {len(toxicity_data.get('high_risk_content', []))}
            
#             ENTITY ANALYSIS:
#             - Total entities found: {entities_data.get('total_entities', 0)}
#             - Unique entities: {entities_data.get('unique_entities', 0)}
            
#             Please provide:
#             1. THREAT LEVEL (LOW/MEDIUM/HIGH/CRITICAL)
#             2. KEY RISK FACTORS
#             3. BEHAVIORAL INDICATORS
#             4. RECOMMENDATIONS FOR MONITORING
#             5. POTENTIAL ESCALATION TRIGGERS
            
#             Format as a professional security assessment.
#             """
            
#             response = self.model.generate_content(prompt)
            
#             return {
#                 'threat_assessment': response.text,
#                 'assessment_date': datetime.now().isoformat(),
#                 'model': 'gemini-1.5-flash',
#                 'data_sources': list(analysis_results.keys())
#             }
            
#         except Exception as e:
#             return {'error': f'Threat assessment failed: {str(e)}'}


# !new above good 

# import google.generativeai as genai
# import asyncio
# from typing import Dict, List
# import os
# from datetime import datetime

# class GeminiSummarizer:
#     def __init__(self):
#         # Use the provided API key
#         api_key = os.getenv('GEMINI_API_KEY', '')
        
#         if api_key:
#             try:
#                 genai.configure(api_key=api_key)
#                 self.model = genai.GenerativeModel("gemini-1.5-flash")
#                 self.enabled = True
                
#                 # Test the model
#                 test_response = self.model.generate_content("Test")
#                 print(f"✓ Gemini API initialized and tested successfully")
                
#             except Exception as e:
#                 print(f"✗ Gemini API initialization failed: {str(e)}")
#                 self.enabled = False
#         else:
#             print("✗ Gemini API key not found. Summarization will be disabled.")
#             self.enabled = False
    
#     async def summarize(self, text: str, max_length: int = 500) -> Dict:
#         if not self.enabled:
#             return {'error': 'Gemini API not configured'}
        
#         try:
#             if not text or len(text.strip()) == 0:
#                 return {'error': 'Empty text provided'}
            
#             # Limit input text to avoid API limits
#             input_text = text[:8000] if len(text) > 8000 else text
            
#             prompt = f"""
#             Analyze the following social media content and provide:
#             1. A concise summary (max {max_length} words)
#             2. Key themes and topics
#             3. Notable patterns or behaviors
#             4. Risk assessment (if any concerning content)
#             5. Overall tone and sentiment
            
#             Content to analyze:
#             {input_text}
            
#             Please format your response as a structured analysis.
#             """
            
#             response = self.model.generate_content(prompt)
            
#             return {
#                 'summary': response.text,
#                 'input_length': len(input_text),
#                 'generated_at': datetime.now().isoformat(),
#                 'model': 'gemini-1.5-flash'
#             }
            
#         except Exception as e:
#             return {'error': f'Gemini summarization failed: {str(e)}'}
    
#     async def analyze_profile(self, profile_data: Dict) -> Dict:
#         if not self.enabled:
#             return {'error': 'Gemini API not configured'}
        
#         try:
#             # Combine all text content from profile
#             all_content = []
            
#             for platform, data in profile_data.items():
#                 if isinstance(data, dict):
#                     if 'posts' in data:
#                         all_content.extend([post.get('content', post.get('caption', post.get('title', post.get('body', post.get('selftext', ''))))) for post in data['posts']])
#                     if 'comments' in data:
#                         all_content.extend([comment.get('content', comment.get('body', '')) for comment in data['comments']])
#                     if 'tweets' in data:
#                         all_content.extend([tweet.get('content', '') for tweet in data['tweets']])
            
#             combined_text = ' '.join([content for content in all_content if content])[:10000]  # Limit to 10k chars
            
#             if not combined_text:
#                 return {'error': 'No content found for analysis'}
            
#             prompt = f"""
#             Analyze this user's social media activity across multiple platforms and provide:
            
#             1. BEHAVIORAL PROFILE:
#                - Communication style and patterns
#                - Interests and topics of focus
#                - Activity levels and engagement patterns
            
#             2. CONTENT ANALYSIS:
#                - Main themes and subjects discussed
#                - Sentiment and emotional patterns
#                - Language use and tone
            
#             3. RISK ASSESSMENT:
#                - Any concerning patterns or content
#                - Potential security or safety considerations
#                - Overall risk level (LOW/MEDIUM/HIGH)
            
#             4. SUMMARY:
#                - Key findings and insights
#                - Notable characteristics
#                - Recommendations for further investigation
            
#             User content:
#             {combined_text}
            
#             Provide a professional OSINT analysis report.
#             """
            
#             response = self.model.generate_content(prompt)
            
#             return {
#                 'profile_analysis': response.text,
#                 'platforms_analyzed': list(profile_data.keys()),
#                 'content_volume': len(combined_text),
#                 'generated_at': datetime.now().isoformat(),
#                 'model': 'gemini-1.5-flash'
#             }
            
#         except Exception as e:
#             return {'error': f'Profile analysis failed: {str(e)}'}
    
#     async def generate_threat_assessment(self, analysis_results: Dict) -> Dict:
#         if not self.enabled:
#             return {'error': 'Gemini API not configured'}
        
#         try:
#             # Extract key information from analysis results
#             sentiment_data = analysis_results.get('sentiment', {})
#             toxicity_data = analysis_results.get('toxicity', {})
#             entities_data = analysis_results.get('entities', {})
            
#             prompt = f"""
#             Based on the following OSINT analysis results, provide a comprehensive threat assessment:
            
#             SENTIMENT ANALYSIS:
#             - Overall sentiment: {sentiment_data.get('overall_sentiment', 'Unknown')}
#             - Negative percentage: {sentiment_data.get('negative_percentage', 0)}%
#             - Positive percentage: {sentiment_data.get('positive_percentage', 0)}%
            
#             TOXICITY ANALYSIS:
#             - Toxicity percentage: {toxicity_data.get('toxicity_percentage', 0)}%
#             - Risk level: {toxicity_data.get('risk_level', 'Unknown')}
#             - High-risk content count: {len(toxicity_data.get('high_risk_content', []))}
            
#             ENTITY ANALYSIS:
#             - Total entities found: {entities_data.get('total_entities', 0)}
#             - Unique entities: {entities_data.get('unique_entities', 0)}
            
#             Please provide:
#             1. THREAT LEVEL (LOW/MEDIUM/HIGH/CRITICAL)
#             2. KEY RISK FACTORS
#             3. BEHAVIORAL INDICATORS
#             4. RECOMMENDATIONS FOR MONITORING
#             5. POTENTIAL ESCALATION TRIGGERS
            
#             Format as a professional security assessment.
#             """
            
#             response = self.model.generate_content(prompt)
            
#             return {
#                 'threat_assessment': response.text,
#                 'assessment_date': datetime.now().isoformat(),
#                 'model': 'gemini-1.5-flash',
#                 'data_sources': list(analysis_results.keys())
#             }
            
#         except Exception as e:
#             return {'error': f'Threat assessment failed: {str(e)}'}


# !new above best 
# import os
# import asyncio
# import logging
# from typing import Dict, List, Optional
# import json

# logger = logging.getLogger(__name__)

# try:
#     import google.generativeai as genai
#     GENAI_AVAILABLE = True
#     logger.info("✓ Google Generative AI available")
# except ImportError:
#     GENAI_AVAILABLE = False
#     logger.warning("⚠️ Google Generative AI not available")

# class GeminiSummarizer:
#     def __init__(self):
#         self.model = None
#         self.api_key = None
        
#         if GENAI_AVAILABLE:
#             self._initialize_gemini()
#         else:
#             logger.warning("⚠️ Gemini summarizer initialized without Google AI")

#     def _initialize_gemini(self):
#         """Initialize Gemini AI with API key"""
#         try:
#             # Try multiple sources for API key
#             api_key_sources = [
#                 os.getenv('GEMINI_API_KEY',''),
#                 os.getenv('GOOGLE_API_KEY'),
#                 ""  # Your provided key
#             ]
            
#             for api_key in api_key_sources:
#                 if api_key:
#                     self.api_key = api_key.strip()
#                     break
            
#             if not self.api_key:
#                 logger.error("❌ No Gemini API key found")
#                 return False
            
#             # Configure Gemini
#             genai.configure(api_key=self.api_key)
            
#             # Initialize model
#             self.model = genai.GenerativeModel('gemini-1.5-flash')
            
#             # Test the model
#             test_response = self.model.generate_content("Hello, this is a test.")
#             logger.info("✓ Gemini model initialized and tested successfully")
#             return True
            
#         except Exception as e:
#             logger.error(f"❌ Failed to initialize Gemini: {str(e)}")
#             self.model = None
#             return False

#     async def summarize(self, text: str, max_length: int = 500) -> Dict:
#         """Generate a summary of the provided text"""
#         try:
#             if not self.model:
#                 return {
#                     'error': 'Gemini model not available',
#                     'summary': 'AI summarization unavailable'
#                 }
            
#             if not text or len(text.strip()) < 10:
#                 return {
#                     'error': 'Insufficient text for summarization',
#                     'summary': 'Not enough content to summarize'
#                 }
            
#             # Truncate text if too long
#             if len(text) > 10000:
#                 text = text[:10000] + "..."
            
#             prompt = f"""
#             Please provide a comprehensive summary of the following text content. 
#             Focus on key themes, main points, and any notable patterns or concerns.
#             Keep the summary under {max_length} characters.
            
#             Text to summarize:
#             {text}
            
#             Summary:
#             """
            
#             response = await asyncio.to_thread(
#                 self.model.generate_content, 
#                 prompt
#             )
            
#             summary = response.text.strip()
            
#             return {
#                 'summary': summary,
#                 'original_length': len(text),
#                 'summary_length': len(summary),
#                 'compression_ratio': len(summary) / len(text) if len(text) > 0 else 0,
#                 'model': 'gemini-1.5-flash'
#             }
            
#         except Exception as e:
#             logger.error(f"❌ Summarization failed: {str(e)}")
#             return {
#                 'error': str(e),
#                 'summary': 'Failed to generate summary'
#             }

#     async def analyze_profile(self, platform_data: Dict) -> Dict:
#         """Analyze user profile across platforms"""
#         try:
#             if not self.model:
#                 return {
#                     'error': 'Gemini model not available',
#                     'analysis': 'AI analysis unavailable'
#                 }
            
#             # Extract key information from platform data
#             analysis_data = {}
#             total_content = []
            
#             for platform, data in platform_data.items():
#                 if platform == 'ai_analysis' or not isinstance(data, dict):
#                     continue
                    
#                 platform_info = {
#                     'platform': platform,
#                     'posts': len(data.get('posts', [])),
#                     'comments': len(data.get('comments', [])),
#                     'tweets': len(data.get('tweets', [])),
#                     'repositories': len(data.get('repositories', [])),
#                     'user_info': data.get('user_info', {})
#                 }
                
#                 analysis_data[platform] = platform_info
                
#                 # Collect content for analysis
#                 for post in data.get('posts', [])[:10]:  # Limit to 10 posts per platform
#                     content = post.get('content') or post.get('caption') or post.get('title') or ''
#                     if content:
#                         total_content.append(f"[{platform}] {content}")
                
#                 for comment in data.get('comments', [])[:10]:
#                     content = comment.get('content') or comment.get('body') or ''
#                     if content:
#                         total_content.append(f"[{platform}] {content}")
                
#                 for tweet in data.get('tweets', [])[:10]:
#                     content = tweet.get('content') or ''
#                     if content:
#                         total_content.append(f"[{platform}] {content}")
            
#             # Create analysis prompt
#             content_sample = "\n".join(total_content[:50])  # Limit content
            
#             prompt = f"""
#             Analyze the following user's digital footprint across multiple platforms.
#             Provide insights about their personality, interests, communication style, and any notable patterns.
            
#             Platform Summary:
#             {json.dumps(analysis_data, indent=2)}
            
#             Sample Content:
#             {content_sample}
            
#             Please provide:
#             1. Personality Assessment
#             2. Key Interests and Topics
#             3. Communication Style
#             4. Activity Patterns
#             5. Potential Concerns or Red Flags
#             6. Overall Digital Persona Summary
            
#             Analysis:
#             """
            
#             response = await asyncio.to_thread(
#                 self.model.generate_content, 
#                 prompt
#             )
            
#             analysis = response.text.strip()
            
#             return {
#                 'profile_analysis': analysis,
#                 'platforms_analyzed': list(analysis_data.keys()),
#                 'total_content_items': len(total_content),
#                 'model': 'gemini-1.5-flash'
#             }
            
#         except Exception as e:
#             logger.error(f"❌ Profile analysis failed: {str(e)}")
#             return {
#                 'error': str(e),
#                 'analysis': 'Failed to generate profile analysis'
#             }

#     async def analyze_sentiment_batch(self, texts: List[str]) -> Dict:
#         """Analyze sentiment for a batch of texts"""
#         try:
#             if not self.model:
#                 return {
#                     'error': 'Gemini model not available',
#                     'sentiments': []
#                 }
            
#             if not texts:
#                 return {
#                     'error': 'No texts provided',
#                     'sentiments': []
#                 }
            
#             # Limit batch size
#             texts = texts[:20]
            
#             # Create batch analysis prompt
#             text_list = "\n".join([f"{i+1}. {text[:200]}" for i, text in enumerate(texts)])
            
#             prompt = f"""
#             Analyze the sentiment and emotional tone of the following texts.
#             For each text, provide:
#             - Sentiment (Positive, Negative, Neutral)
#             - Emotion (Happy, Sad, Angry, Fearful, etc.)
#             - Confidence score (0-1)
#             - Brief explanation
            
#             Texts to analyze:
#             {text_list}
            
#             Please respond in JSON format:
#             {{
#                 "results": [
#                     {{
#                         "text_id": 1,
#                         "sentiment": "Positive",
#                         "emotion": "Happy",
#                         "confidence": 0.85,
#                         "explanation": "Brief explanation"
#                     }}
#                 ]
#             }}
#             """
            
#             response = await asyncio.to_thread(
#                 self.model.generate_content, 
#                 prompt
#             )
            
#             # Try to parse JSON response
#             try:
#                 result = json.loads(response.text.strip())
#                 return result
#             except json.JSONDecodeError:
#                 # Fallback if JSON parsing fails
#                 return {
#                     'raw_response': response.text,
#                     'error': 'Failed to parse JSON response'
#                 }
            
#         except Exception as e:
#             logger.error(f"❌ Batch sentiment analysis failed: {str(e)}")
#             return {
#                 'error': str(e),
#                 'sentiments': []
#             }

#     def test_connection(self) -> Dict:
#         """Test Gemini connection"""
#         try:
#             if not self.model:
#                 return {
#                     'status': 'error',
#                     'message': 'Gemini model not initialized'
#                 }
            
#             test_response = self.model.generate_content("Hello, this is a connection test.")
            
#             return {
#                 'status': 'success',
#                 'message': 'Gemini connection working',
#                 'response_length': len(test_response.text),
#                 'model': 'gemini-1.5-flash'
#             }
            
#         except Exception as e:
#             return {
#                 'status': 'error',
#                 'message': str(e)
#             }


# !new above working bes 

# import os
# import asyncio
# import logging
# from typing import Dict, List, Optional
# import json
# from datetime import datetime

# logger = logging.getLogger(__name__)

# try:
#     import google.generativeai as genai
#     GENAI_AVAILABLE = True
#     logger.info("✓ Google Generative AI available")
# except ImportError:
#     GENAI_AVAILABLE = False
#     logger.warning("⚠️ Google Generative AI not available")

# class GeminiSummarizer:
#     def __init__(self):
#         self.model = None
#         self.api_key = None
#         self.enabled = False
        
#         if GENAI_AVAILABLE:
#             self.enabled = self._initialize_gemini()
#         else:
#             logger.warning("⚠️ Gemini summarizer initialized without Google AI")

#     def _initialize_gemini(self):
#         """Initialize Gemini AI with API key"""
#         try:
#             # Try multiple sources for API key
#             api_key_sources = [
#                 os.getenv('GEMINI_API_KEY'),
#                 os.getenv('GOOGLE_API_KEY'),
#                 '',  # Your first key
#                 ''   # Your second key
#             ]
            
#             for api_key in api_key_sources:
#                 if api_key and api_key.strip():
#                     try:
#                         self.api_key = api_key.strip()
#                         logger.info(f"Trying API key: {self.api_key[:10]}...")
                        
#                         # Configure Gemini
#                         genai.configure(api_key=self.api_key)
                        
#                         # Initialize model
#                         self.model = genai.GenerativeModel('gemini-1.5-flash')
                        
#                         # Test the model
#                         test_response = self.model.generate_content("Hello, this is a test.")
#                         logger.info(f"✓ Gemini model initialized and tested successfully with key: {self.api_key[:10]}...")
#                         return True
                        
#                     except Exception as e:
#                         logger.warning(f"⚠️ API key {self.api_key[:10]}... failed: {str(e)}")
#                         continue
            
#             logger.error("❌ All Gemini API keys failed")
#             return False
            
#         except Exception as e:
#             logger.error(f"❌ Failed to initialize Gemini: {str(e)}")
#             self.model = None
#             return False

#     async def summarize(self, text: str, max_length: int = 500) -> Dict:
#         """Generate a summary of the provided text"""
#         try:
#             if not self.enabled or not self.model:
#                 logger.error("❌ Gemini model not available for summarization")
#                 return {
#                     'error': 'Gemini model not available',
#                     'summary': 'AI summarization unavailable - model not initialized'
#                 }
            
#             if not text or len(text.strip()) < 10:
#                 return {
#                     'error': 'Insufficient text for summarization',
#                     'summary': 'Not enough content to summarize'
#                 }
            
#             # Truncate text if too long
#             if len(text) > 8000:
#                 text = text[:8000] + "..."
            
#             prompt = f"""
#             Analyze and summarize the following social media content. Provide:
            
#             1. **Key Themes**: Main topics and subjects discussed
#             2. **Behavioral Patterns**: Communication style and activity patterns  
#             3. **Sentiment Overview**: Overall emotional tone
#             4. **Notable Content**: Any interesting or concerning posts
#             5. **Summary**: Concise overview in under {max_length} characters
            
#             Content to analyze:
#             {text}
            
#             Please provide a structured analysis:
#             """
            
#             logger.info("🤖 Sending request to Gemini...")
#             response = await asyncio.to_thread(
#                 self.model.generate_content, 
#                 prompt
#             )
            
#             summary = response.text.strip()
#             logger.info(f"✓ Gemini summarization completed: {len(summary)} characters")
            
#             return {
#                 'summary': summary,
#                 'original_length': len(text),
#                 'summary_length': len(summary),
#                 'compression_ratio': len(summary) / len(text) if len(text) > 0 else 0,
#                 'model': 'gemini-1.5-flash',
#                 'generated_at': datetime.now().isoformat()
#             }
            
#         except Exception as e:
#             logger.error(f"❌ Summarization failed: {str(e)}")
#             return {
#                 'error': f'Summarization failed: {str(e)}',
#                 'summary': 'Failed to generate summary due to API error'
#             }

#     async def analyze_profile(self, platform_data: Dict) -> Dict:
#         """Analyze user profile across platforms"""
#         try:
#             if not self.enabled or not self.model:
#                 logger.error("❌ Gemini model not available for profile analysis")
#                 return {
#                     'error': 'Gemini model not available',
#                     'analysis': 'AI profile analysis unavailable - model not initialized'
#                 }
            
#             # Extract key information from platform data
#             analysis_data = {}
#             total_content = []
            
#             for platform, data in platform_data.items():
#                 if platform == 'ai_analysis' or not isinstance(data, dict) or 'error' in data:
#                     continue
                
#                 platform_info = {
#                     'platform': platform,
#                     'posts': len(data.get('posts', [])),
#                     'comments': len(data.get('comments', [])),
#                     'tweets': len(data.get('tweets', [])),
#                     'repositories': len(data.get('repositories', [])),
#                     'user_info': data.get('user_info', {})
#                 }
                
#                 analysis_data[platform] = platform_info
                
#                 # Collect content for analysis
#                 for post in data.get('posts', [])[:5]:  # Limit to 5 posts per platform
#                     content = (post.get('content') or 
#                              post.get('caption') or 
#                              post.get('title') or 
#                              post.get('body') or 
#                              post.get('selftext') or '')
#                     if content and len(content.strip()) > 10:
#                         total_content.append(f"[{platform.upper()}] {content[:200]}")
                
#                 for comment in data.get('comments', [])[:5]:
#                     content = comment.get('content') or comment.get('body') or ''
#                     if content and len(content.strip()) > 10:
#                         total_content.append(f"[{platform.upper()}] {content[:200]}")
                
#                 for tweet in data.get('tweets', [])[:5]:
#                     content = tweet.get('content') or ''
#                     if content and len(content.strip()) > 10:
#                         total_content.append(f"[{platform.upper()}] {content[:200]}")
            
#             if not total_content:
#                 return {
#                     'error': 'No content found for analysis',
#                     'analysis': 'No meaningful content available for profile analysis'
#                 }
            
#             # Create analysis prompt
#             content_sample = "\n".join(total_content[:20])  # Limit content
            
#             prompt = f"""
#             Conduct a comprehensive OSINT profile analysis based on the following digital footprint:
            
#             **Platform Activity Summary:**
#             {json.dumps(analysis_data, indent=2)}
            
#             **Sample Content:**
#             {content_sample}
            
#             Please provide a detailed analysis covering:
            
#             🔍 **DIGITAL PERSONA ANALYSIS**
#             1. **Personality Assessment**: Communication style, tone, and behavioral patterns
#             2. **Interest Profile**: Main topics, hobbies, and areas of focus
#             3. **Activity Patterns**: Posting frequency, engagement style, platform preferences
#             4. **Communication Style**: Language use, formality level, interaction patterns
            
#             ⚠️ **RISK ASSESSMENT**
#             5. **Content Concerns**: Any problematic, controversial, or concerning content
#             6. **Security Indicators**: Privacy awareness, information sharing patterns
#             7. **Behavioral Red Flags**: Unusual patterns or concerning behaviors
            
#             📊 **SUMMARY**
#             8. **Overall Profile**: Concise summary of the digital persona
#             9. **Key Findings**: Most notable discoveries and insights
#             10. **Recommendations**: Suggestions for further investigation if needed
            
#             Provide a professional OSINT analysis report:
#             """
            
#             logger.info("🤖 Sending profile analysis request to Gemini...")
#             response = await asyncio.to_thread(
#                 self.model.generate_content, 
#                 prompt
#             )
            
#             analysis = response.text.strip()
#             logger.info(f"✓ Gemini profile analysis completed: {len(analysis)} characters")
            
#             return {
#                 'profile_analysis': analysis,
#                 'platforms_analyzed': list(analysis_data.keys()),
#                 'total_content_items': len(total_content),
#                 'model': 'gemini-1.5-flash',
#                 'generated_at': datetime.now().isoformat()
#             }
            
#         except Exception as e:
#             logger.error(f"❌ Profile analysis failed: {str(e)}")
#             return {
#                 'error': f'Profile analysis failed: {str(e)}',
#                 'analysis': 'Failed to generate profile analysis due to API error'
#             }

#     async def analyze_sentiment_and_emotions(self, texts: List[str]) -> Dict:
#         """Analyze sentiment and emotions for a batch of texts using Gemini"""
#         try:
#             if not self.enabled or not self.model:
#                 return {
#                     'error': 'Gemini model not available',
#                     'results': []
#                 }
            
#             if not texts:
#                 return {
#                     'error': 'No texts provided',
#                     'results': []
#                 }
            
#             # Limit batch size and clean texts
#             clean_texts = []
#             for text in texts[:15]:  # Limit to 15 texts
#                 if text and isinstance(text, str) and len(text.strip()) > 5:
#                     clean_texts.append(text.strip()[:300])  # Limit text length
            
#             if not clean_texts:
#                 return {
#                     'error': 'No valid texts for analysis',
#                     'results': []
#                 }
            
#             # Create batch analysis prompt
#             text_list = "\n".join([f"{i+1}. {text}" for i, text in enumerate(clean_texts)])
            
#             prompt = f"""
#             Analyze the sentiment and emotional content of the following social media posts/comments.
            
#             For each text, determine:
#             - **Sentiment**: Positive, Negative, or Neutral
#             - **Primary Emotion**: Happy, Sad, Angry, Fearful, Supportive, Mocking, Hateful, Threatening, Sarcastic, or Neutral
#             - **Confidence**: How confident you are (0.0 to 1.0)
#             - **Risk Level**: LOW, MEDIUM, HIGH, or CRITICAL (based on potential harm or toxicity)
#             - **Explanation**: Brief reason for the classification
            
#             **Texts to analyze:**
#             {text_list}
            
#             **Response Format (JSON):**
#             {{
#                 "analysis_summary": {{
#                     "total_texts": {len(clean_texts)},
#                     "positive_count": 0,
#                     "negative_count": 0,
#                     "neutral_count": 0,
#                     "high_risk_count": 0
#                 }},
#                 "detailed_results": [
#                     {{
#                         "text_id": 1,
#                         "sentiment": "Positive",
#                         "emotion": "Happy",
#                         "confidence": 0.85,
#                         "risk_level": "LOW",
#                         "explanation": "Expresses joy and positivity"
#                     }}
#                 ]
#             }}
            
#             Provide accurate sentiment analysis:
#             """
            
#             logger.info(f"🤖 Sending sentiment analysis request for {len(clean_texts)} texts...")
#             response = await asyncio.to_thread(
#                 self.model.generate_content, 
#                 prompt
#             )
            
#             # Try to parse JSON response
#             try:
#                 # Clean the response text
#                 response_text = response.text.strip()
#                 if response_text.startswith('\`\`\`json'):
#                     response_text = response_text[7:]
#                 if response_text.endswith('\`\`\`'):
#                     response_text = response_text[:-3]
                
#                 result = json.loads(response_text.strip())
#                 logger.info("✓ Gemini sentiment analysis completed successfully")
                
#                 # Add metadata
#                 result['model'] = 'gemini-1.5-flash'
#                 result['generated_at'] = datetime.now().isoformat()
#                 result['input_texts_count'] = len(clean_texts)
                
#                 return result
                
#             except json.JSONDecodeError as e:
#                 logger.warning(f"⚠️ JSON parsing failed, using fallback: {str(e)}")
                
#                 # Fallback: create structured response from raw text
#                 return {
#                     'analysis_summary': {
#                         'total_texts': len(clean_texts),
#                         'positive_count': response.text.lower().count('positive'),
#                         'negative_count': response.text.lower().count('negative'),
#                         'neutral_count': response.text.lower().count('neutral'),
#                         'high_risk_count': response.text.lower().count('high') + response.text.lower().count('critical')
#                     },
#                     'raw_response': response.text,
#                     'error': 'JSON parsing failed, raw response provided',
#                     'model': 'gemini-1.5-flash'
#                 }
            
#         except Exception as e:
#             logger.error(f"❌ Sentiment analysis failed: {str(e)}")
#             return {
#                 'error': f'Sentiment analysis failed: {str(e)}',
#                 'results': []
#             }

#     def test_connection(self) -> Dict:
#         """Test Gemini connection"""
#         try:
#             if not self.enabled or not self.model:
#                 return {
#                     'status': 'error',
#                     'message': 'Gemini model not initialized',
#                     'api_key_status': 'Not configured'
#                 }
            
#             test_response = self.model.generate_content("Hello, this is a connection test. Please respond with 'Connection successful'.")
            
#             return {
#                 'status': 'success',
#                 'message': 'Gemini connection working perfectly',
#                 'response': test_response.text.strip(),
#                 'response_length': len(test_response.text),
#                 'model': 'gemini-1.5-flash',
#                 'api_key_status': f'Active ({self.api_key[:10]}...)'
#             }
            
#         except Exception as e:
#             return {
#                 'status': 'error',
#                 'message': f'Connection test failed: {str(e)}',
#                 'api_key_status': f'Error with key: {self.api_key[:10] if self.api_key else "None"}...'
#             }



#! above besto

# import os
# import asyncio
# import logging
# from typing import Dict, List, Optional
# import json
# from datetime import datetime

# logger = logging.getLogger(__name__)

# try:
#     import google.generativeai as genai
#     GENAI_AVAILABLE = True
#     logger.info("✓ Google Generative AI available")
# except ImportError:
#     GENAI_AVAILABLE = False
#     logger.warning("⚠️ Google Generative AI not available")

# class GeminiSummarizer:
#     def __init__(self):
#         self.model = None
#         self.api_key = None
#         self.enabled = False
        
#         if GENAI_AVAILABLE:
#             self.enabled = self._initialize_gemini()
#         else:
#             logger.warning("⚠️ Gemini summarizer initialized without Google AI")

#     def _initialize_gemini(self):
#         """Initialize Gemini AI with API key"""
#         try:
#             # Try multiple sources for API key
#             api_key_sources = [
#                 os.getenv('GEMINI_API_KEY'),
#                 os.getenv('GOOGLE_API_KEY'),
#                 '',
#                 ''
#             ]
            
#             for api_key in api_key_sources:
#                 if api_key and api_key.strip():
#                     try:
#                         self.api_key = api_key.strip()
#                         logger.info(f"Trying API key: {self.api_key[:10]}...")
                        
#                         # Configure Gemini
#                         genai.configure(api_key=self.api_key)
                        
#                         # Initialize model
#                         self.model = genai.GenerativeModel('gemini-1.5-flash')
                        
#                         # Test the model
#                         test_response = self.model.generate_content("Hello, this is a test.")
#                         logger.info(f"✓ Gemini model initialized and tested successfully with key: {self.api_key[:10]}...")
#                         return True
                        
#                     except Exception as e:
#                         logger.warning(f"⚠️ API key {self.api_key[:10]}... failed: {str(e)}")
#                         continue
            
#             logger.error("❌ All Gemini API keys failed")
#             return False
            
#         except Exception as e:
#             logger.error(f"❌ Failed to initialize Gemini: {str(e)}")
#             self.model = None
#             return False

#     async def is_person_deceased(self, name: str) -> Dict:
#         """Check if a person is deceased using Gemini"""
#         try:
#             if not self.enabled or not self.model:
#                 return {"error": "Gemini not available", "deceased": False}
                
#             prompt = f"""
#             Determine if {name} is deceased. Consider only verified historical records and reliable sources.
#             Respond in JSON format with these keys:
#             - deceased: true or false
#             - certainty: high, medium, or low
#             - explanation: brief reason
            
#             Example response:
#             {{"deceased": true, "certainty": "high", "explanation": "Historical records confirm death in 1931"}}
#             """
            
#             response = await asyncio.to_thread(self.model.generate_content, prompt)
#             try:
#                 # Extract JSON from response
#                 response_text = response.text.strip()
#                 if response_text.startswith('```json'):
#                     response_text = response_text[7:]
#                 if response_text.endswith('```'):
#                     response_text = response_text[:-3]
#                 return json.loads(response_text)
#             except:
#                 # Fallback if JSON parsing fails
#                 return {
#                     "deceased": "true" in response.text.lower(),
#                     "certainty": "medium",
#                     "explanation": "Gemini response parsing failed"
#                 }
#         except Exception as e:
#             logger.error(f"Deceased check failed: {str(e)}")
#             return {"error": str(e), "deceased": False}

#     async def filter_social_profiles(self, name: str, profiles: Dict) -> Dict:
#         """Filter social media profiles using Gemini"""
#         try:
#             if not self.enabled or not self.model:
#                 return profiles
                
#             prompt = f"""
#             Filter social media profiles for {name}. Only keep OFFICIAL, VERIFIED profiles.
#             Remove any fan accounts, unofficial pages, or irrelevant links.
            
#             Input profiles (JSON format):
#             {json.dumps(profiles, indent=2)}
            
#             Return filtered profiles in the SAME JSON structure. Only include:
#             - Official verified accounts
#             - Wikipedia if available
#             - Official memorial pages if deceased
#             - Remove all others
            
#             Respond with ONLY the filtered JSON.
#             """
            
#             response = await asyncio.to_thread(self.model.generate_content, prompt)
            
#             try:
#                 # Extract JSON from response
#                 response_text = response.text.strip()
#                 if response_text.startswith('```json'):
#                     response_text = response_text[7:]
#                 if response_text.endswith('```'):
#                     response_text = response_text[:-3]
#                 return json.loads(response_text)
#             except json.JSONDecodeError:
#                 logger.warning("Failed to parse filtered profiles, returning original")
#                 return profiles
                
#         except Exception as e:
#             logger.error(f"Profile filtering failed: {str(e)}")
#             return profiles

#     async def summarize(self, text: str, max_length: int = 500) -> Dict:
#         """Generate a summary of the provided text"""
#         try:
#             if not self.enabled or not self.model:
#                 logger.error("❌ Gemini model not available for summarization")
#                 return {
#                     'error': 'Gemini model not available',
#                     'summary': 'AI summarization unavailable - model not initialized'
#                 }
            
#             if not text or len(text.strip()) < 10:
#                 return {
#                     'error': 'Insufficient text for summarization',
#                     'summary': 'Not enough content to summarize'
#                 }
            
#             # Truncate text if too long
#             if len(text) > 8000:
#                 text = text[:8000] + "..."
            
#             prompt = f"""
#             Analyze and summarize the following social media content. Provide:
            
#             1. **Key Themes**: Main topics and subjects discussed
#             2. **Behavioral Patterns**: Communication style and activity patterns  
#             3. **Sentiment Overview**: Overall emotional tone
#             4. **Notable Content**: Any interesting or concerning posts
#             5. **Summary**: Concise overview in under {max_length} characters
            
#             Content to analyze:
#             {text}
            
#             Please provide a structured analysis:
#             """
            
#             logger.info("🤖 Sending request to Gemini...")
#             response = await asyncio.to_thread(
#                 self.model.generate_content, 
#                 prompt
#             )
            
#             summary = response.text.strip()
#             logger.info(f"✓ Gemini summarization completed: {len(summary)} characters")
            
#             return {
#                 'summary': summary,
#                 'original_length': len(text),
#                 'summary_length': len(summary),
#                 'compression_ratio': len(summary) / len(text) if len(text) > 0 else 0,
#                 'model': 'gemini-1.5-flash',
#                 'generated_at': datetime.now().isoformat()
#             }
            
#         except Exception as e:
#             logger.error(f"❌ Summarization failed: {str(e)}")
#             return {
#                 'error': f'Summarization failed: {str(e)}',
#                 'summary': 'Failed to generate summary due to API error'
#             }

#     async def analyze_profile(self, platform_data: Dict) -> Dict:
#         """Analyze user profile across platforms"""
#         try:
#             if not self.enabled or not self.model:
#                 logger.error("❌ Gemini model not available for profile analysis")
#                 return {
#                     'error': 'Gemini model not available',
#                     'analysis': 'AI profile analysis unavailable - model not initialized'
#                 }
            
#             # Extract key information from platform data
#             analysis_data = {}
#             total_content = []
            
#             for platform, data in platform_data.items():
#                 if platform == 'ai_analysis' or not isinstance(data, dict) or 'error' in data:
#                     continue
                
#                 platform_info = {
#                     'platform': platform,
#                     'posts': len(data.get('posts', [])),
#                     'comments': len(data.get('comments', [])),
#                     'tweets': len(data.get('tweets', [])),
#                     'repositories': len(data.get('repositories', [])),
#                     'user_info': data.get('user_info', {})
#                 }
                
#                 analysis_data[platform] = platform_info
                
#                 # Collect content for analysis
#                 for post in data.get('posts', [])[:5]:  # Limit to 5 posts per platform
#                     content = (post.get('content') or 
#                              post.get('caption') or 
#                              post.get('title') or 
#                              post.get('body') or 
#                              post.get('selftext') or '')
#                     if content and len(content.strip()) > 10:
#                         total_content.append(f"[{platform.upper()}] {content[:200]}")
                
#                 for comment in data.get('comments', [])[:5]:
#                     content = comment.get('content') or comment.get('body') or ''
#                     if content and len(content.strip()) > 10:
#                         total_content.append(f"[{platform.upper()}] {content[:200]}")
                
#                 for tweet in data.get('tweets', [])[:5]:
#                     content = tweet.get('content') or ''
#                     if content and len(content.strip()) > 10:
#                         total_content.append(f"[{platform.upper()}] {content[:200]}")
            
#             if not total_content:
#                 return {
#                     'error': 'No content found for analysis',
#                     'analysis': 'No meaningful content available for profile analysis'
#                 }
            
#             # Create analysis prompt
#             content_sample = "\n".join(total_content[:20])  # Limit content
            
#             prompt = f"""
#             Conduct a comprehensive OSINT profile analysis based on the following digital footprint:
            
#             **Platform Activity Summary:**
#             {json.dumps(analysis_data, indent=2)}
            
#             **Sample Content:**
#             {content_sample}
            
#             Please provide a detailed analysis covering:
            
#             🔍 **DIGITAL PERSONA ANALYSIS**
#             1. **Personality Assessment**: Communication style, tone, and behavioral patterns
#             2. **Interest Profile**: Main topics, hobbies, and areas of focus
#             3. **Activity Patterns**: Posting frequency, engagement style, platform preferences
#             4. **Communication Style**: Language use, formality level, interaction patterns
            
#             ⚠️ **RISK ASSESSMENT**
#             5. **Content Concerns**: Any problematic, controversial, or concerning content
#             6. **Security Indicators**: Privacy awareness, information sharing patterns
#             7. **Behavioral Red Flags**: Unusual patterns or concerning behaviors
            
#             📊 **SUMMARY**
#             8. **Overall Profile**: Concise summary of the digital persona
#             9. **Key Findings**: Most notable discoveries and insights
#             10. **Recommendations**: Suggestions for further investigation if needed
            
#             Provide a professional OSINT analysis report:
#             """
            
#             logger.info("🤖 Sending profile analysis request to Gemini...")
#             response = await asyncio.to_thread(
#                 self.model.generate_content, 
#                 prompt
#             )
            
#             analysis = response.text.strip()
#             logger.info(f"✓ Gemini profile analysis completed: {len(analysis)} characters")
            
#             return {
#                 'profile_analysis': analysis,
#                 'platforms_analyzed': list(analysis_data.keys()),
#                 'total_content_items': len(total_content),
#                 'model': 'gemini-1.5-flash',
#                 'generated_at': datetime.now().isoformat()
#             }
            
#         except Exception as e:
#             logger.error(f"❌ Profile analysis failed: {str(e)}")
#             return {
#                 'error': f'Profile analysis failed: {str(e)}',
#                 'analysis': 'Failed to generate profile analysis due to API error'
#             }

#     async def analyze_sentiment_and_emotions(self, texts: List[str]) -> Dict:
#         """Analyze sentiment and emotions for a batch of texts using Gemini"""
#         try:
#             if not self.enabled or not self.model:
#                 return {
#                     'error': 'Gemini model not available',
#                     'results': []
#                 }
            
#             if not texts:
#                 return {
#                     'error': 'No texts provided',
#                     'results': []
#                 }
            
#             # Limit batch size and clean texts
#             clean_texts = []
#             for text in texts[:15]:  # Limit to 15 texts
#                 if text and isinstance(text, str) and len(text.strip()) > 5:
#                     clean_texts.append(text.strip()[:300])  # Limit text length
            
#             if not clean_texts:
#                 return {
#                     'error': 'No valid texts for analysis',
#                     'results': []
#                 }
            
#             # Create batch analysis prompt
#             text_list = "\n".join([f"{i+1}. {text}" for i, text in enumerate(clean_texts)])
            
#             prompt = f"""
#             Analyze the sentiment and emotional content of the following social media posts/comments.
            
#             For each text, determine:
#             - **Sentiment**: Positive, Negative, or Neutral
#             - **Primary Emotion**: Happy, Sad, Angry, Fearful, Supportive, Mocking, Hateful, Threatening, Sarcastic, or Neutral
#             - **Confidence**: How confident you are (0.0 to 1.0)
#             - **Risk Level**: LOW, MEDIUM, HIGH, or CRITICAL (based on potential harm or toxicity)
#             - **Explanation**: Brief reason for the classification
            
#             **Texts to analyze:**
#             {text_list}
            
#             **Response Format (JSON):**
#             {{
#                 "analysis_summary": {{
#                     "total_texts": {len(clean_texts)},
#                     "positive_count": 0,
#                     "negative_count": 0,
#                     "neutral_count": 0,
#                     "high_risk_count": 0
#                 }},
#                 "detailed_results": [
#                     {{
#                         "text_id": 1,
#                         "sentiment": "Positive",
#                         "emotion": "Happy",
#                         "confidence": 0.85,
#                         "risk_level": "LOW",
#                         "explanation": "Expresses joy and positivity"
#                     }}
#                 ]
#             }}
            
#             Provide accurate sentiment analysis:
#             """
            
#             logger.info(f"🤖 Sending sentiment analysis request for {len(clean_texts)} texts...")
#             response = await asyncio.to_thread(
#                 self.model.generate_content, 
#                 prompt
#             )
            
#             # Try to parse JSON response
#             try:
#                 # Clean the response text
#                 response_text = response.text.strip()
#                 if response_text.startswith('```json'):
#                     response_text = response_text[7:]
#                 if response_text.endswith('```'):
#                     response_text = response_text[:-3]
                
#                 result = json.loads(response_text.strip())
#                 logger.info("✓ Gemini sentiment analysis completed successfully")
                
#                 # Add metadata
#                 result['model'] = 'gemini-1.5-flash'
#                 result['generated_at'] = datetime.now().isoformat()
#                 result['input_texts_count'] = len(clean_texts)
                
#                 return result
                
#             except json.JSONDecodeError as e:
#                 logger.warning(f"⚠️ JSON parsing failed, using fallback: {str(e)}")
                
#                 # Fallback: create structured response from raw text
#                 return {
#                     'analysis_summary': {
#                         'total_texts': len(clean_texts),
#                         'positive_count': response.text.lower().count('positive'),
#                         'negative_count': response.text.lower().count('negative'),
#                         'neutral_count': response.text.lower().count('neutral'),
#                         'high_risk_count': response.text.lower().count('high') + response.text.lower().count('critical')
#                     },
#                     'raw_response': response.text,
#                     'error': 'JSON parsing failed, raw response provided',
#                     'model': 'gemini-1.5-flash'
#                 }
            
#         except Exception as e:
#             logger.error(f"❌ Sentiment analysis failed: {str(e)}")
#             return {
#                 'error': f'Sentiment analysis failed: {str(e)}',
#                 'results': []
#             }

#     def test_connection(self) -> Dict:
#         """Test Gemini connection"""
#         try:
#             if not self.enabled or not self.model:
#                 return {
#                     'status': 'error',
#                     'message': 'Gemini model not initialized',
#                     'api_key_status': 'Not configured'
#                 }
            
#             test_response = self.model.generate_content("Hello, this is a connection test. Please respond with 'Connection successful'.")
            
#             return {
#                 'status': 'success',
#                 'message': 'Gemini connection working perfectly',
#                 'response': test_response.text.strip(),
#                 'response_length': len(test_response.text),
#                 'model': 'gemini-1.5-flash',
#                 'api_key_status': f'Active ({self.api_key[:10]}...)'
#             }
            
#         except Exception as e:
#             return {
#                 'status': 'error',
#                 'message': f'Connection test failed: {str(e)}',
#                 'api_key_status': f'Error with key: {self.api_key[:10] if self.api_key else "None"}...'
#             }



# above bestooooooooo


import os
import asyncio
import logging
from typing import Dict, List, Optional
import json
from datetime import datetime

logger = logging.getLogger(__name__)

try:
    import google.generativeai as genai
    GENAI_AVAILABLE = True
    logger.info("✓ Google Generative AI available")
except ImportError:
    GENAI_AVAILABLE = False
    logger.warning("⚠️ Google Generative AI not available")

class GeminiSummarizer:
    def __init__(self):
        self.model = None
        self.api_key = None
        self.enabled = False
        
        if GENAI_AVAILABLE:
            self.enabled = self._initialize_gemini()
        else:
            logger.warning("⚠️ Gemini summarizer initialized without Google AI")

    def _initialize_gemini(self):
        """Initialize Gemini AI with API key"""
        try:
            # Try multiple sources for API key
            api_key_sources = [
                os.getenv('GEMINI_API_KEY'),
                os.getenv('GOOGLE_API_KEY'),
                'YOUR_FIRST_GOOGLE_API_KEY',
                'YOUR_SECOND_GOOGLE_API_KEY'
            ]
            
            for api_key in api_key_sources:
                if api_key and api_key.strip():
                    try:
                        self.api_key = api_key.strip()
                        logger.info(f"Trying API key: {self.api_key[:10]}...")
                        
                        # Configure Gemini
                        genai.configure(api_key=self.api_key)
                        
                        # Initialize model
                        self.model = genai.GenerativeModel('gemini-1.5-flash')
                        
                        # Test the model
                        test_response = self.model.generate_content("Hello, this is a test.")
                        logger.info(f"✓ Gemini model initialized and tested successfully with key: {self.api_key[:10]}...")
                        return True
                        
                    except Exception as e:
                        logger.warning(f"⚠️ API key {self.api_key[:10]}... failed: {str(e)}")
                        continue
            
            logger.error("❌ All Gemini API keys failed")
            return False
            
        except Exception as e:
            logger.error(f"❌ Failed to initialize Gemini: {str(e)}")
            self.model = None
            return False

    async def is_person_deceased(self, name: str) -> Dict:
        """Check if a person is deceased using Gemini"""
        try:
            if not self.enabled or not self.model:
                return {"error": "Gemini not available", "deceased": False}
                
            prompt = f"""
            Determine if {name} is deceased. Consider only verified historical records and reliable sources.
            Respond in JSON format with these keys:
            - deceased: true or false
            - certainty: high, medium, or low
            - explanation: brief reason
            
            Example response:
            {{"deceased": true, "certainty": "high", "explanation": "Historical records confirm death in 1931"}}
            """
            
            response = await asyncio.to_thread(self.model.generate_content, prompt)
            try:
                # Extract JSON from response
                response_text = response.text.strip()
                if response_text.startswith('```json'):
                    response_text = response_text[7:]
                if response_text.endswith('```'):
                    response_text = response_text[:-3]
                return json.loads(response_text)
            except:
                # Fallback if JSON parsing fails
                return {
                    "deceased": "true" in response.text.lower(),
                    "certainty": "medium",
                    "explanation": "Gemini response parsing failed"
                }
        except Exception as e:
            logger.error(f"Deceased check failed: {str(e)}")
            return {"error": str(e), "deceased": False}

    async def filter_social_profiles(self, name: str, profiles: Dict) -> Dict:
        """Filter social media profiles using Gemini"""
        try:
            if not self.enabled or not self.model:
                return profiles
                
            prompt = f"""
            Filter social media profiles for {name}. Only keep OFFICIAL, VERIFIED profiles.
            Remove any fan accounts, unofficial pages, or irrelevant links.
            
            Input profiles (JSON format):
            {json.dumps(profiles, indent=2)}
            
            Return filtered profiles in the SAME JSON structure. Only include:
            - Official verified accounts
            - Wikipedia if available
            - Official memorial pages if deceased
            - Remove all others
            
            Respond with ONLY the filtered JSON.
            """
            
            response = await asyncio.to_thread(self.model.generate_content, prompt)
            
            try:
                # Extract JSON from response
                response_text = response.text.strip()
                if response_text.startswith('```json'):
                    response_text = response_text[7:]
                if response_text.endswith('```'):
                    response_text = response_text[:-3]
                return json.loads(response_text)
            except json.JSONDecodeError:
                logger.warning("Failed to parse filtered profiles, returning original")
                return profiles
                
        except Exception as e:
            logger.error(f"Profile filtering failed: {str(e)}")
            return profiles

    async def summarize(self, text: str, max_length: int = 500) -> Dict:
        """Generate a summary of the provided text"""
        try:
            if not self.enabled or not self.model:
                logger.error("❌ Gemini model not available for summarization")
                return {
                    'error': 'Gemini model not available',
                    'summary': 'AI summarization unavailable - model not initialized'
                }
            
            if not text or len(text.strip()) < 10:
                return {
                    'error': 'Insufficient text for summarization',
                    'summary': 'Not enough content to summarize'
                }
            
            # Truncate text if too long
            if len(text) > 8000:
                text = text[:8000] + "..."
            
            prompt = f"""
            Analyze and summarize the following social media content. Provide:
            
            1. **Key Themes**: Main topics and subjects discussed
            2. **Behavioral Patterns**: Communication style and activity patterns  
            3. **Sentiment Overview**: Overall emotional tone
            4. **Notable Content**: Any interesting or concerning posts
            5. **Summary**: Concise overview in under {max_length} characters
            
            Content to analyze:
            {text}
            
            Please provide a structured analysis:
            """
            
            logger.info("🤖 Sending request to Gemini...")
            response = await asyncio.to_thread(
                self.model.generate_content, 
                prompt
            )
            
            summary = response.text.strip()
            logger.info(f"✓ Gemini summarization completed: {len(summary)} characters")
            
            return {
                'summary': summary,
                'original_length': len(text),
                'summary_length': len(summary),
                'compression_ratio': len(summary) / len(text) if len(text) > 0 else 0,
                'model': 'gemini-1.5-flash',
                'generated_at': datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"❌ Summarization failed: {str(e)}")
            return {
                'error': f'Summarization failed: {str(e)}',
                'summary': 'Failed to generate summary due to API error'
            }

    async def analyze_profile(self, platform_data: Dict) -> Dict:
        """Analyze user profile across platforms"""
        try:
            if not self.enabled or not self.model:
                logger.error("❌ Gemini model not available for profile analysis")
                return {
                    'error': 'Gemini model not available',
                    'analysis': 'AI profile analysis unavailable - model not initialized'
                }
            
            # Extract key information from platform data
            analysis_data = {}
            total_content = []
            
            for platform, data in platform_data.items():
                if platform == 'ai_analysis' or not isinstance(data, dict) or 'error' in data:
                    continue
                
                platform_info = {
                    'platform': platform,
                    'posts': len(data.get('posts', [])),
                    'comments': len(data.get('comments', [])),
                    'tweets': len(data.get('tweets', [])),
                    'repositories': len(data.get('repositories', [])),
                    'user_info': data.get('user_info', {})
                }
                
                analysis_data[platform] = platform_info
                
                # Collect content for analysis
                for post in data.get('posts', [])[:5]:  # Limit to 5 posts per platform
                    content = (post.get('content') or 
                             post.get('caption') or 
                             post.get('title') or 
                             post.get('body') or 
                             post.get('selftext') or '')
                    if content and len(content.strip()) > 10:
                        total_content.append(f"[{platform.upper()}] {content[:200]}")
                
                for comment in data.get('comments', [])[:5]:
                    content = comment.get('content') or comment.get('body') or ''
                    if content and len(content.strip()) > 10:
                        total_content.append(f"[{platform.upper()}] {content[:200]}")
                
                for tweet in data.get('tweets', [])[:5]:
                    content = tweet.get('content') or ''
                    if content and len(content.strip()) > 10:
                        total_content.append(f"[{platform.upper()}] {content[:200]}")
            
            if not total_content:
                return {
                    'error': 'No content found for analysis',
                    'analysis': 'No meaningful content available for profile analysis'
                }
            
            # Create analysis prompt
            content_sample = "\n".join(total_content[:20])  # Limit content
            
            prompt = f"""
            Conduct a comprehensive OSINT profile analysis based on the following digital footprint:
            
            **Platform Activity Summary:**
            {json.dumps(analysis_data, indent=2)}
            
            **Sample Content:**
            {content_sample}
            
            Please provide a detailed analysis covering:
            
            🔍 **DIGITAL PERSONA ANALYSIS**
            1. **Personality Assessment**: Communication style, tone, and behavioral patterns
            2. **Interest Profile**: Main topics, hobbies, and areas of focus
            3. **Activity Patterns**: Posting frequency, engagement style, platform preferences
            4. **Communication Style**: Language use, formality level, interaction patterns
            
            ⚠️ **RISK ASSESSMENT**
            5. **Content Concerns**: Any problematic, controversial, or concerning content
            6. **Security Indicators**: Privacy awareness, information sharing patterns
            7. **Behavioral Red Flags**: Unusual patterns or concerning behaviors
            
            📊 **SUMMARY**
            8. **Overall Profile**: Concise summary of the digital persona
            9. **Key Findings**: Most notable discoveries and insights
            10. **Recommendations**: Suggestions for further investigation if needed
            
            Provide a professional OSINT analysis report:
            """
            
            logger.info("🤖 Sending profile analysis request to Gemini...")
            response = await asyncio.to_thread(
                self.model.generate_content, 
                prompt
            )
            
            analysis = response.text.strip()
            logger.info(f"✓ Gemini profile analysis completed: {len(analysis)} characters")
            
            return {
                'profile_analysis': analysis,
                'platforms_analyzed': list(analysis_data.keys()),
                'total_content_items': len(total_content),
                'model': 'gemini-1.5-flash',
                'generated_at': datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"❌ Profile analysis failed: {str(e)}")
            return {
                'error': f'Profile analysis failed: {str(e)}',
                'analysis': 'Failed to generate profile analysis due to API error'
            }

    async def analyze_sentiment_and_emotions(self, texts: List[str]) -> Dict:
        """Analyze sentiment and emotions for a batch of texts using Gemini"""
        try:
            if not self.enabled or not self.model:
                return {
                    'error': 'Gemini model not available',
                    'results': []
                }
            
            if not texts:
                return {
                    'error': 'No texts provided',
                    'results': []
                }
            
            # Limit batch size and clean texts
            clean_texts = []
            for text in texts[:15]:  # Limit to 15 texts
                if text and isinstance(text, str) and len(text.strip()) > 5:
                    clean_texts.append(text.strip()[:300])  # Limit text length
            
            if not clean_texts:
                return {
                    'error': 'No valid texts for analysis',
                    'results': []
                }
            
            # Create batch analysis prompt
            text_list = "\n".join([f"{i+1}. {text}" for i, text in enumerate(clean_texts)])
            
            prompt = f"""
            Analyze the sentiment and emotional content of the following social media posts/comments.
            
            For each text, determine:
            - **Sentiment**: Positive, Negative, or Neutral
            - **Primary Emotion**: Happy, Sad, Angry, Fearful, Supportive, Mocking, Hateful, Threatening, Sarcastic, or Neutral
            - **Confidence**: How confident you are (0.0 to 1.0)
            - **Risk Level**: LOW, MEDIUM, HIGH, or CRITICAL (based on potential harm or toxicity)
            - **Explanation**: Brief reason for the classification
            
            **Texts to analyze:**
            {text_list}
            
            **Response Format (JSON):**
            {{
                "analysis_summary": {{
                    "total_texts": {len(clean_texts)},
                    "positive_count": 0,
                    "negative_count": 0,
                    "neutral_count": 0,
                    "high_risk_count": 0
                }},
                "detailed_results": [
                    {{
                        "text_id": 1,
                        "sentiment": "Positive",
                        "emotion": "Happy",
                        "confidence": 0.85,
                        "risk_level": "LOW",
                        "explanation": "Expresses joy and positivity"
                    }}
                ]
            }}
            
            Provide accurate sentiment analysis:
            """
            
            logger.info(f"🤖 Sending sentiment analysis request for {len(clean_texts)} texts...")
            response = await asyncio.to_thread(
                self.model.generate_content, 
                prompt
            )
            
            # Try to parse JSON response
            try:
                # Clean the response text
                response_text = response.text.strip()
                if response_text.startswith('```json'):
                    response_text = response_text[7:]
                if response_text.endswith('```'):
                    response_text = response_text[:-3]
                
                result = json.loads(response_text.strip())
                logger.info("✓ Gemini sentiment analysis completed successfully")
                
                # Add metadata
                result['model'] = 'gemini-1.5-flash'
                result['generated_at'] = datetime.now().isoformat()
                result['input_texts_count'] = len(clean_texts)
                
                return result
                
            except json.JSONDecodeError as e:
                logger.warning(f"⚠️ JSON parsing failed, using fallback: {str(e)}")
                
                # Fallback: create structured response from raw text
                return {
                    'analysis_summary': {
                        'total_texts': len(clean_texts),
                        'positive_count': response.text.lower().count('positive'),
                        'negative_count': response.text.lower().count('negative'),
                        'neutral_count': response.text.lower().count('neutral'),
                        'high_risk_count': response.text.lower().count('high') + response.text.lower().count('critical')
                    },
                    'raw_response': response.text,
                    'error': 'JSON parsing failed, raw response provided',
                    'model': 'gemini-1.5-flash'
                }
            
        except Exception as e:
            logger.error(f"❌ Sentiment analysis failed: {str(e)}")
            return {
                'error': f'Sentiment analysis failed: {str(e)}',
                'results': []
            }

    async def generate_timeline(self, name: str, news_articles: List[Dict]) -> List[Dict]:
        """Generate a timeline of key events using Gemini"""
        try:
            if not self.enabled or not self.model:
                logger.error("❌ Gemini model not available for timeline generation")
                return []
                
            if not news_articles:
                logger.warning("⚠️ No news articles provided for timeline generation")
                return []
            
            # Limit the number of articles and format them
            limited_articles = news_articles[:20]  # Limit to 20 articles
            news_text = "\n".join([
                f"{i+1}. {article.get('title', 'No title')} "
                f"({article.get('published_at', 'No date')[:10] if article.get('published_at') else 'No date'}) - "
                f"{article.get('description', 'No description')[:200]}"
                for i, article in enumerate(limited_articles)
            ])
            
            prompt = f"""
            Create a chronological timeline of key events for {name} based on these news articles.
            Include only significant events, achievements, controversies, and milestones.
            Focus on the most important and impactful events.
            
            News Articles:
            {news_text}
            
            Respond in JSON format with this exact structure:
            {{
                "timeline": [
                    {{
                        "date": "YYYY-MM-DD",
                        "title": "Brief event title",
                        "description": "Detailed description of the event",
                        "significance": "high/medium/low",
                        "source": "Article title or source"
                    }}
                ]
            }}
            
            Guidelines:
            - Sort events chronologically (oldest to newest)
            - Include only 5-10 most significant events
            - Use actual dates from the articles when available
            - Mark significance as: high (major achievements/controversies), medium (notable events), low (minor mentions)
            - Keep descriptions concise but informative
            
            Generate the timeline JSON:
            """
            
            logger.info(f"🤖 Generating timeline for {name} from {len(limited_articles)} articles...")
            response = await asyncio.to_thread(
                self.model.generate_content, 
                prompt
            )
            
            try:
                # Extract JSON from response
                response_text = response.text.strip()
                if response_text.startswith('```json'):
                    response_text = response_text[7:]
                if response_text.endswith('```'):
                    response_text = response_text[:-3]
                
                data = json.loads(response_text.strip())
                timeline = data.get("timeline", [])
                
                # Validate timeline entries
                validated_timeline = []
                for event in timeline:
                    if isinstance(event, dict) and event.get('title') and event.get('description'):
                        # Ensure all required fields exist
                        validated_event = {
                            'date': event.get('date', 'Unknown'),
                            'title': event.get('title', 'Unknown Event'),
                            'description': event.get('description', 'No description'),
                            'significance': event.get('significance', 'medium'),
                            'source': event.get('source', 'Unknown source')
                        }
                        validated_timeline.append(validated_event)
                
                logger.info(f"✓ Timeline generation completed: {len(validated_timeline)} events")
                return validated_timeline
                
            except json.JSONDecodeError as e:
                logger.error(f"❌ Failed to parse timeline JSON: {str(e)}")
                logger.error(f"Raw response: {response.text[:500]}...")
                return []
                
        except Exception as e:
            logger.error(f"❌ Timeline generation failed: {str(e)}")
            return []

    def test_connection(self) -> Dict:
        """Test Gemini connection"""
        try:
            if not self.enabled or not self.model:
                return {
                    'status': 'error',
                    'message': 'Gemini model not initialized',
                    'api_key_status': 'Not configured'
                }
            
            test_response = self.model.generate_content("Hello, this is a connection test. Please respond with 'Connection successful'.")
            
            return {
                'status': 'success',
                'message': 'Gemini connection working perfectly',
                'response': test_response.text.strip(),
                'response_length': len(test_response.text),
                'model': 'gemini-1.5-flash',
                'api_key_status': f'Active ({self.api_key[:10]}...)'
            }
            
        except Exception as e:
            return {
                'status': 'error',
                'message': f'Connection test failed: {str(e)}',
                'api_key_status': f'Error with key: {self.api_key[:10] if self.api_key else "None"}...'
            }