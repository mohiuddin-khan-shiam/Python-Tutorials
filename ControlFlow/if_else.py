# ControlFlow/if_else.py

# This script demonstrates how to use if-else statements in Python

# Example 1: Basic if-else
number = 10

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

# Example 2: Checking even or odd
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# Example 3: Nested if-else
age = 20

if age >= 18:
    if age >= 65:
        print("You are a senior citizen.")
    else:
        print("You are an adult.")
else:
    print("You are a minor.")

# Example 4: Using logical operators
has_id = True
is_over_18 = False

if has_id and is_over_18:
    print("You are allowed to enter.")
elif has_id and not is_over_18:
    print("You have an ID but are underage.")
else:
    print("No ID, entry denied.")
