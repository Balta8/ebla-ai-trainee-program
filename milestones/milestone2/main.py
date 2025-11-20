"""Main entry point for the retrieval-augmented generation system."""
from pathlib import Path
from models.retriever import DocumentRetriever
from views.view import View
from controllers.rag_controller import RAGController


def main() -> None:
    """Main function to run the system."""
    # Initialize components
    retriever = DocumentRetriever()
    
    # Get data directory path
    script_dir = Path(__file__).parent
    data_dir = str(script_dir / "data")
    
    # Build index directly from directory
    print("\nBuilding document index...")
    retriever.build_index_from_directory(data_dir)
    
    # Initialize view and controller
    view = View()
    controller = RAGController(retriever=retriever, view=view)
    
    # Interactive query loop
    while True:
        question = view.get_user_input()
        
        if question.lower() == 'quit':
            view.display_message("\nGoodbye!")
            break
            
        controller.run_query(question)


if __name__ == "__main__":
    main()