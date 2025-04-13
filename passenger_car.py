"""
Passenger Car Module

This module defines the `PassengerCar` class, which is a concrete implementation of the abstract `Car` class.
It represents passenger cars in the rental system and includes functionality to calculate the total rental price,
with discounts applied for rentals longer than 7 days.

Classes:
    - PassengerCar: Represents a passenger car in the rental system.
"""

from base_car import Car


class PassengerCar(Car):
    """
    Represents a passenger car in the rental system.

    Inherits from:
        Car (abstract class): The base class for all car types.

    Methods:
        - calculate_total_price(rental_duration: int) -> int:
            Calculates the total rental price for the car, applying a discount for rentals longer than 7 days.
    """

    def __init__(self, license_plate: str, car_type: str, rental_cost: int):
        """
        Initializes a PassengerCar instance.

        Args:
            license_plate (str): The license plate of the car.
            car_type (str): The type or model of the car.
            rental_cost (int): The rental cost per day in HUF.
        """
        super().__init__(license_plate, car_type, rental_cost)

    def calculate_total_price(self, rental_duration: int) -> int:
        """
        Calculates the total rental price for the car.

        Args:
            rental_duration (int): The duration of the rental in days.

        Returns:
            int: The total rental price in HUF.

        Raises:
            ValueError: If rental_duration is not a positive integer.

        Notes:
            - A 10% discount is applied for rentals longer than 7 days.
        """
        if not isinstance(rental_duration, int):
            raise ValueError("You can only rent cars for full days.")

        if rental_duration <= 0:
            raise ValueError("Do you actually want to rent a car?")

        total_price = self.price_per_day * rental_duration
        if rental_duration > 7:
            print(
                """We offer a 10% discount for durations longer than 7 days.
                The discount will be automatically applied at checkout."""
            )
            return round(total_price * 0.9)
        return total_price
