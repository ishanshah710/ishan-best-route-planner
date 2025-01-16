from math import radians, sin, cos, sqrt, atan2
from constants import EARTH_RADIUS_KM


def get_haversine_distance(latitude1, longitude1, latitude2, longitude2):
    """
    Calculate the Haversine distance between two locations.
    """
    delta_latitude = radians(latitude2 - latitude1)
    delta_longitude = radians(longitude2 - longitude1)
    
    haverinse = sin(delta_latitude / 2) ** 2 + cos(radians(latitude1)) * cos(radians(latitude2)) * sin(delta_longitude / 2) ** 2
    central_angle = 2 * atan2(sqrt(haverinse), sqrt(1 - haverinse))
    
    return EARTH_RADIUS_KM * central_angle
