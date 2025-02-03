# Advanced/exceptions.py

# This script demonstrates how to handle exceptions in Python

# Example 1: Basic try-except block
try:
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Invalid input. Please enter a number.")

# Example 2: Handling multiple exceptions
try:
    numbers = [1, 2, 3]
    print(numbers[5])  # IndexError
except IndexError:
    print("Error: Index out of range.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

# Example 3: Using else with try-except
try:
    value = int(input("Enter a positive number: "))
    if value < 0:
        raise ValueError("Negative value entered.")
except ValueError as ve:
    print(f"Error: {ve}")
else:
    print(f"You entered: {value}")

# Example 4: Using finally to execute code regardless of exceptions
try:
    file = open("example.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found.")
finally:
    print("Closing file (if it was opened).")
    try:
        file.close()
    except NameError:
        pass

# Example 5: Creating custom exceptions
class CustomError(Exception):
    """
    A custom exception class for demonstration purposes.
    """
    pass

try:
    raise CustomError("This is a custom error message.")
except CustomError as ce:
    print(f"Caught custom exception: {ce}")
