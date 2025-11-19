"""Main entry point for the retrieval‑augmented generation system."""

from models.llm_model import LocalLLM
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
    # Sample documents 
    file_paths = ["milestones/milestone2/data/sample.txt"]
    documents = load_documents(file_paths)
    
    if not documents:
        print("No documents loaded. Please check file paths.")
        return

    # Initialize components
    llm = LocalLLM(model_name="qwen2.5:7b")
    retriever = DocumentRetriever()
    
    print("Building document index...")
    retriever.build_index_from_texts(documents)
    
    view = View()
    controller = RAGController(llm=llm, retriever=retriever, view=view)
    
    # Interactive query loop
    while True:
        question = input("\nEnter your question (or 'quit' to exit): ")
        if question.lower() in ['quit', 'exit', 'q']:
            print("Goodbye!")
            break
        
        if question.strip():
            controller.run_query(question)


if __name__ == "__main__":
    main()

