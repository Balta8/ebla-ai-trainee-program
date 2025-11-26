"""
Test script for DatabaseManager.
Creates and resets tables, and performs simple CRUD operations.
"""
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from models.user import UserModel  
from models.session import SessionModel
from models.message import MessageModel  
from models.summary import SummaryModel

from database.db_connection import DatabaseManager
from sqlalchemy import inspect

# Initialize DatabaseManager and create tables

db_manager = DatabaseManager()
db_manager.init_db()

print("Tables created successfully!")
print(db_manager.engine.url)

inspector = inspect(db_manager.engine)
print(inspector.get_table_names(schema="dbo"))


