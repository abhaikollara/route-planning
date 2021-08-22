import math
from collections.abc import Iterable


class Location:
    def __init__(self, x: float, y: float, name: str = None):
        self.x = x
        self.y = y
        self.name = name

    def __repr__(self) -> str:
        return f"Location({self.x}, {self.y})"


def haversine_distance(loc1: Location, loc2: Location) -> float:
    # Refer: https://community.esri.com/t5/coordinate-reference-systems-blog/distance-on-a-sphere-the-haversine-formula/ba-p/902128
    lon1, lat1 = loc1
    lon2, lat2 = loc2
    EARTH_RADIUS = 6371000  # radius of Earth in meters
    phi_1 = math.radians(lat1)
    phi_2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)
    a = (
        math.sin(delta_phi / 2.0) ** 2
        + math.cos(phi_1) * math.cos(phi_2) * math.sin(delta_lambda / 2.0) ** 2
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    meters = EARTH_RADIUS * c  # output distance in meters

    return meters


class Restaurant:
    def __init__(self, name: str, location: Location) -> None:
        self.name = name
        self.location = location


class Customer:
    def __init__(self, name: str, location: Location) -> None:
        self.name = name
        self.location = location


class Order:
    def __init__(self, customer: Customer, restaurant: Restaurant, prep_time: float):
        self.customer = customer
        self.restaurant = restaurant
        self.prep_time = prep_time


def find_optimal_path(start_position: Location, order_list: Iterable[Order]):
    raise NotImplementedError
