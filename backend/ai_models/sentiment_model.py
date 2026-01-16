# from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
# import asyncio
# from typing import List, Dict
# import torch

# class SentimentAnalyzer:
#     def __init__(self):
#         model_name = "distilbert-base-uncased-finetuned-sst-2-english"
#         self.tokenizer = AutoTokenizer.from_pretrained(model_name)
#         self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
#         self.classifier = pipeline(
#             "sentiment-analysis",
#             model=self.model,
#             tokenizer=self.tokenizer,
#             device=0 if torch.cuda.is_available() else -1
#         )
    
#     async def analyze_batch(self, texts: List[str]) -> Dict:
#         try:
#             # Filter and clean texts
#             clean_texts = [text[:512] for text in texts if text and len(text.strip()) > 0]
            
#             if not clean_texts:
#                 return {'error': 'No valid texts to analyze'}
            
#             # Analyze in batches to avoid memory issues
#             batch_size = 32
#             results = []
            
#             for i in range(0, len(clean_texts), batch_size):
#                 batch = clean_texts[i:i + batch_size]
#                 batch_results = self.classifier(batch)
#                 results.extend(batch_results)
            
#             # Aggregate results
#             positive_count = sum(1 for r in results if r['label'] == 'POSITIVE')
#             negative_count = sum(1 for r in results if r['label'] == 'NEGATIVE')
            
#             avg_positive_score = sum(r['score'] for r in results if r['label'] == 'POSITIVE') / max(positive_count, 1)
#             avg_negative_score = sum(r['score'] for r in results if r['label'] == 'NEGATIVE') / max(negative_count, 1)
            
#             return {
#                 'total_analyzed': len(results),
#                 'positive_count': positive_count,
#                 'negative_count': negative_count,
#                 'positive_percentage': (positive_count / len(results)) * 100,
#                 'negative_percentage': (negative_count / len(results)) * 100,
#                 'avg_positive_confidence': avg_positive_score,
#                 'avg_negative_confidence': avg_negative_score,
#                 'detailed_results': results[:100],  # Limit detailed results
#                 'overall_sentiment': 'POSITIVE' if positive_count > negative_count else 'NEGATIVE'
#             }
            
#         except Exception as e:
#             return {'error': f'Sentiment analysis failed: {str(e)}'}
    
#     async def analyze_single(self, text: str) -> Dict:
#         try:
#             if not text or len(text.strip()) == 0:
#                 return {'error': 'Empty text provided'}
            
#             result = self.classifier(text[:512])
#             return result[0] if isinstance(result, list) else result
            
#         except Exception as e:
#             return {'error': f'Sentiment analysis failed: {str(e)}'}



# import os
# import certifi
# import ssl
# from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
# import asyncio
# from typing import List, Dict, Union
# import torch
# import logging

# # Configure SSL certificates at module level
# os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
# os.environ['SSL_CERT_FILE'] = certifi.where()
# ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

# # Configure logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# class SentimentAnalyzer:
#     """
#     Asynchronous sentiment analysis using Hugging Face's transformers with:
#     - SSL certificate handling
#     - GPU support if available
#     - Batch processing
#     - Comprehensive error handling
#     """
    
#     def __init__(self, model_name: str = "distilbert-base-uncased-finetuned-sst-2-english"):
#         """
#         Initialize the sentiment analyzer with SSL configuration.
        
#         Args:
#             model_name: Name of the pre-trained model from Hugging Face hub
#         """
#         self.model_name = model_name
#         self.device = 0 if torch.cuda.is_available() else -1
#         self._initialize_model()

#     def _initialize_model(self):
#         """Initialize the model with proper error handling and SSL configuration."""
#         try:
#             logger.info(f"Loading model: {self.model_name} (device: {'GPU' if self.device == 0 else 'CPU'})")
            
#             self.tokenizer = AutoTokenizer.from_pretrained(
#                 self.model_name,
#                 use_fast=True
#             )
            
#             self.model = AutoModelForSequenceClassification.from_pretrained(
#                 self.model_name
#             )
            
