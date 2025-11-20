"""Module for document retrieval using LlamaIndex"""

from typing import List, Optional
from pathlib import Path
from llama_index.core import VectorStoreIndex, Settings, SimpleDirectoryReader, Document
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.core.node_parser import TokenTextSplitter
from llama_index.core.ingestion import IngestionPipeline

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
        self.similarity_top_k = similarity_top_k
        self.index = None

        # Setup chunker 
        self.chunker = TokenTextSplitter(
            chunk_size=128,
            chunk_overlap=16
        )

        self.pipeline = IngestionPipeline(
            transformations=[self.chunker]
        )

    def build_index_from_directory(
        self, 
        input_dir: str,
        required_exts: Optional[List[str]] = None,
        recursive: bool = True
    ) -> None:
        """
        Build index from a directory of documents with chunking.

        Args:
            input_dir: Path to directory containing documents.
            required_exts: List of file extensions to load (e.g., [".pdf", ".txt"]).
            recursive: Whether to search subdirectories.
        """
        if required_exts is None:
            required_exts = [".txt"]

        # Load raw docs 
        loader = SimpleDirectoryReader(
            input_dir=input_dir,
            required_exts=required_exts,
            recursive=recursive
        )
        docs = loader.load_data()

        # Apply chunking
        nodes = self.pipeline.run(documents=docs)

        # Build index
        self.index = VectorStoreIndex(nodes)

        print(f"Indexed {len(nodes)} chunks from directory: {input_dir}")

    def build_index_from_texts(self, documents: List[str]) -> None:
        """
        Build index from a list of text strings with chunking.

        Args:
            documents: List of text documents.
        """
        docs = [Document(text=doc) for doc in documents]

        # Apply chunking
        nodes = self.pipeline.run(documents=docs)

        # Build index
        self.index = VectorStoreIndex(nodes)

        print(f"Indexed {len(nodes)} chunks from text list.")

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


# Build index from data
if __name__ == "__main__":
    retriever = DocumentRetriever()

    # Get data directory
    data_dir = str(Path(__file__).parent.parent / "data")

    # Build index with real chunking
    retriever.build_index_from_directory(data_dir)

    # Show index stats
    nodes = retriever.index.docstore.docs
    print(f"\nTotal chunks: {len(nodes)}\n")

    for i, (node_id, node) in enumerate(nodes.items(), 1):
        file_name = node.metadata.get("file_name", "Unknown")
        print(f"Chunk #{i} (from {file_name})")
        print(f"{node.text[:200]}...\n")