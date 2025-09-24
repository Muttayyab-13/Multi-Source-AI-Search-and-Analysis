from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from typing import List, Dict
from models.data_models import SearchResult, SentimentAnalysis, SourceAnalysis
from collections import defaultdict

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
    
    def analyze_text(self, text: str) -> SentimentAnalysis:
        """Analyze sentiment of a single text"""
        scores = self.analyzer.polarity_scores(text)
        return SentimentAnalysis(
            positive=scores['pos'],
            negative=scores['neg'],
            neutral=scores['neu'],
            compound=scores['compound']
        )
    
    def analyze_documents(self, documents: List[SearchResult]) -> Dict[str, SourceAnalysis]:
        """Analyze sentiment for documents grouped by source"""
        source_groups = defaultdict(list)
        
        # Group documents by source type
        for doc in documents:
            source_groups[doc.source_type].append(doc)
        
        source_analyses = {}
        
        for source_type, docs in source_groups.items():
            # Analyze sentiment for each document
            sentiments = []
            contents = []
            
            for doc in docs:
                text = f"{doc.title} {doc.content}"
                sentiment = self.analyze_text(text)
                sentiments.append(sentiment)
                contents.append(doc.content[:200])  # First 200 chars for sample
            
            # Calculate average sentiment
            if sentiments:
                avg_sentiment = SentimentAnalysis(
                    positive=sum(s.positive for s in sentiments) / len(sentiments),
                    negative=sum(s.negative for s in sentiments) / len(sentiments),
                    neutral=sum(s.neutral for s in sentiments) / len(sentiments),
                    compound=sum(s.compound for s in sentiments) / len(sentiments)
                )
            else:
                avg_sentiment = SentimentAnalysis(0, 0, 1, 0)
            
            # Extract key themes (simplified - in production, use more advanced NLP)
            key_themes = self._extract_key_themes(docs)
            
            source_analyses[source_type] = SourceAnalysis(
                source_type=source_type,
                total_results=len(docs),
                sentiment=avg_sentiment,
                key_themes=key_themes,
                sample_content=contents[:3]  # First 3 samples
            )
        
        return source_analyses
    
    def _extract_key_themes(self, documents: List[SearchResult]) -> List[str]:
        """Extract key themes from documents (simplified implementation)"""
        # In a production system, we wouldd use more sophisticated NLP
        # For now, we'll extract common words (excluding stop words)
        
        common_words = defaultdict(int)
        stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'this', 'that', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should'}
        
        for doc in documents:
            text = f"{doc.title} {doc.content}".lower()
            words = text.split()
            for word in words:
                # Clean word
                clean_word = ''.join(c for c in word if c.isalpha())
                if len(clean_word) > 3 and clean_word not in stop_words:
                    common_words[clean_word] += 1
        
        # Return top themes
        sorted_themes = sorted(common_words.items(), key=lambda x: x[1], reverse=True)
        return [theme[0] for theme in sorted_themes[:5]]
    
    def get_overall_sentiment_distribution(self, source_analyses: Dict[str, SourceAnalysis]) -> Dict[str, float]:
        """Get overall sentiment distribution across all sources"""
        total_docs = sum(analysis.total_results for analysis in source_analyses.values())
        if total_docs == 0:
            return {'positive': 0, 'negative': 0, 'neutral': 1}
        
        weighted_sentiment = {'positive': 0, 'negative': 0, 'neutral': 0}
        
        for analysis in source_analyses.values():
            weight = analysis.total_results / total_docs
            weighted_sentiment['positive'] += analysis.sentiment.positive * weight
            weighted_sentiment['negative'] += analysis.sentiment.negative * weight
            weighted_sentiment['neutral'] += analysis.sentiment.neutral * weight
        
        return weighted_sentiment