#             self.classifier = pipeline(
#                 "sentiment-analysis",
#                 model=self.model,
#                 tokenizer=self.tokenizer,
#                 device=self.device,
#                 truncation=True,
#                 max_length=512
#             )
            
#             logger.info("Model loaded successfully")
            
#         except Exception as e:
#             logger.error(f"Model initialization failed: {str(e)}")
#             raise RuntimeError(f"Could not initialize model {self.model_name}")

#     async def analyze_batch(self, texts: List[str]) -> Dict[str, Union[str, float, List]]:
#         """
#         Analyze a batch of texts asynchronously with comprehensive results.
        
#         Args:
#             texts: List of texts to analyze
            
#         Returns:
#             Dictionary containing:
#             - Aggregated statistics
#             - Limited detailed results
#             - Error information if any
#         """
#         try:
#             # Clean and validate input
#             clean_texts = [text.strip()[:512] for text in texts if text and text.strip()]
            
#             if not clean_texts:
#                 logger.warning("Empty batch received for analysis")
#                 return {'error': 'No valid texts to analyze'}
            
#             # Process in optimized batches
#             batch_size = 32 if self.device == 0 else 8  # Larger batches for GPU
#             results = []
            
#             for i in range(0, len(clean_texts), batch_size):
#                 batch = clean_texts[i:i + batch_size]
#                 try:
#                     batch_results = await asyncio.to_thread(self.classifier, batch)
#                     results.extend(batch_results)
#                 except Exception as batch_error:
#                     logger.error(f"Batch processing failed: {str(batch_error)}")
#                     # Fallback to individual processing
#                     for text in batch:
#                         try:
#                             result = await asyncio.to_thread(self.classifier, text)
#                             results.extend(result if isinstance(result, list) else [result])
#                         except Exception:
#                             results.append({'label': 'ERROR', 'score': 0.0})
            
#             # Calculate statistics
#             positive = [r for r in results if r.get('label') == 'POSITIVE']
#             negative = [r for r in results if r.get('label') == 'NEGATIVE']
            
#             positive_count = len(positive)
#             negative_count = len(negative)
#             total = len(results)
            
#             return {
#                 'total_texts': total,
#                 'positive_count': positive_count,
#                 'negative_count': negative_count,
#                 'positive_ratio': positive_count / total if total else 0,
#                 'negative_ratio': negative_count / total if total else 0,
#                 'avg_positive_score': sum(r['score'] for r in positive) / positive_count if positive_count else 0,
#                 'avg_negative_score': sum(r['score'] for r in negative) / negative_count if negative_count else 0,
#                 'overall_sentiment': 'POSITIVE' if positive_count > negative_count else 'NEGATIVE',
#                 'sample_results': results[:min(50, len(results))],
#                 'errors': sum(1 for r in results if r.get('label') == 'ERROR')
#             }
            
#         except Exception as e:
#             logger.error(f"Batch analysis failed: {str(e)}")
#             return {'error': f'Sentiment analysis failed: {str(e)}'}

#     async def analyze_single(self, text: str) -> Dict[str, Union[str, float]]:
#         """
#         Analyze a single text with detailed error handling.
        
#         Args:
#             text: Input text to analyze
            
#         Returns:
#             Dictionary containing either:
#             - label: POSITIVE/NEGATIVE
#             - score: Confidence score
#             - error: Error message if analysis failed
#         """
#         try:
#             if not text or not text.strip():
#                 logger.warning("Empty text received for analysis")
#                 return {'error': 'Empty text provided'}
            
#             clean_text = text.strip()[:512]
#             result = await asyncio.to_thread(self.classifier, clean_text)
            
#             if isinstance(result, list):
#                 return result[0]
#             return result
            
#         except Exception as e:
#             logger.error(f"Single analysis failed for text '{text[:50]}...': {str(e)}")
#             return {
#                 'error': f'Sentiment analysis failed',
#                 'input_sample': text[:100],
#                 'details': str(e)
#             }

#     async def analyze_stream(self, text_stream: List[str], window_size: int = 10) -> Dict:
#         """
#         Analyze a stream of texts with sliding window sentiment tracking.
        
#         Args:
#             text_stream: Continuous stream of texts
#             window_size: Number of texts to consider in sentiment window
            
