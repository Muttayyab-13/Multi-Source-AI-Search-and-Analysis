# Multi-Source AI Search & Analysis

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-orange.svg)](https://openai.com)


> A comprehensive Flask-based web application that performs AI-powered analysis across multiple data sources (YouTube, News, Twitter/X) with intelligent search capabilities and interactive Q&A functionality.

## Features

### Multi-Source Data Integration
- **YouTube Videos**: Top 5 relevant videos with metadata
- **News Articles**: Latest 5 news articles from multiple sources
- **Social Media**: Up to 50 Twitter/X posts for comprehensive coverage
- **Parallel Processing**: Multi-threaded data fetching for optimal performance

### AI-Powered Analysis
- **GPT Integration**: OpenAI's GPT-3.5-turbo for intelligent insights
- **Comprehensive Summaries**: Overall analysis of findings across sources
- **Key Insights**: 3-5 actionable insights extracted from data
- **Source Comparison**: Side-by-side analysis of different information sources

### Advanced Analytics
- **Sentiment Analysis**: VADER-based sentiment scoring per source
- **Visual Charts**: Interactive sentiment distribution charts
- **Theme Extraction**: Automatic identification of key topics and themes
- **Temporal Analysis**: Time-based trending and pattern recognition

### Interactive Q&A System
- **RAG-based Chat**: Retrieval Augmented Generation for accurate answers
- **Source Attribution**: Every answer includes relevant source citations
- **Context Awareness**: Maintains conversation history and context
- **Suggested Questions**: AI-generated follow-up questions

### Modern Web Interface
- **Responsive Design**: Works seamlessly on desktop and mobile
- **Real-time Updates**: Live progress tracking during analysis
- **Interactive Elements**: Expandable sections and dynamic content
- **Professional UI**: Clean, modern design with Bootstrap 5

## Architecture Overview

```
User Interface
     |
Flask Backend
     |
├── Data Fetcher Service ──┐
├── Vector Store Service   │
├── AI Analyzer Service    │
├── Sentiment Analyzer     │
└── RAG Bot Service        │
                           │
External APIs:             │
├── YouTube API ←──────────┤
├── News API    ←──────────┤
├── Twitter API ←──────────┤
└── OpenAI GPT  ←──────────┘

Core Components:
- FAISS Vector DB
- VADER Sentiment Analysis
- Sentence Transformers
```

## Project Structure

```
multi-source-ai-search/
├── app.py                          # Main Flask application
├── requirements.txt                # Python dependencies
├── README.md                      # This file
├── .env.example                   # Environment variables template
├── .gitignore                     # Git ignore rules
│
├── config/
│   ├── __init__.py                   # Package initialization
│   └── settings.py                   # Configuration settings
│
├── services/
│   ├── __init__.py                   # Service exports
│   ├── data_fetcher.py              # Multi-source data collection
│   ├── vector_store.py              # FAISS vector database
│   ├── ai_analyzer.py               # LLM analysis engine
│   ├── sentiment_analyzer.py        # VADER sentiment analysis
│   └── rag_bot.py                   # RAG-based Q&A system
│
├── models/
│   ├── __init__.py                   # Model exports
│   └── data_models.py               # Data structure definitions
│
├── static/
│   ├── css/
│   │   └── style.css                # Custom styles
│   └── js/
│       └── main.js                  # Frontend JavaScript
│
├── templates/
│   ├── base.html                    # Base template
│   ├── index.html                   # Homepage
│   └── results.html                 # Results display
│
└── tests/ (optional)
    ├── test_services.py             # Service tests
    ├── test_models.py               # Model tests
    └── test_app.py                  # Application tests
```

## Quick Start

### Prerequisites

- **Python 3.8+** installed on your system
- **Git** for version control
- **API Keys** from the following providers:
  - OpenAI API key
  - NewsAPI key
  - Twitter API Bearer Token
  - YouTube Data API key

### Installation

**Clone the repository:**
```bash
git clone https://github.com/Muttayyab-13/Multi-Source-AI-Search-and-Analysis
cd Multi-Source-AI-Search-and-Analysis
```

**Create and activate virtual environment:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**Install dependencies:**
```bash
pip install -r requirements.txt
```

### Configuration

**Create environment file:**
```bash
cp .env.example .env
```

**Edit `.env` with your API keys:**
```env
# Required API Keys
OPENAI_API_KEY=your-openai-api-key-here
NEWS_API_KEY=your-newsapi-key-here
TWITTER_BEARER_TOKEN=your-twitter-bearer-token-here
YOUTUBE_API_KEY=your-youtube-api-key-here

# Flask Configuration
SECRET_KEY=your-super-secret-key-here
FLASK_ENV=development
DEBUG=True
```

### Run the Application

**Development mode:**
```bash
python app.py
```


**Access the application:**
- Open your browser and navigate to `http://localhost:5000`
- Enter a search query and click "Search & Analyze"
- Wait for the multi-threaded processing to complete
- Explore the results and use the Q&A feature

## API Keys Setup

### OpenAI API Key
1. Visit [OpenAI Platform](https://platform.openai.com/api-keys)
2. Sign up or log in to your account
3. Navigate to API Keys section
4. Click "Create new secret key"
5. Copy the key and add to your `.env` file

### NewsAPI Key
1. Go to [NewsAPI](https://newsapi.org/register)
2. Sign up for a free account
3. Verify your email address
4. Get your API key from the dashboard
5. Add to your `.env` file

### Twitter API Bearer Token
1. Visit [Twitter Developer Portal](https://developer.twitter.com/en/portal/dashboard)
2. Create a new project/app
3. Navigate to Keys and Tokens
4. Generate Bearer Token
5. Add to your `.env` file

### YouTube Data API Key
1. Go to [Google Cloud Console](https://console.developers.google.com/)
2. Create a new project or select existing
3. Enable YouTube Data API v3
4. Create credentials (API Key)
5. Add to your `.env` file

## Usage Guide

### Basic Search
1. **Enter Query**: Type your search topic in the search box
2. **Start Analysis**: Click "Search & Analyze" button
3. **Wait for Processing**: Multi-threaded data collection takes 30-60 seconds
4. **Review Results**: Explore the comprehensive analysis

### Understanding Results

#### Overall Summary
- AI-generated comprehensive overview
- Highlights main themes and findings
- Synthesizes information from all sources

#### Key Insights
- 3-5 actionable insights
- Important patterns and trends
- Contrasting perspectives identified

#### Source Analysis Panels
- **YouTube**: Video content analysis and themes
- **News**: Media coverage and sentiment
- **Social Media**: Public opinion and reactions

#### Sentiment Distribution
- Interactive pie chart showing overall sentiment
- Positive, negative, and neutral percentages
- Visual representation of public opinion

### Interactive Q&A
1. **Ask Questions**: Use the chat panel to ask follow-up questions
2. **Get Sourced Answers**: All responses include source citations
3. **Suggested Questions**: Click on suggested topics for deeper analysis
4. **Context Awareness**: Build on previous questions naturally

### Raw Data Access
- Click "Raw Data" to expand detailed source information
- Browse individual articles, videos, and posts
- Access original source links
- Review metadata and timestamps

## Development

### Running in Development Mode

```bash
# Enable debug mode
export FLASK_ENV=development
export DEBUG=True

# Run with auto-reload
python app.py
```

### Custom Configuration

Edit `config/settings.py` to customize:

```python
class Config:
    # Processing limits
    MAX_RESULTS_PER_SOURCE = 50
    
    # Vector database settings
    VECTOR_DB_DIMENSION = 384
    
    # LLM configuration
    LLM_MODEL = "gpt-3.5-turbo"  # or "gpt-4"
    MAX_TOKENS = 2000
    TEMPERATURE = 0.3
    
    # Rate limiting
    REQUESTS_PER_MINUTE = 100
```

## Deployment

### Docker Deployment

**Create Dockerfile:**
```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 5000

# Run application
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:5000", "app:app"]
```

**Build and run:**
```bash
docker build -t multi-source-ai-search .
docker run -p 5000:5000 --env-file .env multi-source-ai-search
```

## Technology Stack

### Backend
- **Python 3.8+**: Core programming language
- **Flask**: Web framework for API and routing
- **OpenAI GPT-3.5**: Language model for analysis and insights
- **FAISS**: Vector database for similarity search
- **VADER**: Sentiment analysis library
- **Sentence Transformers**: Text embedding generation
- **Langchain**: LLM integration and memory management

### Frontend
- **HTML5/CSS3**: Modern web standards
- **Bootstrap 5**: Responsive UI framework
- **JavaScript ES6+**: Interactive functionality
- **Chart.js**: Data visualization
- **Font Awesome**: Icon library

### External APIs
- **YouTube Data API v3**: Video content and metadata
- **NewsAPI**: News articles from multiple sources
- **Twitter API v2**: Social media posts and trends
- **OpenAI API**: AI-powered text generation

### Development Tools
- **Git**: Version control
- **Docker**: Containerization

## Performance Specifications


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2024 Multi-Source AI Search Team

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

