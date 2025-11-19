"""Loops practice."""

def print_numbers(n: int) -> None:
    """Print numbers from 0 to n-1 using loops."""  
    # for loop
    for i in range(n):
        print(f"Number: {i}")

    # while loop
    count = 0
    while count < 3:
        print(f"Count: {count}")
        count += 1

# Run the function to see output
if __name__ == "__main__":
    print_numbers(5)