#         Returns:
#             Dictionary containing streaming analysis results
#         """
#         # Implementation for streaming analysis would go here
#         pass



# new 

import os
import sys
import certifi
import ssl
import logging
from pathlib import Path

# Configure SSL certificates at module level
os.environ['REQUESTS_CA_BUNDLE'] = certifi.where()
os.environ['SSL_CERT_FILE'] = certifi.where()
ssl._create_default_https_context = lambda: ssl.create_default_context(cafile=certifi.where())

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

try:
    from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
    import asyncio
    from typing import List, Dict, Union
    import torch
    DEPENDENCIES_AVAILABLE = True
except ImportError as e:
    logger.error(f"Failed to import dependencies: {str(e)}")
    DEPENDENCIES_AVAILABLE = False

class SentimentAnalyzer:
    """
    Asynchronous sentiment analysis using Hugging Face's transformers with:
    - SSL certificate handling
    - GPU support if available
    - Batch processing
    - Comprehensive error handling
    """
    
    def __init__(self, model_name: str = "distilbert-base-uncased-finetuned-sst-2-english"):
        """
        Initialize the sentiment analyzer with SSL configuration.
        
        Args:
            model_name: Name of the pre-trained model from Hugging Face hub
        """
        if not DEPENDENCIES_AVAILABLE:
            raise RuntimeError("Required dependencies not available. Run: pip install transformers torch")
        
        self.model_name = model_name
        self.device = 0 if torch.cuda.is_available() else -1
        self.classifier = None
        self.model = None
        self.tokenizer = None
        
        try:
            self._initialize_model()
            logger.info("✓ SentimentAnalyzer initialized successfully")
        except Exception as e:
            logger.error(f"✗ SentimentAnalyzer initialization failed: {str(e)}")
            raise

    def _initialize_model(self):
        """Initialize the model with proper error handling and SSL configuration."""
        try:
            logger.info(f"Loading sentiment model: {self.model_name}")
            logger.info(f"Device: {'GPU' if self.device == 0 else 'CPU'}")
            
            # Download and load tokenizer
            logger.info("Loading tokenizer...")
            self.tokenizer = AutoTokenizer.from_pretrained(
                self.model_name,
                use_fast=True
            )
            
            # Download and load model
            logger.info("Loading model...")
            self.model = AutoModelForSequenceClassification.from_pretrained(
                self.model_name
            )
            
            # Create pipeline
            logger.info("Creating pipeline...")
            self.classifier = pipeline(
                "sentiment-analysis",
                model=self.model,
                tokenizer=self.tokenizer,
                device=self.device,
                truncation=True,
                max_length=512,
                return_all_scores=False
            )
            
            # Test the pipeline
            logger.info("Testing pipeline...")
            test_result = self.classifier("This is a test message")
            logger.info(f"Test result: {test_result}")
            
            logger.info("✓ Model loaded and tested successfully")
            
        except Exception as e:
            logger.error(f"✗ Model initialization failed: {str(e)}")
            logger.error(f"Error type: {type(e).__name__}")
            
            # Provide specific error messages
            if "connection" in str(e).lower() or "ssl" in str(e).lower():
                logger.error("This appears to be a network/SSL issue. Check your internet connection.")
            elif "memory" in str(e).lower() or "cuda" in str(e).lower():
                logger.error("This appears to be a memory/GPU issue. Try using CPU instead.")
            elif "model" in str(e).lower():
                logger.error("This appears to be a model loading issue. The model might be corrupted or unavailable.")
            
            raise RuntimeError(f"Could not initialize sentiment model: {str(e)}")

    async def analyze_batch(self, texts: List[str]) -> Dict[str, Union[str, float, List]]:
        """
        Analyze a batch of texts asynchronously with comprehensive results.
        
        Args:
            texts: List of texts to analyze
            
        Returns:
            Dictionary containing:
            - Aggregated statistics
            - Limited detailed results
            - Error information if any
        """
        if not self.classifier:
            return {'error': 'Sentiment analyzer not properly initialized'}
        
        try:
            logger.info(f"Starting batch sentiment analysis for {len(texts)} texts")
            
            # Clean and validate input
            clean_texts = []
            for text in texts:
                if text and isinstance(text, str) and text.strip():
                    clean_texts.append(text.strip()[:512])  # Truncate to 512 chars
            
            if not clean_texts:
                logger.warning("No valid texts found for analysis")
                return {'error': 'No valid texts to analyze'}
            
            logger.info(f"Processing {len(clean_texts)} valid texts")
            
            # Process in optimized batches
            batch_size = 16 if self.device == 0 else 8  # Smaller batches for stability
            results = []
            
            for i in range(0, len(clean_texts), batch_size):
                batch = clean_texts[i:i + batch_size]
                logger.info(f"Processing batch {i//batch_size + 1}/{(len(clean_texts)-1)//batch_size + 1}")
                
                try:
                    # Run in thread to avoid blocking
                    batch_results = await asyncio.to_thread(self.classifier, batch)
                    
                    # Ensure results is a list
                    if not isinstance(batch_results, list):
                        batch_results = [batch_results]
                    
                    results.extend(batch_results)
                    logger.info(f"✓ Batch {i//batch_size + 1} completed successfully")
                    
                except Exception as batch_error:
                    logger.error(f"✗ Batch {i//batch_size + 1} failed: {str(batch_error)}")
                    
                    # Fallback to individual processing
                    for text in batch:
                        try:
                            result = await asyncio.to_thread(self.classifier, text)
                            if isinstance(result, list):
                                results.extend(result)
                            else:
                                results.append(result)
                        except Exception:
                            results.append({'label': 'ERROR', 'score': 0.0})
            
            # Calculate statistics
            positive = [r for r in results if r.get('label') == 'POSITIVE']
            negative = [r for r in results if r.get('label') == 'NEGATIVE']
            errors = [r for r in results if r.get('label') == 'ERROR']
            
            positive_count = len(positive)
            negative_count = len(negative)
            error_count = len(errors)
            total = len(results)
            
            logger.info(f"Analysis complete: {positive_count} positive, {negative_count} negative, {error_count} errors")
            
            return {
                'total_texts': total,
                'positive_count': positive_count,
                'negative_count': negative_count,
                'error_count': error_count,
                'positive_ratio': positive_count / total if total else 0,
                'negative_ratio': negative_count / total if total else 0,
                'avg_positive_score': sum(r['score'] for r in positive) / positive_count if positive_count else 0,
                'avg_negative_score': sum(r['score'] for r in negative) / negative_count if negative_count else 0,
                'overall_sentiment': 'POSITIVE' if positive_count > negative_count else 'NEGATIVE',
                'sample_results': results[:min(20, len(results))],  # Limit sample size
                'success_rate': (total - error_count) / total if total else 0
            }
            
        except Exception as e:
            logger.error(f"✗ Batch analysis failed: {str(e)}")
            return {
                'error': f'Sentiment analysis failed: {str(e)}',
                'error_type': type(e).__name__
            }

    async def analyze_single(self, text: str) -> Dict[str, Union[str, float]]:
        """
        Analyze a single text with detailed error handling.
        
        Args:
            text: Input text to analyze
            
        Returns:
            Dictionary containing either:
            - label: POSITIVE/NEGATIVE
            - score: Confidence score
            - error: Error message if analysis failed
        """
        if not self.classifier:
            return {'error': 'Sentiment analyzer not properly initialized'}
        
        try:
            if not text or not isinstance(text, str) or not text.strip():
                logger.warning("Empty or invalid text received for analysis")
                return {'error': 'Empty or invalid text provided'}
            
            clean_text = text.strip()[:512]
            logger.info(f"Analyzing single text: '{clean_text[:50]}...'")
            
            result = await asyncio.to_thread(self.classifier, clean_text)
            
            if isinstance(result, list):
                result = result[0]
            
            logger.info(f"Single analysis result: {result}")
            return result
            
        except Exception as e:
            logger.error(f"✗ Single analysis failed: {str(e)}")
            return {
                'error': f'Sentiment analysis failed: {str(e)}',
                'input_sample': text[:100] if text else 'None',
                'error_type': type(e).__name__
            }
