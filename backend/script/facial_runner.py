# import sys
# import os
# import json
# import asyncio

# # Add backend directory to sys.path so we can do relative imports
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# from facial_recognition.face_analyzer import FacialRecognitionAnalyzer

# async def main():
#     try:
#         request_data = json.loads(sys.stdin.read())
#         print("Received request:", request_data, file=sys.stderr)

#         analyzer = FacialRecognitionAnalyzer()

#         image_data = request_data.get("image_data")
#         platforms = request_data.get("search_platforms", ["twitter", "instagram", "linkedin", "facebook"])

#         result = await analyzer.identify_person(image_data)
#         print("identify_person result:", result, file=sys.stderr)

#         if result.get("error"):
#             print(json.dumps({"status": "error", "error": result["error"]}))
#             return

#         person = result.get("identified_person")
#         if not person:
#             print(json.dumps({"status": "no_match", "message": "No match found", "result": result}))
#             return

#         profiles = await analyzer.find_social_media_profiles(person["name"], platforms)
#         print("profiles result:", profiles, file=sys.stderr)

#         news = await analyzer.fetch_news_articles(person["name"], limit=5)
#         print("news result:", news, file=sys.stderr)

#         summary = await analyzer.generate_ai_summary({
#             "identified_person": person,
#             "social_profiles": profiles,
#             "news_articles": news
#         })
#         print("summary result:", summary, file=sys.stderr)

#         report = await analyzer.generate_comprehensive_report({
#             **result,
#             "social_profiles": profiles,
#             "news_articles": news,
#             "ai_summary": summary
#         })
#         print("report ready", file=sys.stderr)

#         print(json.dumps({
#             "status": "success",
#             "identified_person": person,
#             "social_media_profiles": profiles,
#             "news_articles": news,
#             "ai_summary": summary,
#             "comprehensive_report": report,
#             "analysis_metadata": {
#                 "timestamp": result.get("timestamp"),
#                 "method": result.get("analysis_method"),
#                 "faces_detected": result.get("faces_detected", 0)
#             }
#         }))
#     except Exception as e:
#         print(f"❌ Python backend crashed: {e}", file=sys.stderr)
#         print(json.dumps({"status": "error", "error": str(e)}))

# if __name__ == "__main__":
#     asyncio.run(main())



# !above working good 

# import sys
# import os
# import json
# import asyncio
# import base64
# import requests
# from datetime import datetime

# # Add backend directory to sys.path
# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# from facial_recognition.face_analyzer import FacialRecognitionAnalyzer
# from ai_models.summary_gemini import GeminiSummarizer# Assuming you have this

# # Set News API key
# os.environ['NEWS_API_KEY'] = "083abe948ce44367b6afad4152e51230"

# async def main():
#     try:
#         request_data = json.loads(sys.stdin.read())
#         print("Received request:", request_data, file=sys.stderr)

#         analyzer = FacialRecognitionAnalyzer()
#         gemini = GeminiSummarizer()
        
#         image_data = request_data.get("image_data")
#         platforms = request_data.get("search_platforms", ["twitter", "instagram", "linkedin", "facebook"])

#         result = await analyzer.identify_person(image_data)
#         print("identify_person result:", result, file=sys.stderr)

#         if result.get("error"):
#             print(json.dumps({"status": "error", "error": result["error"]}))
#             return

#         person = result.get("identified_person")
#         if not person:
#             print(json.dumps({"status": "no_match", "message": "No match found", "result": result}))
#             return

#         # Check if person is deceased using Gemini
#         deceased_check = await gemini.is_person_deceased(person["name"])
#         is_deceased = deceased_check.get("deceased", False)
#         print(f"Deceased check for {person['name']}: {is_deceased}", file=sys.stderr)

#         # Only search social media if not deceased
#         profiles = {}
#         if not is_deceased:
#             profiles = await analyzer.find_social_media_profiles(person["name"], platforms)
#             print("profiles result:", profiles, file=sys.stderr)
            
#             # Filter profiles using Gemini
#             if profiles:
#                 profiles = await gemini.filter_social_profiles(person["name"], profiles)
#                 print("Filtered profiles:", profiles, file=sys.stderr)
#         else:
#             print("Skipping social media search for deceased person", file=sys.stderr)

