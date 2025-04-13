from base_car import Car


class Truck(Car):
    booking_block = 2

    def __init__(self, license_plate, car_type, rental_cost):
        super().__init__(license_plate, car_type, rental_cost)

    def calculate_total_price(self, rental_duration: int) -> int:
        if not isinstance(rental_duration, int):
            raise ValueError("You can only rent cars for full days.")

        if rental_duration <= 0:
            raise ValueError("Do you actually want to rent a car?")

        if rental_duration % self.booking_block != 0:
            raise ValueError(
                f"Trucks can only be booked in {self.booking_block}-day blocks."
            )

        return self.price_per_day * rental_duration
