from exceptions import InvalidOrderError
from models.geo_location import GeoLocation


class DeliveryOrder:
    """
    Represents an order with its associated restaurant and customer.
    """
    def __init__(
            self, 
            restaurant: GeoLocation, 
            customer: GeoLocation, 
            preparation_time: float
    ):
        self.restaurant_location = restaurant
        self.customer_location = customer
        self.preparation_time = preparation_time
        self.validate()

    
    def validate(self):
        if not isinstance(self.restaurant_location, GeoLocation) or not isinstance(self.customer_location, GeoLocation):
            raise InvalidOrderError("Restaurant and Customer locations must be valid GeoLocation objects.")

    def get_order_time(self):
        """Returns the total time for the order considering travel and preparation time."""
        travel_time = self.restaurant_location.calculate_travel_time(self.customer_location)
        total_time = travel_time + self.preparation_time
        return total_time