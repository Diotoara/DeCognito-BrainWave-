from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
import asyncio
from typing import List, Dict
import torch

class ToxicityAnalyzer:
    def __init__(self):
        model_name = "unitary/toxic-bert"
        try:
            self.tokenizer = AutoTokenizer.from_pretrained(model_name)
            self.model = AutoModelForSequenceClassification.from_pretrained(model_name)
            self.classifier = pipeline(
                "text-classification",
                model=self.model,
                tokenizer=self.tokenizer,
                device=0 if torch.cuda.is_available() else -1
            )
        except Exception as e:
            print(f"Failed to load toxicity model: {e}")
            # Fallback to a simpler model
            self.classifier = pipeline("text-classification", model="martin-ha/toxic-comment-model")
    
    async def analyze_batch(self, texts: List[str]) -> Dict:
        try:
            # Filter and clean texts
            clean_texts = [text[:512] for text in texts if text and len(text.strip()) > 0]
            
            if not clean_texts:
                return {'error': 'No valid texts to analyze'}
            
            # Analyze in batches
            batch_size = 16
            results = []
            
            for i in range(0, len(clean_texts), batch_size):
                batch = clean_texts[i:i + batch_size]
                try:
                    batch_results = self.classifier(batch)
                    results.extend(batch_results)
                except Exception as e:
                    print(f"Error processing batch: {e}")
                    # Add placeholder results for failed batch
                    results.extend([{'label': 'UNKNOWN', 'score': 0.0}] * len(batch))
            
            # Analyze results
            toxic_count = 0
            non_toxic_count = 0
            high_risk_content = []
            
            for i, result in enumerate(results):
                if isinstance(result, list):
                    result = result[0]
                
                # Different models may have different label formats
                is_toxic = (
                    result.get('label', '').upper() in ['TOXIC', 'TOXICITY', '1'] or
                    result.get('score', 0) > 0.7
                )
                
                if is_toxic:
                    toxic_count += 1
                    if result.get('score', 0) > 0.8:
                        high_risk_content.append({
                            'text': clean_texts[i][:100] + '...',
                            'score': result.get('score', 0),
                            'index': i
                        })
                else:
                    non_toxic_count += 1
            
            total_analyzed = len(results)
            toxicity_percentage = (toxic_count / total_analyzed) * 100 if total_analyzed > 0 else 0
            
            return {
                'total_analyzed': total_analyzed,
                'toxic_count': toxic_count,
                'non_toxic_count': non_toxic_count,
                'toxicity_percentage': toxicity_percentage,
                'risk_level': self._calculate_risk_level(toxicity_percentage),
                'high_risk_content': high_risk_content[:10],  # Limit to top 10
                'detailed_results': results[:50]  # Limit detailed results
            }
            
        except Exception as e:
            return {'error': f'Toxicity analysis failed: {str(e)}'}
    
    def _calculate_risk_level(self, toxicity_percentage: float) -> str:
        if toxicity_percentage >= 50:
            return 'HIGH'
        elif toxicity_percentage >= 25:
            return 'MEDIUM'
        elif toxicity_percentage >= 10:
            return 'LOW'
        else:
            return 'MINIMAL'
    
    async def analyze_single(self, text: str) -> Dict:
        try:
            if not text or len(text.strip()) == 0:
                return {'error': 'Empty text provided'}
            
            result = self.classifier(text[:512])
            if isinstance(result, list):
                result = result[0]
            
            return {
                'text': text[:100] + '...' if len(text) > 100 else text,
                'label': result.get('label', 'UNKNOWN'),
                'score': result.get('score', 0.0),
                'risk_level': self._calculate_risk_level(result.get('score', 0) * 100)
            }
            
        except Exception as e:
            return {'error': f'Toxicity analysis failed: {str(e)}'}
