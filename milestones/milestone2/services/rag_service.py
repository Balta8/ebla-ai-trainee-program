"""Module for document retrieval using LlamaIndex"""

from typing import List, Optional
from llama_index.core import VectorStoreIndex, Settings, SimpleDirectoryReader
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.core import Document

from llama_index.core.node_parser import TokenTextSplitter

class DocumentRetriever:
    """Document retrieval with LlamaIndex + Ollama."""

    def __init__(
        self, 
        embedding_model_name: str = "BAAI/bge-large-en-v1.5",
        llm_model_name: str = "qwen2.5:7b",
        similarity_top_k: int = 4
    ) -> None:
        """
        Initialize the retriever with embedding model and LLM.

        Args:
            embedding_model_name: Name of the HuggingFace embedding model.
            llm_model_name: Name of the Ollama model.
            similarity_top_k: Number of similar documents to retrieve.
        """
        # Setup embedding model
        self.embed_model = HuggingFaceEmbedding(
            model_name=embedding_model_name,
            trust_remote_code=True
        )
        
        # Setup LLM
        self.llm = Ollama(model=llm_model_name, request_timeout=120.0)
        
        # Configure global settings
        Settings.embed_model = self.embed_model
        Settings.llm = self.llm
        Settings.text_splitter = TokenTextSplitter(chunk_size=128, chunk_overlap=16)
        
        self.similarity_top_k = similarity_top_k
        self.index = None

    def build_index_from_directory(
        self, 
        input_dir: str,
        required_exts: Optional[List[str]] = None,
        recursive: bool = True
    ) -> None:
        """
        Build index from a directory of documents.

        Args:
            input_dir: Path to directory containing documents.
            required_exts: List of file extensions to load (e.g., [".pdf", ".txt"]).
            recursive: Whether to search subdirectories.
        """
        if required_exts is None:
            required_exts = [".pdf", ".txt"]
            
        # Load documents from directory
        loader = SimpleDirectoryReader(
            input_dir=input_dir,
            required_exts=required_exts,
            recursive=recursive
        )
        docs = loader.load_data()
        
        # Create vector store index
        self.index = VectorStoreIndex.from_documents(docs)
        print(f"Indexed {len(docs)} documents from {input_dir}")

    def build_index_from_texts(self, documents: List[str]) -> None:
        """
        Build index from a list of text strings.

        Args:
            documents: List of text documents.
        """
        
        docs = [Document(text=doc) for doc in documents]
        self.index = VectorStoreIndex.from_documents(docs)
        print(f"Indexed {len(docs)} text documents.")

    def query(self, question: str, streaming: bool = False) -> str:
        """
        Query the index with a question.

        Args:
            question: The question to ask.
            streaming: Whether to stream the response.

        Returns:
            The generated answer.
        """
        if self.index is None:
            raise ValueError("Index not yet built. Call build_index_*() first.")

        # Setup query engine
        query_engine = self.index.as_query_engine(
            streaming=streaming,
            similarity_top_k=self.similarity_top_k
        )
        
        # Query and return response
        response = query_engine.query(question)
        
        if streaming:
            # For streaming, return the response object
            return response
        else:
            return str(response)


# Quick test
if __name__ == "__main__":
    import os
    from pathlib import Path
    
    # Get data directory path
    # Script is in services/, so data is in ../data
    current_dir = Path(__file__).resolve().parent
    data_dir = current_dir.parent / "data"
    
    if not data_dir.exists():
        print(f"Data directory not found at {data_dir}")
        # Create dummy data for testing if not exists
        data_dir.mkdir(parents=True, exist_ok=True)
        with open(data_dir / "sample.txt", "w") as f:
            f.write("Ebla Computer Consultancy is a technology solutions provider.")
    
    retriever = DocumentRetriever()
    
    print(f"Indexing chunks from directory: {data_dir}")
    retriever.build_index_from_directory(str(data_dir))
    
    # Access and display chunks (nodes) from the index
    if retriever.index:
        # Get all nodes from the docstore
        nodes = list(retriever.index.docstore.docs.values())
        print(f"\nTotal chunks: {len(nodes)}")
        
        for i, node in enumerate(nodes, 1):
            # Get metadata
            file_name = node.metadata.get('file_name', 'unknown')
            
            # Get content and clean up newlines for display
            content = node.get_content().replace('\n', ' ')
            preview = content[:70] + "..." if len(content) > 70 else content
            
            print(f"\nChunk #{i} (from {file_name})")
            print(f"Content: {preview}")

    
