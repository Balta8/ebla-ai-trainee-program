"""Controller module orchestrating retrieval + generation."""

from services.rag_service import DocumentRetriever
from views.cli_view import View

class RAGController:
    """Controller for retrieval‑augmented generation flow."""

    def __init__(self, retriever: DocumentRetriever, view: View) -> None:
        """
        Initialize controller.

        Args:
            retriever: DocumentRetriever instance.
            view: View instance.
        """
        self.retriever = retriever
        self.view = view

    def run_query(self, question: str) -> None:
        """
        Execute retrieval and generation for the given question.

        Args:
            question: The user query to answer.
        """
        response: str = self.retriever.query(question)
        self.view.show_response(response)
