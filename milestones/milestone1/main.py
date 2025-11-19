"""Main entry point demonstrating MVC architecture."""

from Controller.person_controller import PersonController


def main() -> None:
    """Run the MVC demo."""
    # Initialize controller
    controller = PersonController()
    
    # Create and display persons
    print("=== MVC Pattern Demo ===\n")
    
    controller.create_and_display_person("Ahmed", 25)
    controller.create_and_display_person("Sara", 30)

if __name__ == "__main__":
    main()
