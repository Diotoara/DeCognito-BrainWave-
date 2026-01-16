#!/bin/bash

echo "🚀 Setting up OSINT Platform Backend..."

# Create virtual environment
python -m venv venv

# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Upgrade pip
pip install --upgrade pip

# Install Python dependencies
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm

# Create necessary directories
mkdir -p reports
mkdir -p logs
mkdir -p temp

# Set up environment variables
if [ ! -f .env ]; then
    cp .env.example .env
    echo "📝 Please configure your .env file with API keys"
fi

echo "✅ Backend setup complete!"
echo ""
echo "Next steps:"
echo "1. Configure your .env file with API keys"
echo "2. Set up your database (Supabase/PostgreSQL)"
echo "3. Run: python main.py"
