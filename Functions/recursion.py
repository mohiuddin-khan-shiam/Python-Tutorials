# Functions/recursion.py

# This script demonstrates the concept of recursion in Python

# Example 1: Basic recursive function to calculate factorial
def factorial(n):
    """
    This function returns the factorial of a given number using recursion.

    Parameters:
    n (int): The number to calculate the factorial for.

    Returns:
    int: The factorial of the number.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Calculating factorial of 5
print(f"Factorial of 5: {factorial(5)}")

# Example 2: Recursive function to calculate Fibonacci numbers
def fibonacci(n):
    """
    This function returns the nth Fibonacci number using recursion.

    Parameters:
    n (int): The position in the Fibonacci sequence.

    Returns:
    int: The nth Fibonacci number.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Printing the first 10 Fibonacci numbers
print("\nFirst 10 Fibonacci numbers:")
for i in range(10):
    print(fibonacci(i), end=" ")

# Example 3: Recursive function to sum elements of a list
def sum_list(numbers):
    """
    This function returns the sum of all elements in a list using recursion.

    Parameters:
    numbers (list): A list of numbers.

    Returns:
    int: The sum of the list elements.
    """
    if not numbers:
        return 0
    else:
        return numbers[0] + sum_list(numbers[1:])

# Summing elements of a list
num_list = [1, 2, 3, 4, 5]
print(f"\n\nSum of {num_list}: {sum_list(num_list)}")

# Example 4: Recursive function to reverse a string
def reverse_string(s):
    """
    This function returns the reversed version of a string using recursion.

    Parameters:
    s (str): The string to reverse.

    Returns:
    str: The reversed string.
    """
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string(s[:-1])

# Reversing a string
input_string = "recursion"
print(f"\nReversed '{input_string}': {reverse_string(input_string)}")
