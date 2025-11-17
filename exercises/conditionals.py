"""Conditionals practice."""

def check_grade(score: int) -> str:
    """Check the grade based on the score using conditionals."""
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Very Good"
    elif score >= 70:
        return "Good"
    else:
        return "Pass"

# Run the function to see output
if __name__ == "__main__":
    test_score = 85
    result = check_grade(test_score)
    print(f"Score: {test_score}, Grade: {result}")