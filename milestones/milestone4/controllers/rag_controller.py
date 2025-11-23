"""RAG controller for orchestrating retrieval and generation."""

from services.vector_store import VectorStoreManager
from services.rag_service import RAGService
from utils.llm_service import LLMModel
from views.base_view import BaseView, SilentView
from models.api_schemas import ChatRequest, ChatResponse, SourceDocument
from typing import Optional
import logging

logger = logging.getLogger(__name__)


class RAGController:
    """Controller for managing RAG operations."""
    
    def __init__(
        self,
        persist_directory: str = "./chroma_db",
        llm_model_name: str = "qwen2.5:7b",
        view: Optional[BaseView] = None
    ):
        """
        Initialize the RAG controller.
        
        Args:
            persist_directory: Directory for ChromaDB persistence
            llm_model_name: Name of the Ollama model
            view: Optional view instance. If None, SilentView is used.
        """
        self.vector_store_manager = VectorStoreManager(persist_directory)
        self.llm_model = LLMModel(model_name=llm_model_name)
        self.service = RAGService(self.vector_store_manager, self.llm_model)
        self.view = view if view else SilentView()
        logger.info("RAG Controller initialized")
    
    def answer_question(self, request: ChatRequest) -> ChatResponse:
        """
        Answer a question using RAG.
        
        Args:
            request: ChatRequest model
            
        Returns:
            ChatResponse model
        """
        try:
            self.view.show_info(f"Processing query: '{request.query}'")
            
            # 1. Retrieve relevant documents
            self.view.show_message("Retrieving relevant documents...")
            vector_store = self.vector_store_manager.load(request.collection_name)
            results = self.vector_store_manager.search(vector_store, request.query, k=request.top_k)
            
            if not results:
                self.view.show_error("No relevant documents found.")
                return ChatResponse(
                    status="success",
                    query=request.query,
                    answer="I couldn't find any relevant information to answer your question.",
                    sources=[]
                )
            
            # 2. Prepare context
            context_text = "\n\n".join([doc.page_content for doc, _ in results])
            
            # 3. Generate answer using service
            self.view.show_message("Generating answer with LLM...")
            answer_result = self.service.answer_question(
                query=request.query,
                collection_name=request.collection_name,
                top_k=request.top_k,
                context_text=context_text
            )
            
            # 4. Format sources using service
            formatted_sources = self.service.format_search_results(results)
            
            # 5. Display results
            self.view.display_rag_response(request.query, answer_result["answer"], results)
            
            # Convert to Pydantic models
            sources = [
                SourceDocument(**src)
                for src in formatted_sources
            ]
            
            return ChatResponse(
                status="success",
                query=answer_result["query"],
                answer=answer_result["answer"],
                sources=sources
            )
            
        except Exception as e:
            self.view.show_error(f"RAG process failed: {str(e)}")
            logger.error(f"RAG process failed: {str(e)}", exc_info=True)
            raise
