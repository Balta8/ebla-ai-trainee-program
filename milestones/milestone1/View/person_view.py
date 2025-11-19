"""Handles all display and user interface."""

class PersonView:
    """Handles how person data is displayed."""
    
    # Static methods for displaying person information without needing an instance
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

# Example usage
if __name__ == "__main__":
    PersonView.display_introduction("Hello, I am John and I am 28 years old.")
    PersonView.display_person_info("John", 28)