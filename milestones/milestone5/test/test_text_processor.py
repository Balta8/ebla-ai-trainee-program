"""Test for TextProcessor."""

import os
import sys

# Add parent directory to path to allow importing modules
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from utils.text_processor import TextProcessor
from services.document_loader import DocumentLoader

def test_text_processor():
    # Define the data directory path
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    data_dir = os.path.abspath(data_dir)

    # Load documents
    print(f"Loading documents from: {data_dir}")
    loader = DocumentLoader(data_dir)
    documents = loader.load_documents()
    
    if not documents:
        print("No documents found to process.")
        return
    
    # Process documents
    print("Processing documents...")
    processor = TextProcessor(chunk_size=500, chunk_overlap=50)
    chunks = processor.process_documents(documents)
    
    # Display results
    print(f"Total documents loaded: {len(documents)}")
    print(f"Total chunks created: {len(chunks)}")
    for i, chunk in enumerate(chunks, 1):
        source_name = chunk.metadata.get('source', 'Unknown').split('/')[-1]
        print(f"{i}. {source_name} - Chunk {chunk.metadata.get('chunk_index', 0)}")
        print(f"   Length: {len(chunk.page_content)} chars")
        print(f"   Preview: {chunk.page_content[:100]}...\n")

if __name__ == "__main__":
    test_text_processor()
