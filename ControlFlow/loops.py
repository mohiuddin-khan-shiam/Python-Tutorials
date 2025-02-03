# ControlFlow/loops.py

# This script demonstrates different types of loops in Python

# For Loop Example
print("--- For Loop ---")
for i in range(1, 6):  # Loop from 1 to 5
    print(f"Iteration {i}")

# Iterating over a list
fruits = ["apple", "banana", "cherry"]
print("\n--- Iterating over a list ---")
for fruit in fruits:
    print(f"Fruit: {fruit}")

# While Loop Example
print("\n--- While Loop ---")
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# Do-While Loop Simulation (Python doesn't have a native do-while loop)
print("\n--- Do-While Loop Simulation ---")
number = 1
while True:
    print(f"Number: {number}")
    number += 1
    if number > 5:
        break

# Nested Loops Example
print("\n--- Nested Loops ---")
for i in range(1, 4):
    for j in range(1, 4):
        print(f"i = {i}, j = {j}")

# Loop with Else Clause
print("\n--- Loop with Else Clause ---")
for num in range(1, 4):
    print(f"Number: {num}")
else:
    print("Loop completed!")

# Breaking out of a loop
print("\n--- Break Statement ---")
for i in range(1, 10):
    if i == 5:
        print("Breaking the loop at i = 5")
        break
    print(f"i = {i}")

# Skipping an iteration with continue
print("\n--- Continue Statement ---")
for i in range(1, 6):
    if i == 3:
        print("Skipping iteration at i = 3")
        continue
    print(f"i = {i}")
