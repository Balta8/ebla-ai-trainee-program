"""Conditionals practice."""

def check_grade(score: int) -> str:
    """Check the grade based on the score using conditionals."""
    if score >= 90:
        return "Excellent"
    elif score >= 80:
        return "Very Good"
    elif score >= 70:
        return "Good"
    elif score >= 60:
        return "Pass"
    else:
        return "Fail"

# Run the function to see output
if __name__ == "__main__":
    test_scores = [85, 92, 76, 54, 67]
    for score in test_scores:
        result = check_grade(score)
        print(f"Score: {score}, Grade: {result}")