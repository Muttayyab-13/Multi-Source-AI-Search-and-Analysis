from flask import Flask, render_template, request, jsonify, session, redirect
import json
from datetime import datetime
import threading
import time

# Import our services
from services.data_fetcher import MultiSourceDataFetcher
from services.vector_store import VectorStore
from services.ai_analyzer import AIAnalyzer
from services.sentiment_analyzer import SentimentAnalyzer
from services.rag_bot import RAGBot
from config.settings import Config

app = Flask(__name__)
app.config['SECRET_KEY'] = Config.SECRET_KEY

# Global services (in production, use proper dependency injection)
vector_store = VectorStore()
data_fetcher = MultiSourceDataFetcher()
ai_analyzer = AIAnalyzer()
sentiment_analyzer = SentimentAnalyzer()
rag_bot = RAGBot(vector_store, ai_analyzer)

# Global storage for current analysis (in production, use Redis or database)
current_analysis = {}
processing_status = {'is_processing': False, 'progress': 0, 'message': 'Ready'}

@app.route('/')
def index():
    """Homepage with search form"""
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    """Handle search request and redirect to results"""
    query = request.form.get('query', '').strip()
    if not query:
        return render_template('index.html', error="Please enter a search query")
    
    # Store query in session
    session['current_query'] = query
    
    # Start background processing
    thread = threading.Thread(target=process_search_async, args=(query,))
    thread.daemon = True
    thread.start()
    
    return render_template('results.html', query=query, processing=True)

def process_search_async(query: str):
    """Process search asynchronously"""
    global current_analysis, processing_status
    
    try:
        processing_status.update({'is_processing': True, 'progress': 10, 'message': 'Fetching data from sources...'})
        
        # Step 1: Fetch data from all sources
        documents = data_fetcher.fetch_all_sources(query)
        processing_status.update({'progress': 40, 'message': 'Processing and storing data...'})
        
        # Step 2: Clear previous data and add new documents to vector store
        vector_store.clear()
        vector_store.add_documents(documents)
        processing_status.update({'progress': 60, 'message': 'Analyzing sentiment...'})
        
        # Step 3: Perform sentiment analysis
        source_analyses = sentiment_analyzer.analyze_documents(documents)
        processing_status.update({'progress': 80, 'message': 'Generating AI insights...'})
        
        # Step 4: Generate AI analysis
        analysis = ai_analyzer.generate_analysis(query, documents, source_analyses)
        processing_status.update({'progress': 90, 'message': 'Finalizing results...'})
        
        # Step 5: Store results
        current_analysis.update({
            'analysis': analysis,
            'documents': documents,
            'source_analyses': source_analyses,
            'sentiment_distribution': sentiment_analyzer.get_overall_sentiment_distribution(source_analyses),
            'timestamp': datetime.now().isoformat()
        })
        
        processing_status.update({'is_processing': False, 'progress': 100, 'message': 'Analysis complete'})
        
    except Exception as e:
        print(f"Error in async processing: {e}")
        processing_status.update({'is_processing': False, 'progress': 0, 'message': f'Error: {str(e)}'})

@app.route('/results')
def results():
    """Display search results"""
    query = session.get('current_query', '')
    if not query:
        return redirect('/')
    
    return render_template('results.html', query=query)

@app.route('/api/status')
def get_status():
    """Get processing status"""
    return jsonify(processing_status)

@app.route('/api/results')
def get_results():
    """Get analysis results"""
    if not current_analysis:
        return jsonify({'error': 'No analysis available'}), 404
    
    # Prepare response data
    analysis = current_analysis['analysis']
    source_analyses = current_analysis['source_analyses']
    
    response_data = {
        'query': analysis.query,
        'summary': analysis.overall_summary,
        'insights': analysis.key_insights,
        'sources': {},
        'sentiment_distribution': current_analysis['sentiment_distribution'],
        'total_documents': len(current_analysis['documents']),
        'timestamp': current_analysis['timestamp']
    }
    
    # Format source analyses
    for source_type, source_analysis in source_analyses.items():
        response_data['sources'][source_type] = {
            'total_results': source_analysis.total_results,
            'sentiment': {
                'positive': source_analysis.sentiment.positive,
                'negative': source_analysis.sentiment.negative,
                'neutral': source_analysis.sentiment.neutral,
                'compound': source_analysis.sentiment.compound
            },
            'key_themes': source_analysis.key_themes,
            'sample_content': source_analysis.sample_content
        }
    
    return jsonify(response_data)

@app.route('/api/documents')
def get_documents():
    """Get raw documents data"""
    if not current_analysis:
        return jsonify({'error': 'No documents available'}), 404
    
    documents = current_analysis['documents']
    documents_data = []
    
    for doc in documents:
        documents_data.append({
            'title': doc.title,
            'content': doc.content,
            'url': doc.url,
            'source_type': doc.source_type,
            'timestamp': doc.timestamp.isoformat() if doc.timestamp else None,
            'metadata': doc.metadata
        })
    
    return jsonify({
        'documents': documents_data,
        'total': len(documents_data)
    })

@app.route('/api/ask', methods=['POST'])
def ask_question():
    """Handle Q&A requests"""
    data = request.get_json()
    question = data.get('question', '').strip()
    
    if not question:
        return jsonify({'error': 'Question is required'}), 400
    
    if not current_analysis:
        return jsonify({'error': 'No search data available. Please perform a search first.'}), 400
    
    try:
        # Get answer from RAG bot
        result = rag_bot.ask_question(question)
        return jsonify(result)
        
    except Exception as e:
        print(f"Error in Q&A: {e}")
        return jsonify({'error': 'Failed to process question'}), 500

@app.route('/api/suggestions')
def get_suggestions():
    """Get suggested questions"""
    query = session.get('current_query', '')
    if not query:
        return jsonify({'suggestions': []})
    
    suggestions = rag_bot.get_suggested_questions(query)
    return jsonify({'suggestions': suggestions})

@app.route('/api/conversation')
def get_conversation():
    """Get conversation history"""
    history = rag_bot.get_conversation_history()
    return jsonify({'conversation': history})

if __name__ == '__main__':
    app.run(debug=True, threaded=True)