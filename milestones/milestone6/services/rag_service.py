"""Service layer for RAG workflow with Chat History integration."""

from typing import List
from sqlalchemy.orm import Session
from fastapi import HTTPException
from config import settings
from repositories.session_repository import SessionRepository
from repositories.message_repository import MessageRepository
from repositories.summary_repository import SummaryRepository
from services.vector_store import VectorStoreManager
from services.llm_service import LLMModel
from utils.prompt_builder import build_summary_prompt, build_rag_prompt
from schemas.chat_schema import ChatRequest, ChatResponse, SourceDocument, ValidationMetrics
import logging

logger = logging.getLogger(__name__)

class RAGService:
    """
    Service layer for complete RAG workflow with Chat History.
    Handles orchestration between History, Vector Store, and LLM.
    
    This service coordinates:
    - Session management (creating/retrieving conversation sessions)
    - Chat history retrieval (maintaining conversation context)
    - Vector search (finding relevant documents)
    - LLM response generation (producing answers)
    - Response validation 
    """
    
    def __init__(self, db: Session) -> None:
        """
        Initialize RAG service with database connection and required dependencies.
        
        Args:
            db: SQLAlchemy database session
        """
        self.db: Session = db
        self.session_repo: SessionRepository = SessionRepository(db)
        self.message_repo: MessageRepository = MessageRepository(db)
        self.summary_repo: SummaryRepository = SummaryRepository(db)
        self.vector_store: VectorStoreManager = VectorStoreManager()
        self.llm_model: LLMModel = LLMModel()

    def summarize_session(self, session_id: str) -> str:
        """
        Generates and saves a summary for the given session.
        Takes the last N messages (configured in settings) to avoid overloading the LLM.
        
        Process:
        1. Retrieve messages (limited by settings.summary_max_messages)
        2. Extract message ID range (start/end)
        3. Format conversation for LLM
        4. Generate summary using LLM
        5. Save summary to database with message range
        
        Args:
            session_id: The session ID to summarize
            
        Returns:
            The generated summary text
            
        Raises:
            HTTPException: If summary generation fails
        """
        try:
            # 1. Get all messages and limit to last N from settings
            messages = self.message_repo.get_recent_messages(
            session_id, 
            limit=settings.summary_max_messages
            )
            messages.reverse()
            
            if not messages:
                return "No messages to summarize."
            
            # 2. Extract start and end message IDs for tracking which messages were summarized
            start_message_id = messages[0].message_id
            end_message_id = messages[-1].message_id
                
            # 3. Prepare text for LLM (format: "role: content")
            conversation_text = "\n".join([
                f"{msg.role}: {msg.content}" for msg in messages
            ])
            
            # 4. Generate Summary with LLM using prompt builder utility
            prompt = build_summary_prompt(conversation_text)
            
            logger.info(f"Generating summary for session {session_id} ({len(messages)} messages)")
            summary_text = self.llm_model.generate(prompt)
            
            # 5. Save to DB with start and end message IDs for reference
            self.summary_repo.create_summary(
                session_id=session_id,
                summary_text=summary_text,
                start_message_id=start_message_id,
                end_message_id=end_message_id
            )
            logger.info(f"Summary saved for session {session_id}")
            
            return summary_text
            
        except Exception as e:
            logger.error(f"Failed to summarize session: {e}")
            raise HTTPException(status_code=500, detail="Failed to generate summary")

    def process_chat(self, request: ChatRequest) -> ChatResponse:
        """
        Orchestrates the complete RAG chat flow with history and validation.
        
        Process:
        1. Manage Session (Create if new, verify if existing)
        2. Retrieve History (Last N messages for context)
        3. Retrieve Context (Vector search for relevant documents)
        4. Generate Answer (LLM with context + history)
        5. Save to History (Store user query and assistant response)
        6. Validate Response (Generate quality metrics)
        7. Return Response (With sources and validation data)
        
        Args:
            request: ChatRequest containing query, session_id, collection_name, top_k
            
        Returns:
            ChatResponse with answer, sources, and validation metrics
            
        Raises:
            HTTPException: For various failure scenarios (session, search, LLM)
        """
        try:
            session_id = request.session_id

            # 1. Session Management
            # Create new session if not provided
            try:
                if not session_id:
                    # No session provided - create new one
                    session_id = self.session_repo.create_session()
                    logger.info(f"Created new session: {session_id}")
                else:
                    # Session provided - verify it exists, create if not
                    if not self.session_repo.get_session(session_id):
                        session_id = self.session_repo.create_session()
                        logger.warning(f"Session {request.session_id} not found, created new: {session_id}")
            except Exception as e:
                logger.error(f"Session management failed: {e}")
                raise HTTPException(status_code=500, detail="Failed to manage chat session")

            # 2. Retrieve Chat History 
            try:
                recent_messages = self.message_repo.get_recent_messages(
                    session_id, 
                    limit=settings.chat_history_limit
                )
                # (oldest to newest)
                recent_messages = recent_messages[::-1]                
                history_text = "\n".join([
                    f"{('User' if msg.role == 'user' else 'Assistant')}: {msg.content}"
                    for msg in recent_messages
                ])
            except Exception as e:
                logger.error(f"Failed to retrieve chat history: {e}")
                history_text = ""

            # 3. Retrieve Context (Vector Search) 
            try:
                search_results = self.vector_store.search(
                    request.query, 
                    request.collection_name, 
                    request.top_k
                )
                
                # Format results for internal use
                context_docs = [
                    {
                        "content": res['document'], 
                        "metadata": res['metadata'], 
                        "score": res['distance']
                    } 
                    for res in search_results
                ]
            except Exception as e:
                logger.error(f"Vector search failed: {e}")
                raise HTTPException(status_code=500, detail="Failed to search knowledge base")

            # 4. Generate Answer (LLM) 
            # Build prompt with system instructions, history, context, and query
            try:
                prompt = build_rag_prompt(request.query, context_docs, history_text)
                answer = self.llm_model.generate(prompt)
            except Exception as e:
                logger.error(f"LLM generation failed: {e}")
                raise HTTPException(status_code=503, detail="AI service is currently unavailable")

            # 5. Save to History
            try:
                user_msg_id = self.message_repo.add_message(session_id, "user", request.query)
                ai_msg_id = self.message_repo.add_message(session_id, "assistant", answer)
                logger.info(f"Saved messages to session {session_id}")
            except Exception as e:
                logger.error(f"Failed to save chat history: {e}")

            # 6. Validate Response     
            # Extract last 3 messages 
            history_preview: List[str] = []
            if recent_messages:
                for msg in recent_messages[-3:]:
                    role: str = "User" if msg.role == "user" else "Assistant"
                    content: str = msg.content[:100] + "..." if len(msg.content) > 100 else msg.content
                    history_preview.append(f"{role}: {content}")

            # Extract first 1000 chars of prompt for debugging
            prompt_preview: str = prompt[:1000] + "..." if len(prompt) > 1000 else prompt

            # Create validation metrics object
            validation_result: ValidationMetrics = ValidationMetrics(
                used_context=len(context_docs) > 0,  
                used_history=len(history_text) > 0,  
                context_sources=len(context_docs),   
                history_preview=history_preview,     
                prompt_preview=prompt_preview        
            )
            logger.info(f"Response validation: {validation_result.model_dump()}")
            
            # 7. Return Response 
            # Format sources for response schema
            response_sources: List[SourceDocument] = [
                SourceDocument(
                    content=doc['content'], 
                    metadata=doc['metadata'], 
                    score=doc.get('score')
                )
                for doc in context_docs
            ]

            return ChatResponse(
                status="success",
                session_id=session_id,
                query=request.query,
                answer=answer,
                sources=response_sources,
                validation=validation_result
            )
        
        except HTTPException:
            raise
        except Exception as e:
            # Catch any unexpected errors
            logger.error(f"Unexpected error in process_chat: {e}", exc_info=True)
            raise HTTPException(status_code=500, detail="An unexpected error occurred")