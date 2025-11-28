"""Test for VectorStoreManager."""

import os
import sys

# Add parent directory to path to allow importing modules
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from services.vector_store import VectorStoreManager
from services.document_loader import DocumentLoader
from utils.text_processor import TextProcessor

def test_vector_store():
    # Define the data directory path
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    data_dir = os.path.abspath(data_dir)

    # Load documents
    print(f"Loading documents from: {data_dir}")
    loader = DocumentLoader(data_dir)
    documents = loader.load_documents()
    
    if not documents:
        print("No documents found to index.")
        return

    # Process documents into chunks
    processor = TextProcessor(chunk_size=500, chunk_overlap=50)
    chunks = processor.process_documents(documents)

    # Create or load vector store
    persist_dir = os.path.join(os.path.dirname(__file__), "..", "chroma_db")
    vector_store_manager = VectorStoreManager(persist_directory=persist_dir)
    
    # Create and populate the vector store 
    print("Indexing documents...")
    vector_store_manager.load()

    # Example search
    query = "what is Retrieval-Augmented Generation?"
    print(f"\nSearching for: '{query}'")

    results = vector_store_manager.search(query)

    print(f"Search results for query: '{query}'")
    for result in results:
        # Result is a dict now: {'document': ..., 'metadata': ..., 'distance': ...}
        doc_content = result['document']
        metadata = result['metadata']
        score = result['distance']
        
        source_name = metadata.get('source', 'Unknown').split('/')[-1]
        print(f"Score: {score:.4f}, Document Source: {source_name}")
        print(f"   Preview: {doc_content[:100]}...\n")

if __name__ == "__main__":
    test_vector_store()
