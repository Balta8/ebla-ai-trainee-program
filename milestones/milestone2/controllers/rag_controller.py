"""Controller module orchestrating retrieval + generation."""

from models.llm_model import LocalLLM
from models.retriever import DocumentRetriever
from views.view import View

class RAGController:
    """Controller for retrieval‑augmented generation flow."""

    def __init__(self, llm: LocalLLM, retriever: DocumentRetriever, view: View) -> None:
        """
        Initialize controller.

        Args:
            llm: The local LLM interface.
            retriever: DocumentRetriever instance.
            view: View instance.
        """
        self.llm = llm
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
