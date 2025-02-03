# Functions/lambda_functions.py

# This script demonstrates the use of lambda (anonymous) functions in Python

# Example 1: Basic lambda function for addition
add = lambda a, b: a + b
print(f"Sum using lambda: {add(5, 3)}")

# Example 2: Lambda function for squaring a number
square = lambda x: x ** 2
print(f"Square of 4: {square(4)}")

# Example 3: Lambda function with no arguments
no_args = lambda: "Hello from a lambda function!"
print(no_args())

# Example 4: Using lambda with filter() to filter even numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(f"Even numbers: {even_numbers}")

# Example 5: Using lambda with map() to square each number
squared_numbers = list(map(lambda x: x ** 2, numbers))
print(f"Squared numbers: {squared_numbers}")

# Example 6: Using lambda with sorted() to sort by custom key
people = [("Alice", 25), ("Bob", 20), ("Charlie", 30)]
sorted_by_age = sorted(people, key=lambda person: person[1])
print(f"People sorted by age: {sorted_by_age}")

# Example 7: Lambda function inside another function
def make_multiplier(factor):
    """
    Returns a lambda function that multiplies its input by a given factor.
    """
    return lambda x: x * factor

# Creating a doubler function
doubler = make_multiplier(2)
print(f"Doubled value of 5: {doubler(5)}")

# Creating a tripler function
tripler = make_multiplier(3)
print(f"Tripled value of 5: {tripler(5)}")
