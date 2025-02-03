# Advanced/generators.py

# This script demonstrates the use of generators in Python

# Example 1: Basic generator function
def simple_generator():
    """
    A simple generator that yields numbers from 1 to 3.
    """
    yield 1
    yield 2
    yield 3

# Using the generator
gen = simple_generator()
print("--- Simple Generator ---")
for value in gen:
    print(value)

# Example 2: Generator with a loop
def number_generator(n):
    """
    A generator that yields numbers from 0 to n-1.

    Parameters:
    n (int): The number of values to generate.
    """
    for i in range(n):
        yield i

print("\n--- Number Generator ---")
for num in number_generator(5):
    print(num)

# Example 3: Generator expression
print("\n--- Generator Expression ---")
squares = (x ** 2 for x in range(5))
for square in squares:
    print(square)

# Example 4: Using next() with generators
def countdown(n):
    """
    A generator that counts down from n to 1.

    Parameters:
    n (int): The starting number for the countdown.
    """
    while n > 0:
        yield n
        n -= 1

print("\n--- Countdown Generator ---")
count_gen = countdown(3)
print(next(count_gen))  # Output: 3
print(next(count_gen))  # Output: 2
print(next(count_gen))  # Output: 1

# Example 5: Infinite generator
def infinite_counter():
    """
    A generator that yields numbers indefinitely.
    """
    num = 0
    while True:
        yield num
        num += 1

print("\n--- Infinite Generator (first 5 values) ---")
inf_gen = infinite_counter()
for _ in range(5):
    print(next(inf_gen))

# Example 6: Generator for Fibonacci sequence
def fibonacci_sequence(limit):
    """
    A generator for the Fibonacci sequence up to a specified limit.

    Parameters:
    limit (int): The number of Fibonacci numbers to generate.
    """
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b

print("\n--- Fibonacci Sequence ---")
for fib in fibonacci_sequence(10):
    print(fib)
