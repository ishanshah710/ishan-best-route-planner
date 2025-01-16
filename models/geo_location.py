
from constants import AVG_SPEED_KMPH
from exceptions import InvalidLocationError
from utils import get_haversine_distance


class GeoLocation:
    """
    Represents a geographic location with latitude and longitude.
    """
    def __init__(self, name: str, latitude: float, longitude: float):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.validate()

    def validate(self):
        if not (-90 <= self.latitude <= 90) or not (-180 <= self.longitude <= 180):
            raise InvalidLocationError("Invalid latitude or longitude values.")

    def calculate_distance(self, other: 'GeoLocation') -> float:
        """
        Calculate the Haversine distance (in kilometers) between two locations.
        """
        return get_haversine_distance(
            self.latitude, 
            self.longitude, 
            other.latitude, 
            other.longitude
        )

    def calculate_travel_time(self, other: 'GeoLocation', avg_speed_kmph=AVG_SPEED_KMPH) -> float:
        distance = self.calculate_distance(other)
        time = distance / avg_speed_kmph * 60  # Time in minutes
        return time
