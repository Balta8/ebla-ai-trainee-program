"""RAG service for business logic."""

from services.vector_store import VectorStoreManager
from utils.llm_service import LLMModel
from typing import Dict, Any, List
import logging

logger = logging.getLogger(__name__)


class RAGService:
    """Service layer for RAG operations."""
    
    def __init__(self, vector_store_manager: VectorStoreManager, llm_model: LLMModel):
        """
        Initialize the service.
        
        Args:
            vector_store_manager: VectorStoreManager instance
            llm_model: LLMModel instance
        """
        self.vector_store_manager = vector_store_manager
        self.llm_model = llm_model
    
    def answer_question(
        self,
        query: str,
        collection_name: str,
        top_k: int,
        context_text: str
    ) -> Dict[str, Any]:
        """
        Generate answer and format results.
        
        Args:
            query: User's question
            collection_name: ChromaDB collection name
            top_k: Number of documents to retrieve
            context_text: Retrieved context
            
        Returns:
            Dictionary with formatted answer and sources
        """
        # Build prompt
        prompt = self._build_rag_prompt(query, context_text)
        
        # Generate answer
        answer = self.llm_model.generate(prompt)
        
        return {
            "query": query,
            "answer": answer
        }
    
    def format_search_results(self, results: List[tuple]) -> List[Dict[str, Any]]:
        """
        Format search results for API response.
        
        Args:
            results: List of (Document, score) tuples
            
        Returns:
            List of formatted result dictionaries
        """
        return [
            {
                "content": doc.page_content,
                "metadata": doc.metadata,
                "score": float(score)
            }
            for doc, score in results
        ]
    
    def _build_rag_prompt(self, query: str, context: str) -> str:
        """
        Build a RAG prompt with query and context.
        
        Args:
            query: User's question
            context: Retrieved context
            
        Returns:
            Formatted prompt
        """
        prompt = f"""You are a helpful AI assistant. Answer the question based ONLY on the provided context.
If the context doesn't contain enough information to answer the question, say "I don't have enough information to answer this question."

Context:
{context}

Question: {query}

Answer:"""
        return prompt
