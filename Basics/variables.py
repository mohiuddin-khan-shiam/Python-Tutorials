# Basics/variables.py

# This script demonstrates how to declare and use variables in Python

# Declaring variables of different data types
name = "Alice"          # String variable
age = 25                # Integer variable
height = 5.7            # Float variable
is_student = True       # Boolean variable

# Printing the values of the variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Changing the value of a variable
age = 26  # Updating the age
print("Updated Age:", age)

# Multiple assignments in one line
x, y, z = 1, 2, 3
print("Values of x, y, z:", x, y, z)

# Assigning the same value to multiple variables
a = b = c = 100
print("Values of a, b, c:", a, b, c)

# Concatenating strings
greeting = "Hello, " + name + "!"
print(greeting)

# Combining strings and numbers using f-strings
print(f"{name} is {age} years old and {height} feet tall.")
