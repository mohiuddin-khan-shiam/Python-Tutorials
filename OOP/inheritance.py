# OOP/inheritance.py

# This script demonstrates the concept of inheritance in Python

# Parent class (Base class)
class Animal:
    """
    A class to represent a generic animal.
    """
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

# Child class (Derived class) inheriting from Animal
class Dog(Animal):
    """
    A class to represent a dog, inheriting from Animal.
    """
    def __init__(self, name, breed):
        super().__init__(name)  # Calling the constructor of the parent class
        self.breed = breed

    def speak(self):
        print(f"{self.name} barks.")

# Another child class inheriting from Animal
class Cat(Animal):
    """
    A class to represent a cat, inheriting from Animal.
    """
    def speak(self):
        print(f"{self.name} meows.")

# Creating objects of the derived classes
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers")

# Calling methods on objects
print("Dog Details:")
dog.speak()  # Overridden method
print(f"Breed: {dog.breed}")

print("\nCat Details:")
cat.speak()  # Overridden method

# Demonstrating polymorphism
print("\nPolymorphism Example:")

animals = [dog, cat]
for animal in animals:
    animal.speak()
