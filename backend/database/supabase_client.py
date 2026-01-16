from supabase import create_client, Client
import os
import json
from typing import Dict, List, Optional
from datetime import datetime

class SupabaseClient:
    def __init__(self):
        supabase_url = os.getenv('SUPABASE_URL')
        supabase_key = os.getenv('SUPABASE_ANON_KEY')
        
        if supabase_url and supabase_key:
            self.supabase: Client = create_client(supabase_url, supabase_key)
            self.enabled = True
        else:
            print("Supabase credentials not found. Database operations will be disabled.")
            self.enabled = False
    
    async def store_results(self, investigation_id: str, platform_results: Dict, ai_results: Dict) -> bool:
        """Store investigation results in Supabase"""
        if not self.enabled:
            return False
        
        try:
            # Store platform results
            for platform, data in platform_results.items():
                if isinstance(data, dict) and 'error' not in data:
                    # Store posts/tweets
                    for post in data.get('posts', []):
                        await self._store_result_item(
                            investigation_id, platform, 'post', post, ai_results
                        )
                    
                    # Store comments
                    for comment in data.get('comments', []):
                        await self._store_result_item(
                            investigation_id, platform, 'comment', comment, ai_results
                        )
                    
                    # Store tweets
                    for tweet in data.get('tweets', []):
                        await self._store_result_item(
                            investigation_id, platform, 'tweet', tweet, ai_results
                        )
            
            return True
            
        except Exception as e:
            print(f"Error storing results: {e}")
            return False
    
    async def _store_result_item(self, investigation_id: str, platform: str, data_type: str, content: Dict, ai_results: Dict):
        """Store individual result item"""
        try:
            # Extract relevant AI analysis for this content
            content_text = content.get('content', content.get('body', content.get('title', '')))
            
            # Prepare result data
            result_data = {
                'investigation_id': investigation_id,
                'platform': platform,
                'data_type': data_type,
                'content': content,
                'created_at': datetime.now().isoformat()
            }
            
            # Add AI analysis if available
            if ai_results:
                result_data['sentiment'] = ai_results.get('sentiment', {})
                result_data['entities'] = ai_results.get('entities', {})
                result_data['toxicity'] = ai_results.get('toxicity', {})
                result_data['summary'] = ai_results.get('summary', {}).get('summary', '')
            
            # Insert into database
            response = self.supabase.table('results').insert(result_data).execute()
            
            if response.data:
                print(f"Stored {data_type} from {platform}")
            else:
                print(f"Failed to store {data_type} from {platform}")
                
        except Exception as e:
            print(f"Error storing result item: {e}")
    
    async def get_investigation_results(self, investigation_id: str) -> Optional[Dict]:
        """Retrieve investigation results from database"""
        if not self.enabled:
            return None
        
        try:
            # Get investigation info
            investigation_response = self.supabase.table('investigations').select('*').eq('id', investigation_id).execute()
            
            if not investigation_response.data:
                return None
            
            investigation = investigation_response.data[0]
            
            # Get results
            results_response = self.supabase.table('results').select('*').eq('investigation_id', investigation_id).execute()
            
            results = results_response.data if results_response.data else []
            
            # Group results by platform
            platform_results = {}
            for result in results:
                platform = result['platform']
                if platform not in platform_results:
                    platform_results[platform] = []
                platform_results[platform].append(result)
            
            return {
                'investigation': investigation,
                'results': platform_results,
                'total_results': len(results)
            }
            
        except Exception as e:
            print(f"Error retrieving results: {e}")
            return None
    
    async def list_investigations(self, user_id: str = None, limit: int = 50) -> List[Dict]:
        """List recent investigations"""
        if not self.enabled:
            return []
        
        try:
            query = self.supabase.table('investigations').select('*').order('created_at', desc=True).limit(limit)
            
            if user_id:
                query = query.eq('user_id', user_id)
            
            response = query.execute()
            return response.data if response.data else []
            
        except Exception as e:
            print(f"Error listing investigations: {e}")
            return []
    
    async def update_investigation_status(self, investigation_id: str, status: str, completed_at: str = None) -> bool:
        """Update investigation status"""
        if not self.enabled:
            return False
        
        try:
            update_data = {'status': status}
            if completed_at:
                update_data['completed_at'] = completed_at
            
            response = self.supabase.table('investigations').update(update_data).eq('id', investigation_id).execute()
            
            return bool(response.data)
            
        except Exception as e:
            print(f"Error updating investigation status: {e}")
            return False
    
    async def delete_investigation(self, investigation_id: str) -> bool:
        """Delete investigation and all related results"""
        if not self.enabled:
            return False
        
        try:
            # Delete results first (foreign key constraint)
            self.supabase.table('results').delete().eq('investigation_id', investigation_id).execute()
            
            # Delete investigation
            response = self.supabase.table('investigations').delete().eq('id', investigation_id).execute()
            
            return bool(response.data)
            
        except Exception as e:
            print(f"Error deleting investigation: {e}")
            return False
    
    async def get_analytics(self) -> Dict:
        """Get platform analytics"""
        if not self.enabled:
            return {}
        
        try:
            # Get investigation counts
            investigations_response = self.supabase.table('investigations').select('status').execute()
            investigations = investigations_response.data if investigations_response.data else []
            
            # Get results counts by platform
            results_response = self.supabase.table('results').select('platform').execute()
            results = results_response.data if results_response.data else []
            
            # Calculate statistics
            status_counts = {}
            for inv in investigations:
                status = inv['status']
                status_counts[status] = status_counts.get(status, 0) + 1
            
            platform_counts = {}
            for result in results:
                platform = result['platform']
                platform_counts[platform] = platform_counts.get(platform, 0) + 1
            
            return {
                'total_investigations': len(investigations),
                'status_distribution': status_counts,
                'platform_distribution': platform_counts,
                'total_results': len(results)
            }
            
        except Exception as e:
            print(f"Error getting analytics: {e}")
            return {}
