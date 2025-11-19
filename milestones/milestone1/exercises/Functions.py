"""Functions practice."""

def calculate_rectangle_area(length: float, width: float) -> float:
    """
    Calculate rectangle area.
    
    Args:
        length: Rectangle length
        width: Rectangle width
        
    Returns:
        float: Area of the rectangle
    """
    return length * width


# Run the functions to see output
if __name__ == "__main__":
    length = 5.0
    width = 3.0
    area = calculate_rectangle_area(length, width)
    print(f"Rectangle area (length={length}, width={width}): {area}")


