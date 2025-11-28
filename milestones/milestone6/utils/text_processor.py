"""Text processing and chunking using LangChain."""

from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents import Document
from typing import List

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