# Multi-Source AI Search & Analysis

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.3+-green.svg)](https://flask.palletsprojects.com/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-orange.svg)](https://openai.com)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

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
git clone https://github.com/yourusername/multi-source-ai-search.git
cd multi-source-ai-search
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

**Production mode:**
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
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

### Testing

```bash
# Install testing dependencies
pip install pytest pytest-cov

# Run tests
pytest tests/

# Run with coverage
pytest --cov=. tests/
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

### Cloud Deployment Options

#### Heroku
```bash
# Install Heroku CLI
# Create Procfile
echo "web: gunicorn app:app" > Procfile

# Deploy
heroku create your-app-name
heroku config:set OPENAI_API_KEY=your-key
git push heroku main
```

#### AWS EC2/ECS
- Use the Docker container
- Configure environment variables
- Set up load balancer
- Enable auto-scaling

#### Google Cloud Run
```bash
# Build and deploy
gcloud builds submit --tag gcr.io/your-project/multi-source-ai-search
gcloud run deploy --image gcr.io/your-project/multi-source-ai-search
```

## Performance Optimization

### Configuration Tuning

```python
# In config/settings.py
class ProductionConfig(Config):
    # Increase worker threads
    MAX_WORKERS = 8
    
    # Optimize vector database
    VECTOR_DB_DIMENSION = 256  # Reduce for speed
    
    # Cache settings
    CACHE_TTL = 3600  # 1 hour
    
    # Rate limiting
    RATE_LIMIT_PER_HOUR = 1000
```

### Monitoring

```python
# Add to app.py for monitoring
import logging
import time
from functools import wraps

def monitor_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"{func.__name__} took {end_time - start_time:.2f}s")
        return result
    return wrapper
```

### Caching Strategy

```python
# Redis caching example
import redis
import json

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def cache_results(key, data, ttl=3600):
    redis_client.setex(key, ttl, json.dumps(data))

def get_cached_results(key):
    cached = redis_client.get(key)
    return json.loads(cached) if cached else None
```

## Security Considerations

### API Key Security
- Never commit API keys to version control
- Use environment variables exclusively
- Rotate keys regularly
- Monitor API usage for anomalies

### Web Security
```python
# Add security headers
@app.after_request
def security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response
```

### Rate Limiting
```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/api/search')
@limiter.limit("5 per minute")
def search():
    # Your search logic
    pass
```

## Troubleshooting

### Common Issues

#### Import Errors
```bash
# Problem: ModuleNotFoundError
# Solution: Ensure all __init__.py files exist
find . -name "*.py" -path "*/services/*" -exec dirname {} \; | sort -u | xargs -I {} touch {}/__init__.py
```

#### API Rate Limits
```python
# Problem: API rate limit exceeded
# Solution: Implement exponential backoff
import time
import random

def api_call_with_backoff(api_function, max_retries=3):
    for attempt in range(max_retries):
        try:
            return api_function()
        except RateLimitError:
            wait_time = (2 ** attempt) + random.uniform(0, 1)
            time.sleep(wait_time)
    raise Exception("Max retries exceeded")
```

#### Memory Issues
```python
# Problem: High memory usage
# Solution: Process data in chunks
def process_in_chunks(data, chunk_size=100):
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i + chunk_size]
        yield process_chunk(chunk)
```

#### JavaScript Errors
- Open browser Developer Tools (F12)
- Check Console for error messages
- Verify all external CDN resources are loading
- Check network requests for API call failures


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

## Acknowledgments

- **OpenAI** for providing powerful language models
- **Hugging Face** for sentence transformers and NLP tools
- **Facebook AI Research** for FAISS vector database
- **VADER Sentiment Analysis** for sentiment scoring
- **Bootstrap** team for the responsive UI framework
- **Chart.js** for interactive data visualizations
- **Flask** community for the excellent web framework

## Support & Contact

### Get Help
- **Bug Reports**: [Create an Issue](https://github.com/yourusername/multi-source-ai-search/issues)
- **Feature Requests**: [Request a Feature](https://github.com/yourusername/multi-source-ai-search/issues)
- **Discussions**: [Join the Discussion](https://github.com/yourusername/multi-source-ai-search/discussions)
- **Documentation**: [Read the Docs](https://multi-source-ai-search.readthedocs.io/)

### Project Status
- **Version**: 1.0.0
- **Status**: Active Development
- **Python**: 3.8+
- **License**: MIT
- **Last Updated**: 2024

### Show Your Support
If this project helped you, please consider:
- **Star** the repository
- **Report** issues you encounter
- **Suggest** new features
- **Contribute** to the codebase
- **Share** with your network

---

**Built with ❤️ by the Multi-Source AI Search Team**

[Home](https://github.com/yourusername/multi-source-ai-search) • 
[Docs](https://multi-source-ai-search.readthedocs.io/) • 
[Issues](https://github.com/yourusername/multi-source-ai-search/issues) • 
[Discussions](https://github.com/yourusername/multi-source-ai-search/discussions)
```python
# In config/settings.py
class ProductionConfig(Config):
    # Increase worker threads
    MAX_WORKERS = 8
    
    # Optimize vector database
    VECTOR_DB_DIMENSION = 256  # Reduce for speed
    
    # Cache settings
    CACHE_TTL = 3600  # 1 hour
    
    # Rate limiting
    RATE_LIMIT_PER_HOUR = 1000
```

### 📊 **Monitoring**

```python
# Add to app.py for monitoring
import logging
import time
from functools import wraps

