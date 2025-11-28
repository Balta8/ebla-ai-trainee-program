"""History-related Pydantic schemas."""

from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
from datetime import datetime

class SessionSchema(BaseModel):
    """Schema for session serialization."""
    
    session_id: str = Field(..., description="Unique session identifier")
    user_id: Optional[str] = Field(None, description="User ID associated with session")
    created_at: datetime = Field(..., description="Session creation timestamp")
    message_count: int = Field(0, description="Number of messages in session")
    
    model_config = ConfigDict(from_attributes=True)

class MessageSchema(BaseModel):
    """Schema for message serialization."""
    
    message_id: str = Field(..., description="Unique message identifier")
    role: str = Field(..., description="Message role: 'user' or 'assistant'")
    content: str = Field(..., description="Message content")
    created_at: datetime = Field(..., description="Message creation timestamp")
    
    model_config = ConfigDict(from_attributes=True)


class SessionHistoryResponse(BaseModel):
    """Response schema for session history."""
    
    session_id: str = Field(..., description="Session identifier")
    messages: List[MessageSchema] = Field(default_factory=list, description="List of messages")
    
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "session_id": "30ba30b4-2195-43fb-9431-b4ed45db5008",
                "messages": [
                    {
                        "message_id": "msg-1",
                        "role": "user",
                        "content": "Hello",
                        "created_at": "2025-11-23T10:30:00"
                    }
                ]
            }
        }
    )