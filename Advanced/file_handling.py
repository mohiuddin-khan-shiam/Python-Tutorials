# Advanced/file_handling.py

# This script demonstrates basic file handling operations in Python

# Example 1: Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, this is a file handling example.\n")
    file.write("This is the second line.\n")

print("Data written to 'example.txt'.")

# Example 2: Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print("\nContent of 'example.txt':")
    print(content)

# Example 3: Reading a file line by line
with open("example.txt", "r") as file:
    print("Reading file line by line:")
    for line in file:
        print(line.strip())  # strip() removes the newline character

# Example 4: Appending to a file
with open("example.txt", "a") as file:
    file.write("This line is appended to the file.\n")

print("\nNew line appended to 'example.txt'.")

# Example 5: Reading the updated file
with open("example.txt", "r") as file:
    print("\nUpdated content of 'example.txt':")
    print(file.read())

# Example 6: Using try-except for error handling
try:
    with open("non_existent_file.txt", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("\nError: The file 'non_existent_file.txt' does not exist.")

# Example 7: Writing and reading JSON data
import json

# Writing JSON data
data = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

with open("data.json", "w") as json_file:
    json.dump(data, json_file)

print("\nJSON data written to 'data.json'.")

# Reading JSON data
with open("data.json", "r") as json_file:
    loaded_data = json.load(json_file)
    print("\nContent of 'data.json':")
    print(loaded_data)
