from abc import ABC, abstractmethod


class Car(ABC):
    """
    Abstract base class representing a car in a rental system.

    Attributes:
        license_plate (str): The license plate of the car.
        car_type (str): The type or model of the car.
        price_per_day (int): The rental cost per day in HUF.
        availability (bool): Indicates whether the car is available for rent.
    """

    def __init__(self, license_plate: str, car_type: str, rental_cost: int):
        """
        Initializes a Car instance.

        Args:
            license_plate (str): The license plate of the car.
            car_type (str): The type or model of the car.
            rental_cost (int): The rental cost per day in HUF.

        Raises:
            ValueError: If rental_cost is negative.
        """
        if rental_cost < 0:
            raise ValueError("Rental cost cannot be negative")
        self.license_plate = license_plate
        self.car_type = car_type
        self._price_per_day = rental_cost
        self._is_available = True

    def __str__(self) -> str:
        """
        Returns a string representation of the car.

        Returns:
            str: A string containing the car type, license plate, and rental cost.
        """
        return (
            f"{self.license_plate} | {self.car_type} | "
            f"{self.price_per_day} HUF per day."
        )

    @property
    def price_per_day(self) -> int:
        """
        Gets the rental price per day.

        Returns:
            int: The rental price per day in HUF.
        """
        return self._price_per_day

    @price_per_day.setter
    def price_per_day(self, price: int) -> None:
        """
        Sets the rental price per day.

        Args:
            price (int): The rental price per day in HUF.

        Raises:
            ValueError: If the price is negative.
        """
        if price < 0:
            raise ValueError("Price can't be negative")
        self._price_per_day = price

    @property
    def availability(self) -> bool:
        """
        Gets the availability status of the car.

        Returns:
            bool: True if the car is available, False otherwise.
        """
        return self._is_available

    @availability.setter
    def availability(self, available: bool) -> None:
        """
        Sets the availability status of the car.

        Args:
            available (bool): True if the car is available, False otherwise.

        Raises:
            ValueError: If the provided value is not a boolean.
        """
        if not isinstance(available, bool):
            raise ValueError("Car's either available or not.")
        self._is_available = available

    @abstractmethod
    def calculate_total_price(self, rental_duration: int) -> int:
        """
        Abstract method to calculate the total rental price.

        Args:
            rental_duration (int): The duration of the rental in days.

        Returns:
            int: The total rental price in HUF.

        Raises:
            ValueError: If rental_duration is negative or zero.
        """
