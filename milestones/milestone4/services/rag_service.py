"""RAG service for complete RAG workflow."""

from services.vector_store import VectorStoreManager
from utils.llm_service import LLMModel
from models.api_schemas import ChatRequest, ChatResponse, SourceDocument
from typing import Dict, Any, List
import logging

logger = logging.getLogger(__name__)


class RAGService:
    """Service layer for complete RAG operations (Retrieval + Generation)."""
    
    def __init__(
        self,
        persist_directory: str = "./chroma_db",
        llm_model_name: str = "qwen2.5:7b"
    ):
        """
        Initialize the RAG service with vector store and LLM.
        
        Args:
            persist_directory: Directory for ChromaDB persistence
            llm_model_name: Name of the Ollama model
        """
        self.vector_store_manager = VectorStoreManager(persist_directory)
        self.llm_model = LLMModel(model_name=llm_model_name)
        logger.info(f"RAG Service initialized with model: {llm_model_name}")
    
    def process_query(self, request: ChatRequest) -> ChatResponse:
        """
        Complete RAG workflow: Retrieve → Generate → Format.
        
        Args:
            request: ChatRequest with query and parameters
            
        Returns:
            ChatResponse with answer and sources
        """
        try:
            logger.info(f"Processing query: '{request.query}'")
            
            # 1. Retrieve relevant documents
            vector_store = self.vector_store_manager.load(request.collection_name)
            results = self.vector_store_manager.search(
                vector_store, 
                request.query, 
                k=request.top_k
            )
            
            # Handle no results case
            if not results:
                logger.warning("No relevant documents found")
                return ChatResponse(
                    status="success",
                    query=request.query,
                    answer="I couldn't find any relevant information to answer your question.",
                    sources=[]
                )
            
            # 2. Prepare context from retrieved documents
            context_text = "\n\n".join([doc.page_content for doc, _ in results])
            
            # 3. Build prompt and generate answer
            prompt = self._build_rag_prompt(request.query, context_text)
            answer = self.llm_model.generate(prompt)
            
            # 4. Format sources
            sources = self._format_sources(results)
            
            logger.info("Query processed successfully")
            return ChatResponse(
                status="success",
                query=request.query,
                answer=answer,
                sources=sources
            )
            
        except Exception as e:
            logger.error(f"RAG process failed: {str(e)}", exc_info=True)
            raise
    
    def _format_sources(self, results: List[tuple]) -> List[SourceDocument]:
        """
        Format search results as SourceDocument models.
        
        Args:
            results: List of (Document, score) tuples
            
        Returns:
            List of SourceDocument models
        """
        return [
            SourceDocument(
                content=doc.page_content,
                metadata=doc.metadata,
                score=float(score)
            )
            for doc, score in results
        ]
    
    def _build_rag_prompt(self, query: str, context: str) -> str:
        """
        Build a RAG prompt with system instructions, context, and query.
        
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
