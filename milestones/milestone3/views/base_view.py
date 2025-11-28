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
    def display_indexing_stats(self, documents_count: int, chunks_count: int, collection_name: str): pass
    
    @abstractmethod
    def display_search_results(self, results: List[Tuple[Any, float]], query: str): pass


class SilentView(BaseView):
    """A dummy view that does nothing (Null Object Pattern)."""
    def show_info(self, msg: str): pass
    def show_message(self, msg: str): pass
    def show_success(self, msg: str): pass
    def show_error(self, msg: str): pass
    def display_indexing_stats(self, documents_count: int, chunks_count: int, collection_name: str): pass
    def display_search_results(self, results: List[Tuple[Any, float]], query: str): pass