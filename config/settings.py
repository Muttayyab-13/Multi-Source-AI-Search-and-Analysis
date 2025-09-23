import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # API Keys 
    OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', 'your-openai-api-key-here')
    NEWS_API_KEY = os.getenv('NEWS_API_KEY', '9d6ea6b7f375468d9940380668f31b81')
    TWITTER_BEARER_TOKEN = os.getenv('TWITTER_BEARER_TOKEN', 'your-twitter-bearer-token-here')
    YOUTUBE_API_KEY = os.getenv('YOUTUBE_API_KEY', 'your-youtube-api-key-here')
    
    # Application Settings
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
    MAX_RESULTS_PER_SOURCE = 50
    VECTOR_DB_DIMENSION = 384  # For sentence-transformers/all-MiniLM-L6-v2
    
    # LLM Settings
    LLM_MODEL = "gpt-3.5-turbo"
    MAX_TOKENS = 2000
    TEMPERATURE = 0.3