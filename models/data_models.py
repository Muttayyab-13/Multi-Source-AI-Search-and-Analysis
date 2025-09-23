from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from datetime import datetime

@dataclass
class SearchResult:
    title: str
    content: str
    url: str
    source_type: str  # 'youtube', 'news', 'twitter'
    timestamp: Optional[datetime] = None
    metadata: Dict[str, Any] = field(default_factory=dict)
    embedding: Optional[List[float]] = None
    
@dataclass
class SentimentAnalysis:
    positive: float
    negative: float
    neutral: float
    compound: float
    
@dataclass
class SourceAnalysis:
    source_type: str
    total_results: int
    sentiment: SentimentAnalysis
    key_themes: List[str]
    sample_content: List[str]
    
@dataclass
class SearchAnalysis:
    query: str
    overall_summary: str
    key_insights: List[str]
    source_analyses: List[SourceAnalysis]
    timestamp: datetime = field(default_factory=datetime.now)