"""Base view definitions."""

from abc import ABC, abstractmethod
from typing import List, Tuple, Any

class BaseView(ABC):
    """Abstract base class for views."""
    
    @abstractmethod
    def show_info(self, msg: str): pass
    
    @abstractmethod
    def show_message(self, msg: str): pass
    
    @abstractmethod
    def show_success(self, msg: str): pass
    
    @abstractmethod
    def show_error(self, msg: str): pass
    
    @abstractmethod
    def display_rag_response(self, query: str, answer: str, sources: List[Tuple[Any, float]]): pass


class SilentView(BaseView):
    """A dummy view that does nothing (Null Object Pattern)."""
    def show_info(self, msg: str): pass
    def show_message(self, msg: str): pass
    def show_success(self, msg: str): pass
    def show_error(self, msg: str): pass
    def display_rag_response(self, query: str, answer: str, sources: List[Tuple[Any, float]]): pass