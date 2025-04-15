from datetime import datetime, timedelta

from customer import Customer
from passenger_car import PassengerCar
from truck import Truck


class RentalManager:
    def __init__(self):
        self.rentals: list["Rental"] = []

    def __str__(self):
        return ", ".join(
            [
                f"{rental.car.car_type}: {rental.car.license_plate}"
                for rental in self.rentals
            ]
        )  # Readability counts. Except when it doesn't.

    def book_car(
        self,
        car: PassengerCar | Truck,
        duration: int,
        customer: Customer,
        start_date: datetime,
    ) -> None:
        if duration < 1:
            raise ValueError("Rental duration must be at least 1 day!")
        if not car.availability:
            # ? print all available cars of the same class for user
            # not going to create a custom Exception class for this
            raise Exception(f"{car} is already booked!")

        rental = Rental(
            car=car,
            customer=customer,
            days=duration,
            total_price=car.calculate_total_price(duration),
            start_date=start_date,
        )
        self.rentals.append(rental)

    def remove_rental(self, rental: "Rental"):
        if rental in self.rentals:
            rental.close_rental()
            self.rentals.remove(rental)


class Rental:
    def __init__(  # pylint hates how many arguments this has
        self,
        car: PassengerCar | Truck,
        customer: Customer,
        days: int,
        total_price: int,
        start_date: datetime,
    ):
        self.car = car
        self.customer = customer
        self.days = days
        self.total_price = total_price
        self.start_date = self.validate_date(start_date)
        self.end_date = self.start_date + timedelta(days=self.days)
        self.is_active = True
        self.car.availability = False

    def __str__(self):
        return (
            f"Rental: {self.car} to {self.customer} for {self.days} days, "
            f"Total: {self.total_price} HUF, "
            f"Active: {self.is_active}"
        )

    def validate_date(self, start_date: datetime) -> datetime:
        if not isinstance(start_date, datetime):
            raise TypeError("Date is not a date. Also, the cake is a lie.")
        if start_date < datetime.now():
            raise ValueError(
                "All timeturners have been destroyed and we don't offer DeLoreans to rent."
            )
        return start_date

    def close_rental(self) -> None:
        self.car.availability = True
        self.is_active = False
