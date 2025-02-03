# ControlFlow/switch_case.py

# This script demonstrates the use of match-case (similar to switch-case) in Python 3.10+

# Example 1: Basic match-case

choice = 2

match choice:
    case 1:
        print("You selected option 1.")
    case 2:
        print("You selected option 2.")
    case 3:
        print("You selected option 3.")
    case _:
        print("Invalid option selected.")

# Example 2: Matching strings

fruit = "apple"

match fruit:
    case "apple":
        print("You chose an apple.")
    case "banana":
        print("You chose a banana.")
    case "cherry":
        print("You chose a cherry.")
    case _:
        print("Unknown fruit.")

# Example 3: Using guards (conditions within cases)

number = 15

match number:
    case n if n < 0:
        print("The number is negative.")
    case n if n == 0:
        print("The number is zero.")
    case n if n % 2 == 0:
        print("The number is even.")
    case _:
        print("The number is odd.")

# Example 4: Matching with multiple values

value = "B"

match value:
    case "A" | "B" | "C":
        print(f"{value} is a grade between A and C.")
    case "D" | "E":
        print(f"{value} is a lower grade.")
    case _:
        print("Unknown grade.")
