"""Test SessionRepository"""
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from repositories.session_repository import SessionRepository
from repositories.database.db_connection import init_db, get_db
from models.user import UserModel  
from models.session import SessionModel
from models.message import MessageModel  
from models.summary import SummaryModel

# Initialize DB
init_db()
db = next(get_db())

try:
    from models.user import UserModel
    user = UserModel(user_name="Ahmed")
    db.add(user)
    db.commit()
    db.refresh(user)
    print(f"User created: {user.user_id}")
    
    repo = SessionRepository(db)
    
    session_id = repo.create_session(user_id=user.user_id)
    print(f"Session created: {session_id}")
    
    exists = repo.session_exists(session_id)
    print(f"Session exists: {exists}")
    
    session = repo.get_session(session_id)
    print(f"Session details: ID={session.session_id}, User={session.user_id}")
    
finally:
    db.close()