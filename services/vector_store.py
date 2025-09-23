import faiss
import numpy as np
import pickle
from typing import List, Dict, Any, Optional
from sentence_transformers import SentenceTransformer
from models.data_models import SearchResult
import concurrent.futures
import threading

class VectorStore:
    def __init__(self, dimension: int = 384):
        self.dimension = dimension
        self.index = faiss.IndexFlatL2(dimension)
        self.encoder = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        self.documents: List[SearchResult] = []
        self.lock = threading.Lock()
        
    def add_documents(self, documents: List[SearchResult]) -> None:
        """Add documents to vector store with parallel embedding generation"""
        if not documents:
            return
            
        # Generate embeddings in parallel
        texts = [f"{doc.title} {doc.content}" for doc in documents]
        
        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as executor:
            # Split texts into chunks for parallel processing
            chunk_size = max(1, len(texts) // 4)
            chunks = [texts[i:i + chunk_size] for i in range(0, len(texts), chunk_size)]
            
            # Generate embeddings for each chunk
            embedding_futures = [
                executor.submit(self.encoder.encode, chunk) 
                for chunk in chunks
            ]
            
            # Collect results
            all_embeddings = []
            for future in concurrent.futures.as_completed(embedding_futures):
                embeddings = future.result()
                all_embeddings.extend(embeddings)
        
        # Convert to numpy array
        embeddings_array = np.array(all_embeddings).astype('float32')
        
        # Thread-safe operations
        with self.lock:
            # Add to FAISS index
            self.index.add(embeddings_array)
            
            # Store documents with embeddings
            for doc, embedding in zip(documents, all_embeddings):
                doc.embedding = embedding.tolist()
                self.documents.append(doc)
    
    def search(self, query: str, k: int = 5) -> List[tuple]:
        """Search for similar documents"""
        if not self.documents:
            return []
            
        # Generate query embedding
        query_embedding = self.encoder.encode([query]).astype('float32')
        
        # Search in FAISS
        with self.lock:
            distances, indices = self.index.search(query_embedding, min(k, len(self.documents)))
        
        # Return results with documents and scores
        results = []
        for distance, idx in zip(distances[0], indices[0]):
            if idx < len(self.documents):
                results.append((self.documents[idx], float(distance)))
        
        return results
    
    def get_all_documents(self) -> List[SearchResult]:
        """Get all stored documents"""
        with self.lock:
            return self.documents.copy()
    
    def clear(self) -> None:
        """Clear the vector store"""
        with self.lock:
            self.index = faiss.IndexFlatL2(self.dimension)
            self.documents.clear()
    
    def get_documents_by_source(self, source_type: str) -> List[SearchResult]:
        """Get documents filtered by source type"""
        with self.lock:
            return [doc for doc in self.documents if doc.source_type == source_type]
