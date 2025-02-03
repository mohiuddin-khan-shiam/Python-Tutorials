# OOP/encapsulation.py

# This script demonstrates the concept of encapsulation in Python

class Person:
    """
    A class to represent a person using encapsulation.

    Attributes:
    __name (str): The name of the person (private).
    __age (int): The age of the person (private).
    """

    def __init__(self, name, age):
        """
        Constructor to initialize name and age.

        Parameters:
        name (str): The name of the person.
        age (int): The age of the person.
        """
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for name
    def set_name(self, name):
        self.__name = name

    # Getter for age
    def get_age(self):
        return self.__age

    # Setter for age with validation
    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age must be positive.")

    # Method to display person information
    def display_info(self):
        print(f"Name: {self.__name}, Age: {self.__age}")

# Creating an object of the Person class
person = Person("Alice", 25)

# Accessing data using getters
print("Initial Information:")
print(f"Name: {person.get_name()}")
print(f"Age: {person.get_age()}")

# Modifying data using setters
person.set_name("Bob")
person.set_age(30)

# Displaying updated information
print("\nUpdated Information:")
person.display_info()

# Attempting to set an invalid age
print("\nAttempting to set an invalid age:")
person.set_age(-5)  # This will trigger validation
