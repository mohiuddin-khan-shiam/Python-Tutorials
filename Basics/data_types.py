# Basics/data_types.py

# This script demonstrates different data types in Python

# Integer
integer_value = 42
print("Integer:", integer_value, "Type:", type(integer_value))

# Float
float_value = 3.14159
print("Float:", float_value, "Type:", type(float_value))

# String
string_value = "Hello, Python!"
print("String:", string_value, "Type:", type(string_value))

# Boolean
boolean_value = True
print("Boolean:", boolean_value, "Type:", type(boolean_value))

# List
list_value = [1, 2, 3, 4, 5]
print("List:", list_value, "Type:", type(list_value))

# Tuple
tuple_value = (10, 20, 30)
print("Tuple:", tuple_value, "Type:", type(tuple_value))

# Set
set_value = {"apple", "banana", "cherry"}
print("Set:", set_value, "Type:", type(set_value))

# Dictionary
dict_value = {"name": "Alice", "age": 25, "city": "New York"}
print("Dictionary:", dict_value, "Type:", type(dict_value))

# NoneType
none_value = None
print("NoneType:", none_value, "Type:", type(none_value))

# Complex
complex_value = 2 + 3j
print("Complex:", complex_value, "Type:", type(complex_value))

# Demonstrating dynamic typing
variable = 10  # Initially an integer
print("Variable as Integer:", variable, "Type:", type(variable))

variable = "Now I'm a string"  # Now a string
print("Variable as String:", variable, "Type:", type(variable))
