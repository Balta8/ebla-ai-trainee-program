"""Handles all display and user interface."""

class PersonView:
    """Handles how person data is displayed."""
    
    @staticmethod
    def display_introduction(message: str) -> None:
        """Display introduction message."""
        print(f"{message}")
    
    @staticmethod
    def display_person_info(name: str, age: int) -> None:
        """Display person information."""
        print(f"Name: {name}")
        print(f"Age: {age}")
        print("-" * 20)