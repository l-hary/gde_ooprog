"""
Company Module

This module defines the `Company` class, which represents a car rental company.
The company manages a collection of cars and provides functionality to add cars
to its inventory.

Classes:
    - Company: Represents a car rental company.
"""

from base_car import Car


class Company:
    """
    Represents a car rental company.

    Attributes:
        name (str): The name of the company.
        _cars (list[Car]): A list of cars managed by the company.

    Methods:
        - __str__(): Returns the name of the company.
        - __add__(car: Car) -> "Company": Adds a car to the company's inventory.
        - cars: Property to get the list of cars.
    """

    def __init__(self, name: str, cars: list[Car]):
        """
        Initializes a Company instance.

        Args:
            name (str): The name of the company.
            cars (list[Car]): A list of cars to initialize the company's inventory.

        Raises:
            ValueError: If any item in the cars list is not an instance of `Car`.
        """
        self.name = name
        self._cars = []

        for car in cars:
            if not isinstance(car, Car):
                raise ValueError("Only cars pls.")
            self._cars.append(car)

    def __str__(self) -> str:
        """
        Returns the name of the company.

        Returns:
            str: The name of the company.
        """
        return self.name

    def __add__(self, car: Car) -> "Company":
        """
        Adds a car to the company's inventory.

        Args:
            car (Car): The car to add.

        Returns:
            Company: The updated company instance.

        Raises:
            ValueError: If the provided object is not an instance of `Car`.
        """
        if not isinstance(car, Car):
            raise ValueError("You can only add cars.")

        self._cars.append(car)
        return self

    @property
    def cars(self) -> list[Car]:
        """
        Gets the list of cars managed by the company.

        Returns:
            list[Car]: The list of cars.
        """
        return self._cars
