"""Test for DocumentLoader."""

import os
import sys

# Add parent directory to path to allow importing modules
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from services.document_loader import DocumentLoader

def test_document_loader():
    # Get path to data directory
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    data_dir = os.path.abspath(data_dir)
    
    print(f"Loading documents from: {data_dir}")
    try:
        loader = DocumentLoader(data_dir)
        documents = loader.load_documents()
        
        # Display results
        print(f"Total documents loaded: {len(documents)}\n")
        for i, doc in enumerate(documents, 1):
            source = doc.metadata.get('source', 'Unknown')
            print(f"{i}. {source.split('/')[-1]}")
            print(f"   Length: {len(doc.page_content)} chars")
            print(f"   Preview: {doc.page_content[:100]}...\n")
            
    except Exception as e:
        print(f"Error testing document loader: {e}")

if __name__ == "__main__":
    test_document_loader()
