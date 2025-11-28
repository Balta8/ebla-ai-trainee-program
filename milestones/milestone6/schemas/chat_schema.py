"""Chat-related Pydantic schemas."""

from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime
from typing import Optional, List, Dict, Any


class ChatRequest(BaseModel):
    """Request schema for chat endpoint."""
    
    query: str = Field(..., min_length=1, description="The user's question")
    session_id: Optional[str] = Field(None, description="Session ID for chat history")
    collection_name: str = Field("documents", description="Vector store collection name")
    top_k: int = Field(3, ge=1, le=10, description="Number of documents to retrieve")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "query": "What services does EBLA provide?",
                "session_id": "30ba30b4-2195-43fb-9431-b4ed45db5008",
                "collection_name": "documents",
                "top_k": 3
            }
        }
    )

class SourceDocument(BaseModel):
    """Schema for source document in chat response."""
    
    content: str = Field(..., description="Document content")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Document metadata")
    score: Optional[float] = Field(None, description="Relevance score")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "content": "EBLA supports the following infrastructure services...",
                "metadata": {"source": "data/ebla_services.txt"},
                "score": 0.45
            }
        }
    )

class ValidationMetrics(BaseModel):
    """Validation metrics for RAG response quality."""
    
    used_context: bool = Field(..., description="Whether context documents were used")
    used_history: bool = Field(..., description="Whether chat history was used")
    context_sources: int = Field(..., description="Number of context sources retrieved")
    history_preview: List[str] = Field(default_factory=list, description="Preview of recent history messages (max 3)")
    prompt_preview: str = Field(default="", description="Preview of the prompt sent to LLM (first 500 chars)")  
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "used_context": True,
                "used_history": True,
                "context_sources": 3,
                "history_preview": [
                    "User: What services does EBLA provide?",
                    "Assistant: EBLA provides..."
                ],
                "prompt_preview": "You are an intelligent assistant for EBLA Computer Consultancy..."
            }
        }
    )
    
class ChatResponse(BaseModel):
    """Response schema for chat endpoint."""
    
    status: str = Field(..., description="Response status")
    session_id: str = Field(..., description="Session identifier")
    query: str = Field(..., description="Original user query")
    answer: str = Field(..., description="Generated answer")
    sources: List[SourceDocument] = Field(default_factory=list, description="Source documents")
    validation: ValidationMetrics = Field(..., description="Response validation metrics")  
    created_at: datetime = Field(default_factory=datetime.utcnow, description="Response timestamp")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "status": "success",
                "session_id": "30ba30b4-2195-43fb-9431-b4ed45db5008",
                "query": "What services does EBLA provide?",
                "answer": "EBLA provides infrastructure services including...",
                "sources": [
                    {
                        "content": "EBLA supports infrastructure services...",
                        "metadata": {"source": "data/ebla_services.txt"},
                        "score": 0.45
                    }
                ],
                "validation": {  
                    "used_context": True,
                    "used_history": True,
                    "context_sources": 3,
                    "history_preview": [
                        "User: What services does EBLA provide?",
                        "Assistant: EBLA provides..."
                    ],
                    "prompt_preview": "You are an intelligent assistant for EBLA Computer Consultancy..."
                },
                "created_at": "2025-11-23T10:30:00"
            }
        }
    )