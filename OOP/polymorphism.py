# OOP/polymorphism.py

# This script demonstrates the concept of polymorphism in Python

# Base class
class Animal:
    """
    A class to represent a generic animal.
    """
    def speak(self):
        return "The animal makes a sound."

# Derived class 1
class Dog(Animal):
    """
    A class to represent a dog, inheriting from Animal.
    """
    def speak(self):
        return "The dog barks."

# Derived class 2
class Cat(Animal):
    """
    A class to represent a cat, inheriting from Animal.
    """
    def speak(self):
        return "The cat meows."

# Function demonstrating polymorphism
def animal_sound(animal):
    """
    This function demonstrates polymorphism by calling the speak method 
    on any object that inherits from the Animal class.

    Parameters:
    animal (Animal): An object of type Animal or its derived classes.
    """
    print(animal.speak())

# Creating instances of each class
my_animal = Animal()
my_dog = Dog()
my_cat = Cat()

# Using the same function to call different behaviors
animal_sound(my_animal)  # Outputs: The animal makes a sound.
animal_sound(my_dog)     # Outputs: The dog barks.
animal_sound(my_cat)     # Outputs: The cat meows.

# Polymorphism with a list of objects
animals = [my_animal, my_dog, my_cat]

print("\nPolymorphism with a list of animals:")
for animal in animals:
    print(animal.speak())
