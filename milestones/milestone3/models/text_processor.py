"""Text processing and chunking using LangChain."""
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from typing import List
from models.document_loader import DocumentLoader


class TextProcessor:
    """Process and chunk text documents using LangChain."""
    
    def __init__(self, chunk_size: int = 500, chunk_overlap: int = 50):
        """
        Initialize the text processor.
        
        Args:
            chunk_size: Maximum size of each text chunk
            chunk_overlap: Number of characters to overlap between chunks
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
            separators=["\n\n", "\n", ". ", " ", ""]
        )
    
    def process_documents(self, documents: List[Document]) -> List[Document]:
        """
        Split documents into smaller chunks.
        
        Args:
            documents: List of LangChain Document objects
            
        Returns:
            List of chunked Document objects with metadata
            
        Raises:
            Exception: If document processing fails
        """
        try:
            chunks = self.text_splitter.split_documents(documents)
            
            # Add chunk index to metadata
            for i, chunk in enumerate(chunks):
                chunk.metadata['chunk_index'] = i
            
            return chunks
            
        except Exception as e:
            raise Exception(f"Error processing documents: {str(e)}")
        
# Example usage
if __name__ == "__main__":

    # Define the data directory path
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    data_dir = os.path.abspath(data_dir)

    # Load documents
    loader = DocumentLoader(data_dir)
    documents = loader.load_documents()
    
    # Process documents
    processor = TextProcessor(chunk_size=500, chunk_overlap=50)
    chunks = processor.process_documents(documents)
    
    # Display results
    print(f"Total documents loaded: {len(documents)}")
    print(f"Total chunks created: {len(chunks)}")
    for i, chunk in enumerate(chunks, 1):
        print(f"{i}. {chunk.metadata['source'].split('/')[-1]} - Chunk {chunk.metadata['chunk_index']}")
        print(f"   Length: {len(chunk.page_content)} chars")
        print(f"   Preview: {chunk.page_content[:100]}...\n")