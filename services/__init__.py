"""
Services package for Multi-Source AI Search & Analysis

This package contains all the core business logic services:
- data_fetcher: Multi-source data collection
- vector_store: FAISS-based vector database
- ai_analyzer: AI-powered analysis and insights
- sentiment_analyzer: VADER sentiment analysis
- rag_bot: RAG-based Q&A system
"""

from .data_fetcher import MultiSourceDataFetcher
from .vector_store import VectorStore
from .ai_analyzer import AIAnalyzer
from .sentiment_analyzer import SentimentAnalyzer
from .rag_bot import RAGBot

__all__ = [
    'MultiSourceDataFetcher',
    'VectorStore', 
    'AIAnalyzer',
    'SentimentAnalyzer',
    'RAGBot'
]

# Version information
__version__ = '1.0.0'
__author__ = 'Multi-Source AI Search Team'