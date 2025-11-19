"""Person class representing a simple user model."""

class Person:
    """Represents a person with name and age."""

    def __init__(self, name: str, age: int) -> None:
        """Initialize person with name and age."""
        self.name = name
        self.age = age

    def introduce(self) -> str:
        """Return an introduction message."""
        return f"My name is {self.name} and I am {self.age} years old."