"""ChromaDB vector store manager."""

import os
import sys
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.documents import Document
from typing import List, Tuple

class VectorStoreManager:
    """Simplified ChromaDB vector store manager with auto-persistence."""
    
    def __init__(self, persist_directory: str = "./chroma_db"):
        """
        Initialize ChromaDB with persistent storage.
        
        Args:
            persist_directory: Directory for ChromaDB persistence
        """
        self.persist_directory = persist_directory
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        os.makedirs(persist_directory, exist_ok=True)
    
    def create(self, documents: List[Document], collection_name: str = "documents") -> Chroma:
        """Create and populate vector store."""
        return Chroma.from_documents(
            documents=documents,
            embedding=self.embeddings,
            collection_name=collection_name,
            persist_directory=self.persist_directory
        )
    
    def load(self, collection_name: str = "documents") -> Chroma:
        """Load existing vector store."""
        return Chroma(
            collection_name=collection_name,
            embedding_function=self.embeddings,
            persist_directory=self.persist_directory
        )
    
    def search(self, vector_store: Chroma, query: str, k: int = 3) -> List[Tuple[Document, float]]:
        """Search vector store and return documents with scores."""
        return vector_store.similarity_search_with_score(query, k=k)

# Example usage
if __name__ == "__main__":
    # Add parent directory to path to allow importing utils
    sys.path.append(os.path.join(os.path.dirname(__file__), ".."))
    from utils.document_loader import DocumentLoader
    from utils.text_processor import TextProcessor

    # Define the data directory path
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    data_dir = os.path.abspath(data_dir)

    # Load documents
    loader = DocumentLoader(data_dir)
    documents = loader.load_documents()

    # Process documents into chunks
    processor = TextProcessor(chunk_size=500, chunk_overlap=50)
    chunks = processor.process_documents(documents)

    # Create or load vector store
    persist_dir = os.path.join(os.path.dirname(__file__), "..", "chroma_db")
    vector_store_manager = VectorStoreManager(persist_directory=persist_dir)
    
    # Create and populate the vector store 
    print("Indexing documents...")
    vector_store = vector_store_manager.load(collection_name="documents")

    # Example search
    query = "what is Retrieval-Augmented Generation?"
    results = vector_store_manager.search(vector_store, query, k=3)

    print(f"Search results for query: '{query}'")
    for doc, score in results:
        source_name = doc.metadata.get('source', 'Unknown').split('/')[-1]
        print(f"Score: {score:.4f}, Document Source: {source_name}")
        print(f"   Preview: {doc.page_content[:100]}...\n")