#         # Fetch news using News API
#         news = []
#         news_api_key = os.getenv("NEWS_API_KEY")
#         if news_api_key:
#             news = await fetch_news_from_api(person["name"], news_api_key)
#         else:
#             print("News API key not found", file=sys.stderr)
#         print("news result:", news, file=sys.stderr)

#         summary = await analyzer.generate_ai_summary({
#             "identified_person": person,
#             "social_profiles": profiles,
#             "news_articles": news,
#             "is_deceased": is_deceased
#         })
#         print("summary result:", summary, file=sys.stderr)

#         report = await analyzer.generate_comprehensive_report({
#             **result,
#             "social_profiles": profiles,
#             "news_articles": news,
#             "ai_summary": summary,
#             "is_deceased": is_deceased
#         })
        
#         # Generate PDF report
#         pdf_content = generate_pdf_report(report)
#         pdf_base64 = base64.b64encode(pdf_content).decode('utf-8')
#         print("PDF generated", file=sys.stderr)

#         print(json.dumps({
#             "status": "success",
#             "identified_person": person,
#             "social_media_profiles": profiles,
#             "news_articles": news,
#             "ai_summary": summary,
#             "comprehensive_report": report,
#             "pdf_report_base64": pdf_base64,
#             "analysis_metadata": {
#                 "timestamp": result.get("timestamp"),
#                 "method": result.get("analysis_method"),
#                 "faces_detected": result.get("faces_detected", 0),
#                 "is_deceased": is_deceased
#             }
#         }))
#     except Exception as e:
#         print(f"❌ Python backend crashed: {e}", file=sys.stderr)
#         print(json.dumps({"status": "error", "error": str(e)}))

# async def fetch_news_from_api(name, api_key, limit=5):
#     """Fetch news using News API"""
#     try:
#         url = f"https://newsapi.org/v2/everything?q={name}&apiKey={api_key}&pageSize={limit}"
#         response = requests.get(url)
#         data = response.json()
        
#         if data.get("status") == "ok":
#             return [{
#                 "title": article["title"],
#                 "description": article["description"],
#                 "url": article["url"],
#                 "source": article["source"]["name"],
#                 "published_at": article["publishedAt"],
#                 "image": article.get("urlToImage", "")
#             } for article in data["articles"][:limit]]
#         return []
#     except Exception as e:
#         print(f"News API error: {str(e)}", file=sys.stderr)
#         return []

# def generate_pdf_report(report_data):
#     """Generate PDF report using report data"""
#     # This is simplified - in real implementation use a PDF library like ReportLab
#     # For now return a simple text-based PDF
#     from fpdf import FPDF
    
#     pdf = FPDF()
#     pdf.add_page()
#     pdf.set_font("Arial", size=12)
    
#     # Add report content
#     pdf.cell(200, 10, txt=f"OSINT Report: {report_data.get('subject', '')}", ln=1, align='C')
#     pdf.cell(200, 10, txt=f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=1, align='C')
#     pdf.ln(10)
    
#     # Add sections
#     sections = [
#         ("Identified Person", report_data.get("identified_person", {})),
#         ("Risk Assessment", report_data.get("risk_assessment", {})),
#         ("Summary", report_data.get("summary", "")),
#         ("Timeline", report_data.get("controversies_timeline", []))
#     ]
    
#     for title, content in sections:
#         pdf.set_font("Arial", 'B', 14)
#         pdf.cell(200, 10, txt=title, ln=1)
#         pdf.set_font("Arial", size=12)
        
#         if isinstance(content, dict):
#             for key, value in content.items():
#                 pdf.cell(200, 10, txt=f"{key}: {value}", ln=1)
#         elif isinstance(content, list):
#             for item in content:
#                 pdf.cell(200, 10, txt=f"- {item.get('title', '')} ({item.get('date', '')})", ln=1)
#         else:
#             pdf.multi_cell(0, 10, txt=str(content))
        
#         pdf.ln(5)
    
#     return pdf.output(dest='S').encode('latin1')

# if __name__ == "__main__":
#     asyncio.run(main())


# !!!!!!!above bestoooo 


import sys
import os
import json
import asyncio
import base64
import requests
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from facial_recognition.face_analyzer import FacialRecognitionAnalyzer
from ai_models.summary_gemini import GeminiSummarizer

os.environ['NEWS_API_KEY'] = "" #your api key here

