import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import plotly.graph_objects as go
import plotly.express as px
from datetime import datetime
import json
import os
from typing import Dict, List
from weasyprint import HTML, CSS
import base64
from io import BytesIO

class ReportGenerator:
    def __init__(self):
        self.output_dir = "reports"
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Set up matplotlib for headless operation
        plt.switch_backend('Agg')
        
        # Configure seaborn style
        sns.set_style("darkgrid")
        plt.style.use('dark_background')
    
    async def generate_csv(self, investigation_id: str, platform_results: Dict, ai_results: Dict) -> str:
        """Generate CSV export of all data"""
        try:
            all_data = []
            
            # Process platform data
            for platform, data in platform_results.items():
                if isinstance(data, dict) and 'error' not in data:
                    # Posts/Tweets
                    if 'posts' in data:
                        for post in data['posts']:
                            all_data.append({
                                'investigation_id': investigation_id,
                                'platform': platform,
                                'type': 'post',
                                'content': post.get('content', post.get('title', post.get('body', ''))),
                                'date': post.get('date', post.get('created_utc', post.get('created_at', ''))),
                                'engagement': post.get('score', post.get('likes', post.get('like_count', 0))),
                                'url': post.get('url', post.get('permalink', '')),
                                'metadata': json.dumps(post)
                            })
                    
                    # Comments
                    if 'comments' in data:
                        for comment in data['comments']:
                            all_data.append({
                                'investigation_id': investigation_id,
                                'platform': platform,
                                'type': 'comment',
                                'content': comment.get('body', comment.get('content', '')),
                                'date': comment.get('created_utc', comment.get('date', '')),
                                'engagement': comment.get('score', comment.get('likes', 0)),
                                'url': comment.get('permalink', ''),
                                'metadata': json.dumps(comment)
                            })
                    
                    # Tweets
                    if 'tweets' in data:
                        for tweet in data['tweets']:
                            all_data.append({
                                'investigation_id': investigation_id,
                                'platform': platform,
                                'type': 'tweet',
                                'content': tweet.get('content', ''),
                                'date': tweet.get('date', ''),
                                'engagement': tweet.get('like_count', 0),
                                'url': tweet.get('url', ''),
                                'metadata': json.dumps(tweet)
                            })
            
            # Create DataFrame
            df = pd.DataFrame(all_data)
            
            # Add AI analysis results as separate columns
            if ai_results:
                df['sentiment_analysis'] = json.dumps(ai_results.get('sentiment', {}))
                df['entity_analysis'] = json.dumps(ai_results.get('entities', {}))
                df['toxicity_analysis'] = json.dumps(ai_results.get('toxicity', {}))
                df['ai_summary'] = ai_results.get('summary', {}).get('summary', '')
            
            # Save CSV
            csv_path = os.path.join(self.output_dir, f"{investigation_id}_report.csv")
            df.to_csv(csv_path, index=False)
            
            return csv_path
            
        except Exception as e:
            print(f"CSV generation failed: {e}")
            return None
    
    async def generate_pdf(self, investigation_id: str, platform_results: Dict, ai_results: Dict) -> str:
        """Generate PDF report with visualizations"""
        try:
            # Generate visualizations
            charts = await self._generate_charts(platform_results, ai_results)
            
            # Create HTML report
            html_content = self._create_html_report(investigation_id, platform_results, ai_results, charts)
            
            # Convert to PDF
            pdf_path = os.path.join(self.output_dir, f"{investigation_id}_report.pdf")
            
            HTML(string=html_content).write_pdf(
                pdf_path,
                stylesheets=[CSS(string=self._get_pdf_styles())]
            )
            
            return pdf_path
            
        except Exception as e:
            print(f"PDF generation failed: {e}")
            return None
    
    async def generate_json(self, investigation_id: str, platform_results: Dict, ai_results: Dict) -> str:
        """Generate JSON export of all data"""
        try:
            report_data = {
                'investigation_id': investigation_id,
                'generated_at': datetime.now().isoformat(),
                'platform_results': platform_results,
                'ai_analysis': ai_results,
                'summary': {
                    'platforms_analyzed': len(platform_results),
                    'total_content_items': self._count_content_items(platform_results),
                    'ai_models_used': list(ai_results.keys()) if ai_results else []
                }
            }
            
            json_path = os.path.join(self.output_dir, f"{investigation_id}_report.json")
            
            with open(json_path, 'w', encoding='utf-8') as f:
                json.dump(report_data, f, indent=2, ensure_ascii=False)
            
            return json_path
            
        except Exception as e:
            print(f"JSON generation failed: {e}")
            return None
    
    async def _generate_charts(self, platform_results: Dict, ai_results: Dict) -> Dict:
        """Generate visualization charts"""
        charts = {}
        
        try:
            # Platform distribution chart
            platform_counts = {}
            for platform, data in platform_results.items():
                if isinstance(data, dict) and 'error' not in data:
                    count = 0
                    count += len(data.get('posts', []))
                    count += len(data.get('comments', []))
                    count += len(data.get('tweets', []))
                    platform_counts[platform] = count
            
            if platform_counts:
                fig = px.pie(
                    values=list(platform_counts.values()),
                    names=list(platform_counts.keys()),
                    title="Content Distribution by Platform"
                )
                charts['platform_distribution'] = self._fig_to_base64(fig)
            
            # Sentiment analysis chart
            if 'sentiment' in ai_results:
                sentiment_data = ai_results['sentiment']
                if 'positive_count' in sentiment_data and 'negative_count' in sentiment_data:
                    fig = go.Figure(data=[
                        go.Bar(
                            x=['Positive', 'Negative'],
                            y=[sentiment_data['positive_count'], sentiment_data['negative_count']],
                            marker_color=['green', 'red']
                        )
                    ])
                    fig.update_layout(title="Sentiment Analysis Results")
                    charts['sentiment_analysis'] = self._fig_to_base64(fig)
            
            # Toxicity analysis chart
            if 'toxicity' in ai_results:
                toxicity_data = ai_results['toxicity']
                if 'toxicity_percentage' in toxicity_data:
                    fig = go.Figure(go.Indicator(
                        mode="gauge+number",
                        value=toxicity_data['toxicity_percentage'],
                        domain={'x': [0, 1], 'y': [0, 1]},
                        title={'text': "Toxicity Level (%)"},
                        gauge={
                            'axis': {'range': [None, 100]},
                            'bar': {'color': "darkred"},
                            'steps': [
                                {'range': [0, 25], 'color': "lightgray"},
                                {'range': [25, 50], 'color': "yellow"},
                                {'range': [50, 100], 'color': "red"}
                            ],
                            'threshold': {
                                'line': {'color': "red", 'width': 4},
                                'thickness': 0.75,
                                'value': 90
                            }
                        }
                    ))
                    charts['toxicity_gauge'] = self._fig_to_base64(fig)
            
            # Word cloud
            all_text = self._extract_all_text(platform_results)
            if all_text:
                wordcloud = WordCloud(
                    width=800, 
                    height=400, 
                    background_color='white',
                    colormap='viridis'
                ).generate(all_text)
                
                plt.figure(figsize=(10, 5))
                plt.imshow(wordcloud, interpolation='bilinear')
                plt.axis('off')
                plt.title('Most Common Words')
                
                buffer = BytesIO()
                plt.savefig(buffer, format='png', bbox_inches='tight', dpi=150)
                buffer.seek(0)
                charts['wordcloud'] = base64.b64encode(buffer.getvalue()).decode()
                plt.close()
            
        except Exception as e:
            print(f"Chart generation error: {e}")
        
        return charts
    
    def _fig_to_base64(self, fig) -> str:
        """Convert plotly figure to base64 string"""
        buffer = BytesIO()
        fig.write_image(buffer, format='png')
        buffer.seek(0)
        return base64.b64encode(buffer.getvalue()).decode()
    
    def _extract_all_text(self, platform_results: Dict) -> str:
        """Extract all text content for word cloud"""
        all_text = []
        
        for platform, data in platform_results.items():
            if isinstance(data, dict) and 'error' not in data:
                # Extract text from posts
                for post in data.get('posts', []):
                    text = post.get('content', post.get('title', post.get('body', '')))
                    if text:
                        all_text.append(text)
                
                # Extract text from comments
                for comment in data.get('comments', []):
                    text = comment.get('body', comment.get('content', ''))
                    if text:
                        all_text.append(text)
                
                # Extract text from tweets
                for tweet in data.get('tweets', []):
                    text = tweet.get('content', '')
                    if text:
                        all_text.append(text)
        
        return ' '.join(all_text)
    
    def _count_content_items(self, platform_results: Dict) -> int:
        """Count total content items across all platforms"""
        total = 0
        for platform, data in platform_results.items():
            if isinstance(data, dict) and 'error' not in data:
                total += len(data.get('posts', []))
                total += len(data.get('comments', []))
                total += len(data.get('tweets', []))
        return total
    
    def _create_html_report(self, investigation_id: str, platform_results: Dict, ai_results: Dict, charts: Dict) -> str:
        """Create HTML report template"""
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>OSINT Investigation Report - {investigation_id}</title>
        </head>
        <body>
            <div class="header">
                <h1>🔍 OSINT Investigation Report</h1>
                <p><strong>Investigation ID:</strong> {investigation_id}</p>
                <p><strong>Generated:</strong> {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
            </div>
            
            <div class="section">
                <h2>📊 Executive Summary</h2>
                <ul>
                    <li>Platforms Analyzed: {len(platform_results)}</li>
                    <li>Total Content Items: {self._count_content_items(platform_results)}</li>
                    <li>AI Models Used: {', '.join(ai_results.keys()) if ai_results else 'None'}</li>
                </ul>
            </div>
            
            <div class="section">
                <h2>🎯 Platform Results</h2>
                {self._format_platform_results(platform_results)}
            </div>
            
            <div class="section">
                <h2>🧠 AI Analysis</h2>
                {self._format_ai_results(ai_results)}
            </div>
            
            <div class="section">
                <h2>📈 Visualizations</h2>
                {self._format_charts(charts)}
            </div>
            
            <div class="footer">
                <p><em>This report was generated by the AI-Based OSINT Platform for ethical research purposes.</em></p>
            </div>
        </body>
        </html>
        """
        return html
    
    def _format_platform_results(self, platform_results: Dict) -> str:
        """Format platform results for HTML"""
        html = ""
        for platform, data in platform_results.items():
            if isinstance(data, dict):
                if 'error' in data:
                    html += f"<h3>{platform.title()}</h3><p>Error: {data['error']}</p>"
                else:
                    html += f"<h3>{platform.title()}</h3>"
                    html += f"<p>Posts: {len(data.get('posts', []))}</p>"
                    html += f"<p>Comments: {len(data.get('comments', []))}</p>"
                    html += f"<p>Tweets: {len(data.get('tweets', []))}</p>"
        return html
    
    def _format_ai_results(self, ai_results: Dict) -> str:
        """Format AI results for HTML"""
        html = ""
        for model, results in ai_results.items():
            if isinstance(results, dict) and 'error' not in results:
                html += f"<h3>{model.title()} Analysis</h3>"
                html += f"<pre>{json.dumps(results, indent=2)}</pre>"
        return html
    
    def _format_charts(self, charts: Dict) -> str:
        """Format charts for HTML"""
        html = ""
        for chart_name, chart_data in charts.items():
            html += f'<h3>{chart_name.replace("_", " ").title()}</h3>'
            html += f'<img src="data:image/png;base64,{chart_data}" style="max-width: 100%; height: auto;">'
        return html
    
    def _get_pdf_styles(self) -> str:
        """Get CSS styles for PDF"""
        return """
        body { font-family: Arial, sans-serif; margin: 40px; }
        .header { text-align: center; border-bottom: 2px solid #333; padding-bottom: 20px; }
        .section { margin: 30px 0; }
        h1 { color: #2c3e50; }
        h2 { color: #34495e; border-bottom: 1px solid #bdc3c7; }
        h3 { color: #7f8c8d; }
        pre { background-color: #f8f9fa; padding: 10px; border-radius: 5px; }
        .footer { margin-top: 50px; text-align: center; font-style: italic; }
        """
