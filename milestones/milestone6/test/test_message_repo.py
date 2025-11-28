"""Test MessageRepository"""
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from repositories.message_repository import MessageRepository
from repositories.session_repository import SessionRepository
from repositories.database.db_connection import init_db, get_db
from models.user import UserModel

# Initialize DB
init_db()
db = next(get_db())

try:
    print("--- Testing MessageRepository ---")
    
    # 1. Setup: Create User and Session
    user = UserModel(user_name="TestUser_Msg")
    db.add(user)
    db.commit()
    db.refresh(user)
    
    session_repo = SessionRepository(db)
    session_id = session_repo.create_session(user_id=user.user_id)
    print(f"Setup: Created Session {session_id}")

    # 2. Test: Add Messages
    msg_repo = MessageRepository(db)
    
    # User message
    msg1_id = msg_repo.add_message(session_id, "user", "Hello, AI!")
    print(f"Added User Message: {msg1_id}")
    
    # Assistant message
    msg2_id = msg_repo.add_message(session_id, "assistant", "Hello! How can I help you?")
    print(f"Added Assistant Message: {msg2_id}")
    
    # Another user message
    msg3_id = msg_repo.add_message(session_id, "user", "Tell me about EBLA.")
    print(f"Added User Message: {msg3_id}")

    # 3. Test: Get All Messages
    all_messages = msg_repo.get_messages_by_session(session_id)
    print(f"\nAll Messages ({len(all_messages)}):")
    for msg in all_messages:
        print(f" - [{msg.role}] {msg.content}")
        
    # 4. Test: Get Recent Messages
    recent_messages = msg_repo.get_recent_messages(session_id, limit=2)
    print(f"\nRecent Messages (Limit 2):")
    for msg in recent_messages:
        print(f" - [{msg.role}] {msg.content}")

    # 5. Test: Convert to Schemas
    schemas = msg_repo.convert_to_schemas(all_messages)
    print(f"\nConverted to Schemas: {len(schemas)} items")
    print(f"First schema item: {schemas[0]}")

finally:
    db.close()