async def main():
    try:
        request_data = json.loads(sys.stdin.read())
        print("Received request:", request_data, file=sys.stderr)

        analyzer = FacialRecognitionAnalyzer()
        gemini = GeminiSummarizer()
        
        image_data = request_data.get("image_data")
        platforms = request_data.get("search_platforms", ["twitter", "instagram", "linkedin", "facebook"])

        # Step 1: Identify person
        result = await analyzer.identify_person(image_data)
        print("identify_person result:", result, file=sys.stderr)

        if result.get("error"):
            print(json.dumps({"status": "error", "error": result["error"]}))
            return

        person = result.get("identified_person")
        if not person:
            print(json.dumps({"status": "no_match", "message": "No match found", "result": result}))
            return

        # Step 2: Check if person is deceased
        deceased_check = await gemini.is_person_deceased(person["name"])
        is_deceased = deceased_check.get("deceased", False)
        print(f"Deceased check for {person['name']}: {is_deceased}", file=sys.stderr)

        # Step 3: Find social media profiles (only if not deceased)
        profiles = {}
        if not is_deceased:
            profiles = await analyzer.find_social_media_profiles(person["name"], platforms)
            print("profiles result:", profiles, file=sys.stderr)
            
            if profiles:
                profiles = await gemini.filter_social_profiles(person["name"], profiles)
                print("Filtered profiles:", profiles, file=sys.stderr)
        else:
            print("Skipping social media search for deceased person", file=sys.stderr)

        # Step 4: Fetch news articles
        news = []
        news_api_key = os.getenv("NEWS_API_KEY")
        if news_api_key:
            news = await fetch_news_from_api(person["name"], news_api_key)
        else:
            print("News API key not found", file=sys.stderr)
        print("news result:", news, file=sys.stderr)

        # Step 5: Generate timeline
        timeline = []
        if news:
            timeline = await gemini.generate_timeline(person["name"], news)
            print("Timeline result:", timeline, file=sys.stderr)

        # Step 6: Generate AI summary
        try:
            summary = await analyzer.generate_ai_summary({
                "identified_person": person,
                "social_profiles": profiles,
                "news_articles": news,
                "is_deceased": is_deceased,
                "timeline": timeline
            })
            print("AI summary result:", summary, file=sys.stderr)
        except Exception as e:
            print(f"❌ AI summary generation failed: {e}", file=sys.stderr)
            summary = {
                'error': f'AI summary generation failed: {str(e)}',
                'summary': 'Failed to generate summary due to an error'
            }

        # Step 7: Generate comprehensive report
        try:
            report = await analyzer.generate_comprehensive_report({
                **result,
                "social_profiles": profiles,
                "news_articles": news,
                "ai_summary": summary,
                "is_deceased": is_deceased,
                "timeline": timeline
            })
        except Exception as e:
            print(f"❌ Comprehensive report generation failed: {e}", file=sys.stderr)
            report = {
                'error': f'Report generation failed: {str(e)}',
                'report_id': 'ERROR',
                'generated_at': datetime.now().isoformat()
            }
        
        # Step 8: Generate PDF report
        try:
            pdf_content = generate_pdf_report(report, person, profiles, news, timeline)
            pdf_base64 = base64.b64encode(pdf_content).decode('utf-8')
            print("PDF generated", file=sys.stderr)
        except Exception as e:
            print(f"❌ PDF generation failed: {e}", file=sys.stderr)
            pdf_base64 = None

        # Prepare final response
        response_data = {
            "status": "success",
            "identified_person": person,
            "social_media_profiles": profiles,
            "news_articles": news,
            "ai_summary": summary,
            "comprehensive_report": report,
            "timeline": timeline,
            "analysis_metadata": {
                "timestamp": result.get("timestamp"),
                "method": result.get("analysis_method"),
                "faces_detected": result.get("faces_detected", 0),
                "is_deceased": is_deceased
            }
        }
        
        if pdf_base64:
            response_data["pdf_report_base64"] = pdf_base64

        print(json.dumps(response_data))
    except Exception as e:
        print(f"❌ Python backend crashed: {e}", file=sys.stderr)
        print(json.dumps({"status": "error", "error": str(e)}))

