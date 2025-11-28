"""Base model definition for chat history database."""

from sqlalchemy.orm import declarative_base
import uuid
from sqlalchemy import MetaData

metadata = MetaData(schema="dbo")
Base = declarative_base(metadata=metadata)

# Function to generate UUIDs

def generate_uuid():
    return str(uuid.uuid4())