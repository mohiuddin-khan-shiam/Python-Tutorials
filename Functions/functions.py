# Functions/functions.py

# This script demonstrates how to define and use functions in Python

# Example 1: Basic function definition and call
def greet():
    """
    This function prints a simple greeting message.
    """
    print("Hello, welcome to Python functions!")

# Calling the greet function
greet()

# Example 2: Function with parameters
def greet_person(name):
    """
    This function takes a name as an argument and prints a personalized greeting.

    Parameters:
    name (str): The name of the person to greet.
    """
    print(f"Hello, {name}! Nice to meet you.")

# Calling the function with an argument
greet_person("Alice")

# Example 3: Function with default parameters
def greet_person_with_default(name="Guest"):
    """
    This function greets the person using a default name if no name is provided.

    Parameters:
    name (str): The name of the person to greet. Defaults to "Guest".
    """
    print(f"Hello, {name}!")

# Calling the function without an argument
greet_person_with_default()
# Calling the function with an argument
greet_person_with_default("Bob")

# Example 4: Function with return value
def add_numbers(a, b):
    """
    This function returns the sum of two numbers.

    Parameters:
    a (int or float): The first number.
    b (int or float): The second number.

    Returns:
    int or float: The sum of a and b.
    """
    return a + b

# Storing the return value in a variable
result = add_numbers(5, 7)
print(f"The sum is: {result}")

# Example 5: Function with multiple return values
def get_min_max(numbers):
    """
    This function returns the minimum and maximum values from a list.

    Parameters:
    numbers (list): A list of numbers.

    Returns:
    tuple: A tuple containing the minimum and maximum values.
    """
    return min(numbers), max(numbers)

# Using the function with multiple return values
min_val, max_val = get_min_max([1, 2, 3, 4, 5])
print(f"Minimum: {min_val}, Maximum: {max_val}")

# Example 6: Lambda function (anonymous function)
add = lambda x, y: x + y
print(f"Sum using lambda: {add(3, 4)}")
