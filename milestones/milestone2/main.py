"""Main entry point for the retrieval‑augmented generation system."""
import os
from pathlib import Path
from models.retriever import DocumentRetriever
from views.view import View
from controllers.rag_controller import RAGController

def load_documents(file_paths: list[str]) -> list[str]:
    """
    Load text documents from given file paths.

    Args:
        file_paths: List of file path strings.

    Returns:
        List of document contents.
    """
    docs: list[str] = []
    for path in file_paths:
        with open(path, "r", encoding="utf‑8") as f:
            docs.append(f.read())
    return docs

def main() -> None:
    """Main function to run the system."""
    # Get the directory 
    script_dir = Path(__file__).parent
    data_dir = script_dir / "data"
    
    # Load all .txt files from data directory
    file_paths = list(data_dir.glob("*.txt"))
    
    if not file_paths:
        print(f"No .txt files found in {data_dir}")
        return
    
    print(f"Found {len(file_paths)} document(s):")
    for fp in file_paths:
        print(f"  - {fp.name}")
    
    documents = load_documents([str(fp) for fp in file_paths])
    
    if not documents:
        print("No documents loaded. Please check file paths.")
        return

    # Initialize components
    retriever = DocumentRetriever()
    
    print("\nBuilding document index...")
    retriever.build_index_from_texts(documents)
    
    view = View()
    controller = RAGController(retriever=retriever, view=view)

    # Interactive query loop
    while True:
        question = input("\nEnter your question (or 'quit' to exit): ")
        if question.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        if question.strip():
            controller.run_query(question)

# Start the application
if __name__ == "__main__":
    main()

