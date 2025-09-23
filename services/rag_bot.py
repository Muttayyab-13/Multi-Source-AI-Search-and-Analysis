from typing import List, Dict, Any, Optional
from models.data_models import SearchResult
from services.vector_store import VectorStore
from services.ai_analyzer import AIAnalyzer
import threading

class RAGBot:
    def __init__(self, vector_store: VectorStore, ai_analyzer: AIAnalyzer):
        self.vector_store = vector_store
        self.ai_analyzer = ai_analyzer
        self.conversation_history: List[Dict[str, str]] = []
        self.lock = threading.Lock()
    
    def ask_question(self, question: str, context_limit: int = 5) -> Dict[str, Any]:
        """Ask a question and get an answer with sources"""
        # Search for relevant documents
        search_results = self.vector_store.search(question, k=context_limit)
        
        if not search_results:
            return {
                'answer': "I don't have enough information to answer that question based on the current search results.",
                'sources': [],
                'confidence': 0.0
            }
        
        # Extract documents and their relevance scores
        relevant_docs = [result[0] for result in search_results]
        relevance_scores = [1.0 / (1.0 + result[1]) for result in search_results]  # Convert distance to relevance
        
        # Generate answer using AI analyzer
        answer = self.ai_analyzer.answer_followup_question(question, relevant_docs)
        
        # Prepare source information
        sources = []
        for doc, score in zip(relevant_docs, relevance_scores):
            sources.append({
                'title': doc.title,
                'url': doc.url,
                'source_type': doc.source_type,
                'relevance_score': score,
                'snippet': doc.content[:200] + "..." if len(doc.content) > 200 else doc.content
            })
        
        # Calculate overall confidence based on relevance scores
        avg_confidence = sum(relevance_scores) / len(relevance_scores) if relevance_scores else 0.0
        
        # Store in conversation history
        with self.lock:
            self.conversation_history.append({
                'question': question,
                'answer': answer,
                'timestamp': str(threading.current_thread().ident)
            })
        
        return {
            'answer': answer,
            'sources': sources,
            'confidence': min(avg_confidence, 1.0),  # Cap at 1.0
            'total_sources_found': len(sources)
        }
    
    def get_conversation_history(self) -> List[Dict[str, str]]:
        """Get conversation history"""
        with self.lock:
            return self.conversation_history.copy()
    
    def clear_conversation(self) -> None:
        """Clear conversation history"""
        with self.lock:
            self.conversation_history.clear()
    
    def get_suggested_questions(self, current_query: str) -> List[str]:
        """Generate suggested follow-up questions"""
        # Get document types available
        all_docs = self.vector_store.get_all_documents()
        source_types = set(doc.source_type for doc in all_docs)
        
        suggestions = []
        
        # Generate contextual suggestions based on available sources
        if 'news' in source_types:
            suggestions.append(f"What do news sources say about {current_query}?")
            suggestions.append(f"What are the latest developments regarding {current_query}?")
        
        if 'twitter' in source_types:
            suggestions.append(f"What is the public opinion on {current_query}?")
            suggestions.append(f"How are people reacting to {current_query} on social media?")
        
        if 'youtube' in source_types:
            suggestions.append(f"Are there any educational videos about {current_query}?")
            suggestions.append(f"What explanations are available for {current_query}?")
        
        # General analytical questions
        suggestions.extend([
            f"What are the main controversies around {current_query}?",
            f"How has the perception of {current_query} changed over time?",
            f"What are the different perspectives on {current_query}?"
        ])
        
        return suggestions[:6]  # Return top 6 suggestions