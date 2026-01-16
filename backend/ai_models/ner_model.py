import spacy
from transformers import pipeline
import asyncio
from typing import List, Dict
from collections import Counter

class NERAnalyzer:
    def __init__(self):
        # Load spaCy model
        try:
            self.nlp = spacy.load("en_core_web_sm")
        except OSError:
            print("spaCy model not found. Please install: python -m spacy download en_core_web_sm")
            self.nlp = None
        
        # Load Hugging Face NER model as backup
        try:
            self.hf_ner = pipeline("ner", model="dslim/bert-base-NER", aggregation_strategy="simple")
        except Exception as e:
            print(f"Failed to load HF NER model: {e}")
            self.hf_ner = None
    
    async def extract_entities_batch(self, texts: List[str]) -> Dict:
        try:
            all_entities = []
            entity_counts = Counter()
            
            # Clean texts
            clean_texts = [text[:1000] for text in texts if text and len(text.strip()) > 0]
            
            if not clean_texts:
                return {'error': 'No valid texts to analyze'}
            
            # Process with spaCy if available
            if self.nlp:
                for text in clean_texts:
                    doc = self.nlp(text)
                    for ent in doc.ents:
                        entity_info = {
                            'text': ent.text,
                            'label': ent.label_,
                            'start': ent.start_char,
                            'end': ent.end_char,
                            'confidence': 1.0  # spaCy doesn't provide confidence scores
                        }
                        all_entities.append(entity_info)
                        entity_counts[f"{ent.label_}:{ent.text}"] += 1
            
            # Fallback to Hugging Face NER if spaCy failed
            elif self.hf_ner:
                for text in clean_texts:
                    try:
                        entities = self.hf_ner(text)
                        for ent in entities:
                            entity_info = {
                                'text': ent['word'],
                                'label': ent['entity_group'],
                                'confidence': ent['score'],
                                'start': ent.get('start', 0),
                                'end': ent.get('end', 0)
                            }
                            all_entities.append(entity_info)
                            entity_counts[f"{ent['entity_group']}:{ent['word']}"] += 1
                    except Exception as e:
                        print(f"Error processing text with HF NER: {e}")
                        continue
            
            # Aggregate results by entity type
            entity_types = {}
            for entity in all_entities:
                label = entity['label']
                if label not in entity_types:
                    entity_types[label] = []
                entity_types[label].append(entity)
            
            # Get most common entities
            most_common = entity_counts.most_common(20)
            
            return {
                'total_entities': len(all_entities),
                'entity_types': entity_types,
                'entity_counts': dict(entity_counts),
                'most_common_entities': most_common,
                'unique_entities': len(entity_counts),
                'detailed_entities': all_entities[:100]  # Limit detailed results
            }
            
        except Exception as e:
            return {'error': f'NER analysis failed: {str(e)}'}
    
    async def extract_entities_single(self, text: str) -> Dict:
        try:
            if not text or len(text.strip()) == 0:
                return {'error': 'Empty text provided'}
            
            entities = []
            
            if self.nlp:
                doc = self.nlp(text[:1000])
                for ent in doc.ents:
                    entities.append({
                        'text': ent.text,
                        'label': ent.label_,
                        'start': ent.start_char,
                        'end': ent.end_char,
                        'description': spacy.explain(ent.label_)
                    })
            elif self.hf_ner:
                hf_entities = self.hf_ner(text[:1000])
                for ent in hf_entities:
                    entities.append({
                        'text': ent['word'],
                        'label': ent['entity_group'],
                        'confidence': ent['score'],
                        'start': ent.get('start', 0),
                        'end': ent.get('end', 0)
                    })
            
            return {
                'entities': entities,
                'total_count': len(entities)
            }
            
        except Exception as e:
            return {'error': f'NER analysis failed: {str(e)}'}