async def fetch_news_from_api(name, api_key, limit=5):
    try:
        url = f"https://newsapi.org/v2/everything?q={name}&apiKey={api_key}&pageSize={limit}&sortBy=popularity"
        response = requests.get(url)
        data = response.json()
        
        if data.get("status") == "ok":
            return [{
                "title": article["title"],
                "description": article["description"],
                "url": article["url"],
                "source": article["source"]["name"],
                "published_at": article["publishedAt"],
                "image": article.get("urlToImage", "")
            } for article in data["articles"][:limit]]
        return []
    except Exception as e:
        print(f"News API error: {str(e)}", file=sys.stderr)
        return []

def generate_pdf_report(report_data, person, profiles, news, timeline):
    from fpdf import FPDF
    
    class PDF(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 16)
            self.cell(0, 10, f"OSINT Report: {person['name']}", 0, 1, 'C')
            self.ln(5)
            
        def footer(self):
            self.set_y(-15)
            self.set_font('Arial', 'I', 8)
            self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', 0, 0, 'C')
            
        def chapter_title(self, title):
            self.set_font('Arial', 'B', 14)
            self.set_fill_color(200, 220, 255)
            self.cell(0, 10, title, 0, 1, 'L', 1)
            self.ln(4)
            
        def chapter_body(self, body):
            self.set_font('Arial', '', 12)
            self.multi_cell(0, 8, body)
            self.ln()
            
        def add_section(self, title, content):
            self.chapter_title(title)
            self.chapter_body(content)
    
    pdf = PDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    
    # Cover page
    pdf.set_font('Arial', 'B', 24)
    pdf.cell(0, 40, "COMPREHENSIVE OSINT REPORT", 0, 1, 'C')
    pdf.ln(20)
    
    pdf.set_font('Arial', 'B', 18)
    pdf.cell(0, 20, person['name'], 0, 1, 'C')
    
    pdf.set_font('Arial', '', 14)
    pdf.cell(0, 10, person['description'], 0, 1, 'C')
    pdf.ln(20)
    
    pdf.set_font('Arial', 'I', 12)
    pdf.cell(0, 10, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", 0, 1, 'C')
    pdf.add_page()
    
    # Personal Summary
    if report_data.get('ai_summary') and 'summary' in report_data['ai_summary']:
        pdf.add_section("Personal Summary", report_data['ai_summary']['summary'])
    else:
        pdf.add_section("Personal Summary", "Summary not available")
    
    # Key Details
    details = f"Name: {person['name']}\n"
    details += f"Confidence: {person['confidence']*100:.2f}%\n"
    details += f"Identification Method: {person['method']}\n"
    if report_data.get('is_deceased'):
        details += "Status: Deceased\n"
    else:
        details += "Status: Living\n"
    pdf.add_section("Key Details", details)
    
    # Social Media Profiles
    if profiles:
        social_text = ""
        for platform, links in profiles.items():
            social_text += f"{platform.capitalize()}:\n"
            for link in links:
                social_text += f"- {link}\n"
            social_text += "\n"
        pdf.add_section("Social Media Profiles", social_text)
    
    # Timeline
    if timeline:
        timeline_text = ""
        for event in timeline:
            timeline_text += f"{event['date']}: {event['title']}\n"
            timeline_text += f"   {event['description']}\n\n"
        pdf.add_section("Key Events Timeline", timeline_text)
    
    # News Analysis
    if news:
        news_text = "Recent News Coverage:\n\n"
        for article in news:
            news_text += f"Title: {article['title']}\n"
            news_text += f"Source: {article['source']} ({article['published_at'][:10]})\n"
            news_text += f"Summary: {article['description']}\n\n"
        pdf.add_section("Media Coverage", news_text)
    
    # Risk Assessment
    if report_data.get('risk_assessment'):
        risk = report_data['risk_assessment']
        risk_text = f"Overall Risk Level: {risk['overall_risk_level']}\n"
        risk_text += f"Public Sentiment: {risk['public_sentiment']}\n"
        risk_text += f"Media Attention: {risk['media_attention']}\n\n"
        risk_text += "Recommendations:\n"
        for rec in risk.get('recommendations', []):
            risk_text += f"- {rec}\n"
        pdf.add_section("Risk Assessment", risk_text)
    
    return pdf.output(dest='S').encode('latin1')

if __name__ == "__main__":
    asyncio.run(main())