def monitor_performance(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"{func.__name__} took {end_time - start_time:.2f}s")
        return result
    return wrapper
```

### 💾 **Caching Strategy**

```python
# Redis caching example
import redis
import json

redis_client = redis.Redis(host='localhost', port=6379, db=0)

def cache_results(key, data, ttl=3600):
    redis_client.setex(key, ttl, json.dumps(data))

def get_cached_results(key):
    cached = redis_client.get(key)
    return json.loads(cached) if cached else None
```

## 🛡️ Security Considerations

### 🔐 **API Key Security**
- Never commit API keys to version control
- Use environment variables exclusively
- Rotate keys regularly
- Monitor API usage for anomalies

### 🌐 **Web Security**
```python
# Add security headers
@app.after_request
def security_headers(response):
    response.headers['X-Content-Type-Options'] = 'nosniff'
    response.headers['X-Frame-Options'] = 'DENY'
    response.headers['X-XSS-Protection'] = '1; mode=block'
    return response
```

### 🚦 **Rate Limiting**
```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/api/search')
@limiter.limit("5 per minute")
def search():
    # Your search logic
    pass
```

## 🐛 Troubleshooting

### ❗ **Common Issues**

#### **Import Errors**
```bash
# Problem: ModuleNotFoundError
# Solution: Ensure all __init__.py files exist
find . -name "*.py" -path "*/services/*" -exec dirname {} \; | sort -u | xargs -I {} touch {}/__init__.py
```

#### **API Rate Limits**
```python
# Problem: API rate limit exceeded
# Solution: Implement exponential backoff
import time
import random

def api_call_with_backoff(api_function, max_retries=3):
    for attempt in range(max_retries):
        try:
            return api_function()
        except RateLimitError:
            wait_time = (2 ** attempt) + random.uniform(0, 1)
            time.sleep(wait_time)
    raise Exception("Max retries exceeded")
```

#### **Memory Issues**
```python
# Problem: High memory usage
# Solution: Process data in chunks
def process_in_chunks(data, chunk_size=100):
    for i in range(0, len(data), chunk_size):
        chunk = data[i:i + chunk_size]
        yield process_chunk(chunk)
```

#### **JavaScript Errors**
- Open browser Developer Tools (F12)
- Check Console for error messages
- Verify all external CDN resources are loading
- Check network requests for API call failures

### 📝 **Debugging Tips**

#### **Enable Detailed Logging**
```python
import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# In your services
logger = logging.getLogger(__name__)
logger.debug("Processing search query: %s", query)
```

#### **Monitor API Usage**
```python
# Track API calls
api_usage = {
    'openai': 0,
    'newsapi': 0,
    'twitter': 0,
    'youtube': 0
}

def track_api_call(service):
    api_usage[service] += 1
    logger.info(f"API usage: {api_usage}")
```

## 🤝 Contributing

We welcome contributions! Please follow these guidelines:

### 📋 **Development Setup**
```bash
# Fork the repository
git clone https://github.com/yourusername/multi-source-ai-search.git

# Create feature branch
git checkout -b feature/amazing-feature

# Install development dependencies
pip install -r requirements-dev.txt

# Run pre-commit hooks
pre-commit install
```

### 🔄 **Pull Request Process**
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### 📏 **Code Standards**
- Follow PEP 8 style guidelines
- Add docstrings to all functions
- Include type hints where appropriate
- Write tests for new features
- Update documentation

### 🧪 **Testing Requirements**
```bash
# Run all tests
pytest tests/ -v

# Check code coverage
pytest --cov=services --cov=models tests/

# Run linting
flake8 . --max-line-length=88
black . --check
```

## 📜 License

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

## 🙏 Acknowledgments

- **OpenAI** for providing powerful language models
- **Hugging Face** for sentence transformers and NLP tools
- **Facebook AI Research** for FAISS vector database
- **VADER Sentiment Analysis** for sentiment scoring
- **Bootstrap** team for the responsive UI framework
- **Chart.js** for interactive data visualizations
- **Flask** community for the excellent web framework

## 📞 Support & Contact

### 📧 **Get Help**
- 🐛 **Bug Reports**: [Create an Issue](https://github.com/yourusername/multi-source-ai-search/issues)
- 💡 **Feature Requests**: [Request a Feature](https://github.com/yourusername/multi-source-ai-search/issues)
- 💬 **Discussions**: [Join the Discussion](https://github.com/yourusername/multi-source-ai-search/discussions)
- 📖 **Documentation**: [Read the Docs](https://multi-source-ai-search.readthedocs.io/)

### 🏷️ **Project Status**
- **Version**: 1.0.0
- **Status**: Active Development
- **Python**: 3.8+
- **License**: MIT
- **Last Updated**: 2024

### 🌟 **Show Your Support**
If this project helped you, please consider:
- ⭐ **Star** the repository
- 🐛 **Report** issues you encounter
- 💡 **Suggest** new features
- 🤝 **Contribute** to the codebase
- 📢 **Share** with your network

---

<div align="center">

**Built with ❤️ by the Multi-Source AI Search Team**

[🏠 Home](https://github.com/yourusername/multi-source-ai-search) • 
[📖 Docs](https://multi-source-ai-search.readthedocs.io/) • 
[🐛 Issues](https://github.com/yourusername/multi-source-ai-search/issues) • 
[💬 Discussions](https://github.com/yourusername/multi-source-ai-search/discussions)

</div>