"""Coordinates between Model and View."""

from Model.person_model import Person
from View.person_view import PersonView

class PersonController:
    """Manages person operations."""
    
    def __init__(self) -> None:
        """Initialize controller with view."""
        self.view = PersonView()
    
    def create_and_display_person(self, name: str, age: int) -> None:
        """Create a person and display their information."""
        # Create model
        person = Person(name, age)
        
        # Use view to display
        self.view.display_person_info(person.name, person.age)
        self.view.display_introduction(person.introduce())

# Example usage
if __name__ == "__main__":
    controller = PersonController()
    controller.create_and_display_person("Alice", 30)
    controller.create_and_display_person("Bob", 25)