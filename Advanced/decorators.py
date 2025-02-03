# Advanced/decorators.py

# This script demonstrates how to use decorators in Python

# Example 1: Basic function decorator
def my_decorator(func):
    """
    A simple decorator that prints a message before and after a function call.
    """
    def wrapper():
        print("Before the function is called.")
        func()
        print("After the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello, World!")

# Calling the decorated function
say_hello()

# Example 2: Decorator with arguments
def repeat(n):
    """
    A decorator that repeats the function call 'n' times.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def greet(name):
    print(f"Hello, {name}!")

# Calling the decorated function with an argument
greet("Alice")

# Example 3: Decorator for measuring execution time
import time

def timing_decorator(func):
    """
    A decorator that measures the execution time of a function.
    """
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time:.4f} seconds")
        return result
    return wrapper

@timing_decorator
def slow_function():
    time.sleep(2)
    print("Finished slow function.")

# Calling the decorated function
slow_function()

# Example 4: Using multiple decorators
def uppercase_decorator(func):
    """
    A decorator that converts the result of a function to uppercase.
    """
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.upper()
    return wrapper

@uppercase_decorator
@my_decorator
def get_message():
    return "This is a decorated message."

# Calling the decorated function
print(get_message())
