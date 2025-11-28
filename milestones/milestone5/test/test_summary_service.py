"""Test for Summary Generation Service"""

from pathlib import Path
import sys

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from services.rag_service import RAGService
from repositories.database.db_connection import init_db, get_db
from config import settings

# Initialize DB
init_db()
db = next(get_db())

try:
    # Replace with your actual session ID
    session_id = "30ba30b4-2195-43fb-9431-b4ed45db5008"
    
    # Initialize RAG Service
    rag_service = RAGService(db)
    
    # Verify session exists
    session = rag_service.session_repo.get_session(session_id)
    if not session:
        raise ValueError(f"Session {session_id} not found")

    # Get last N messages directly from DB
    messages = rag_service.message_repo.get_recent_messages(
        session_id, limit=settings.summary_max_messages
    )
    if not messages:
        raise ValueError(f"No messages found for session {session_id}")

    # Number of messages used for summarization
    num_messages_used = len(messages)

    # Generate summary
    summary_text = rag_service.summarize_session(session_id)

    # Verify summary saved in database
    saved_summary = rag_service.summary_repo.get_latest_summary(session_id)
    if not saved_summary or saved_summary.summary_text != summary_text:
        raise ValueError("Summary not saved correctly")

    # Return results
    result = {
        "summary_text": summary_text,
        "num_messages_used": num_messages_used,
        "session_created_at": session.created_date
    }

finally:
    db.close()

print(result)