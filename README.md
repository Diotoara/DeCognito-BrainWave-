# 🔍 DeCognito – AI-Powered OSINT Platform

> **Phone Intelligence Toolkit + Multi-Platform Human OSINT for Ethical Investigations in India 🇮🇳**

DeCognito is a **comprehensive OSINT (Open Source Intelligence) platform** combining **phone number intelligence** with **AI-based human OSINT**. It uses a **FastAPI backend** and **Next.js 15 frontend** to deliver advanced, ethical intelligence gathering and analysis tools.

---

## 📱 Phone Intelligence Toolkit

A complete toolkit for analyzing phone numbers with multiple fallback mechanisms.

### Features
- **Basic Info** – Country code, region, carrier, line type  
- **Geolocation** – City, state, timezone coordinates  
- **Owner & Spam** – Caller name, spam score, spam tags  
- **Messaging Apps** – WhatsApp/Telegram presence  
- **Social Media** – Instagram, Twitter, Facebook discovery  
- **Breach Data** – Email leaks and breach info  
- **Spam Reports** – Community-driven reporting + sentiment analysis  
- **Domain/WHOIS** – Linked domains and registration data  
- **Profile Images** – Profile pictures from connected platforms  
- **Number Reassignment** – Carrier change detection  
- **Online Mentions** – Timeline tracking and mentions  

### 🛡️ Robust Fallback System
- **Primary** – Free APIs (Numverify, AbstractAPI, etc.)  
- **Secondary** – Web scraping (requests + BeautifulSoup4)  
- **Tertiary** – Browser automation (Selenium/Playwright)  

### 💾 Data Management
- Raw JSON storage per feature  
- Consolidated export (JSON, CSV, PDF)  
- Profile image downloads  
- Comprehensive error logging  
- Local browser persistence  

### 🎨 Matrix-Style UI
- Animated cyberpunk matrix background  
- Real-time progress tracking  
- Collapsible result sections  
- Responsive design  

---

## 🤖 AI-Based Human OSINT Platform

DeCognito also enables **multi-platform username intelligence** and **AI-driven analysis**.

### Repositories & Demo
- Username Breach Data → [Repo Link](https://github.com/Swayam-jhaa/DeCognito)  
- Data Scraping + Summarization → [Repo Link](https://github.com/ADITYASINGH77770000/Algoverse)  
- 🎥 [Demo Video](https://youtu.be/9wX6ymmzXzE?si=fkaAHpa3aG4ehETZ)  

### Supported Platforms
- **Reddit** – PRAW API + scraping fallback  
- **Twitter/X** – snscrape + scraping  
- **GitHub** – PyGithub API + scraping  
- **Instagram** – instaloader + scraping  
- **News Sources** – newspaper3k + News API  

### AI-Powered Analysis
- **Sentiment Analysis** – DistilBERT  
- **NER (Entity Recognition)** – spaCy + Hugging Face  
- **Toxicity Detection** – ToxicBERT  
- **Summarization** – Gemini 1.5 Flash  
- **Multi-language** – Translation + regional support  

### Visualizations
- Word clouds, timelines, and relationship graphs  
- Sentiment distribution and toxicity gauges  
- Interactive dashboards with real-time updates  

### Reporting
- **CSV, JSON, PDF exports**  
- Interactive dashboards  
- Historical investigation tracking  

---

## 🏗️ Tech Stack

**Frontend**
- Next.js 15 (App Router)  
- TypeScript + Tailwind CSS  
- Prisma ORM + Supabase  

**Backend**
- FastAPI (Python)  
- Hugging Face Transformers + spaCy  
- Gemini AI APIs  
- PostgreSQL  

---

## 🚀 Getting Started

### Prerequisites
- Node.js 18+  
- Python 3.9+  
- PostgreSQL or Supabase  

### Installation
```bash
# Clone repo
git clone https://github.com/your-org/decognito.git
cd decognito
```

# Install frontend
```bash
npm install
```

# Backend setup
```bash
cd backend && pip install -r requirements.txt
```

# Configure environment
```bash
cp .env.example .env
Database Setup
bash
Copy
Edit
npx prisma generate
npx prisma db push
Download AI Models
bash
Copy
Edit
cd backend
python -m spacy download en_core_web_sm
Run Project
bash
Copy
Edit
```

# Terminal 1: frontend
```bash
npm run dev
```

# Terminal 2: backend
```bash
cd backend && python main.py
Visit → http://localhost:3000
```

# 🛡️ Ethical Guidelines
✅ Permitted

Academic research

Journalism & fact-checking

Cybersecurity & forensics

Personal safety

❌ Prohibited

Harassment, stalking, privacy violations

Commercial espionage

Malicious cyber activities

# 📊 Roadmap
v2.0 (Q2 2024)
Advanced visualization & ML threat detection

Real-time monitoring + mobile app

v2.1 (Q3 2024)
Blockchain & crypto analysis

Dark web monitoring (ethical/legal only)

Image/video OSINT

#  📄 License
MIT License – see LICENSE

# ⚠️ Disclaimer
This tool is for educational & research purposes only. Users are solely responsible for compliance with laws and platform terms. Developers assume no liability for misuse.

```bash
Made with ❤️ for ethical OSINT in India 🇮🇳
"Information is power, but with great power comes great responsibility."







