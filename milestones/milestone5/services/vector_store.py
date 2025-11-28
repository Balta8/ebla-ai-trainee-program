"""ChromaDB vector store manager."""

import os
import sys
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from config import settings
from typing import List, Dict

class VectorStoreManager:
    """Simplified ChromaDB vector store manager with auto-persistence."""
    
    def __init__(self, persist_directory: str = None, embedding_model: str = None):
        """
        Initialize ChromaDB with persistent storage.
        
        Args:
            persist_directory: Directory for ChromaDB persistence (defaults to settings)
            embedding_model: HuggingFace embedding model name (defaults to settings)
        """
        if persist_directory is None:
            persist_directory = settings.vector_store_persist_dir
        if embedding_model is None:
            embedding_model = settings.embedding_model_name
            
        self.persist_directory = persist_directory
        self.embeddings = HuggingFaceEmbeddings(
            model_name=embedding_model
        )
        os.makedirs(persist_directory, exist_ok=True)
    
    def create(self, documents: List[Document], collection_name: str = "documents") -> Chroma:
        """Create and populate vector store."""
        return Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings,
            collection_name=collection_name,
            persist_directory=self.persist_directory
        )
    
    def load(self, collection_name: str = "documents") -> Chroma:
        """Load existing vector store."""
        return Chroma(
            collection_name=collection_name,
            embedding_function=self.embeddings,
            persist_directory=self.persist_directory
        )
    
    def search(self, query: str, collection_name: str = "documents", k: int = 3) -> List[Dict]:
        """Search in a Chroma collection and return formatted results."""
        vector_store = self.load(collection_name=collection_name)
        results = vector_store.similarity_search_with_score(query, k=k)
        
        # Convert Tuple[Document, float] to Dict format
        return [
            {
                "document": doc.page_content,
                "metadata": doc.metadata,
                "distance": score
            }
            for doc, score in results
        ]

