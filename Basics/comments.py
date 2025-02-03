# Basics/comments.py

# This script demonstrates how to use comments in Python

# Single-line comment:
# This is a single-line comment explaining that the next line prints a message.
print("Hello, this is an example of a single-line comment!")

# You can also place single-line comments next to code:
name = "Alice"  # This variable stores the user's name
print("Name:", name)

# Multi-line comments:
# You can use multiple single-line comments to create a multi-line explanation.
# This section will demonstrate how to use multi-line comments in your code.

print("This is an example of multi-line comments using multiple # symbols.")

"""
Alternatively, you can use triple quotes (single or double) for multi-line comments.
This method is also used for writing docstrings in functions, classes, or modules.
The code below demonstrates the use of triple-quoted multi-line comments.
"""

print("This is an example of multi-line comments using triple quotes.")

# Function with a docstring (multi-line comment)
def greet(name):
    """
    This function takes a name as input and prints a greeting message.

    Parameters:
    name (str): The name of the person to greet.
    """
    print(f"Hello, {name}! Welcome to Python.")

# Calling the function
greet("Alice")
