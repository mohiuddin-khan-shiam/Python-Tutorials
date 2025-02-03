# OOP/classes_and_objects.py

# This script demonstrates how to define classes and create objects in Python

# Defining a class
class Car:
    """
    A class to represent a car.

    Attributes:
    brand (str): The brand of the car.
    model (str): The model of the car.
    year (int): The year the car was manufactured.
    """

    def __init__(self, brand, model, year):
        """
        The constructor for the Car class.

        Parameters:
        brand (str): The brand of the car.
        model (str): The model of the car.
        year (int): The year the car was manufactured.
        """
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        """
        Method to display information about the car.
        """
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")

# Creating objects of the Car class
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Honda", "Civic", 2022)

# Calling methods on objects
print("Car 1 Details:")
car1.display_info()

print("\nCar 2 Details:")
car2.display_info()

# Accessing attributes directly
print(f"\nThe brand of car1 is {car1.brand}.")
