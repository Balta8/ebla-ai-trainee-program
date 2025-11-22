"""Document loader module using LangChain."""

from langchain_community.document_loaders import DirectoryLoader, TextLoader, PyPDFLoader
from typing import List
from langchain_core.documents import Document
import os
import logging

logger = logging.getLogger(__name__)

class DocumentLoader:
    """Load documents from a directory using LangChain."""
    
    def __init__(self, documents_path: str):
        """
        Initialize the document loader.
        
        Args:
            documents_path: Path to the directory containing documents
        """
        self.documents_path = os.path.abspath(documents_path)
        if not os.path.exists(self.documents_path):
            logger.error(f"Directory not found: {self.documents_path}")
            raise ValueError(f"Directory not found: '{documents_path}' (absolute path: {self.documents_path})")
        logger.info(f"DocumentLoader initialized with path: {self.documents_path}")
    
    def load_documents(self) -> List[Document]:
        """
        Load all text and PDF documents from the specified directory.
        
        Returns:
            List of LangChain Document objects
            
        Raises:
            Exception: If documents cannot be loaded
        """
        try:
            documents = []
            
            # Load all .txt files from the directory
            txt_loader = DirectoryLoader(
                self.documents_path,
                glob="**/*.txt",
                loader_cls=TextLoader,
                show_progress=True
            )
            txt_documents = txt_loader.load()
            documents.extend(txt_documents)
            
            # Load all .pdf files from the directory
            pdf_loader = DirectoryLoader(
                self.documents_path,
                glob="**/*.pdf",
                loader_cls=PyPDFLoader,
                show_progress=True
            )
            pdf_documents = pdf_loader.load()
            documents.extend(pdf_documents)
            
            if not documents:
                logger.warning(f"No documents found in {self.documents_path}")
                raise ValueError(f"No documents found in {self.documents_path}")
            
            logger.info(f"Loaded {len(documents)} documents: {len(txt_documents)} text, {len(pdf_documents)} PDF")
            print(f"Loaded {len(documents)} documents:")
            print(f"   - {len(txt_documents)} text files")
            print(f"   - {len(pdf_documents)} PDF files")
            
            return documents
            
        except Exception as e:
            logger.error(f"Error loading documents: {str(e)}")
            raise Exception(f"Error loading documents: {str(e)}")
        
# Example usage
if __name__ == "__main__":
    # Get path to data directory
    data_dir = os.path.join(os.path.dirname(__file__), "..", "data")
    data_dir = os.path.abspath(data_dir)
    loader = DocumentLoader(data_dir)
    documents = loader.load_documents()
    
    # Display results
    print(f"Total documents loaded: {len(documents)}\n")
    for i, doc in enumerate(documents, 1):
        print(f"{i}. {doc.metadata['source'].split('/')[-1]}")
        print(f"   Length: {len(doc.page_content)} chars")
        print(f"   Preview: {doc.page_content[:100]}...\n")