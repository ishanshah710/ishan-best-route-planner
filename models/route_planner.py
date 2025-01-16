import itertools
from typing import List

from exceptions import InvalidOrderError
from models.delivery_order import DeliveryOrder
from models.geo_location import GeoLocation


class RoutePlanner:
    """
    Plans the optimal delivery route for a batch of orders.
    """
    def __init__(self, base_location: GeoLocation, orders: List[DeliveryOrder] = []):
        self.orders = orders
        self.base_location = base_location

    def add_order(self, order: DeliveryOrder):
        if not isinstance(order, DeliveryOrder):
            raise InvalidOrderError("Order must be a valid DeliveryOrder object.")
        self.orders.append(order)

    def set_order(self, orders: List[DeliveryOrder]):
        self.orders = orders

    def get_best_route(self):
        """Calculate the best route by trying all permutations and selecting the one with the shortest total time."""
        best_route = None
        shortest_time = float('inf')
        
        # Generate all permutations of the orders (pickup and delivery order)
        all_possible_order_paths = itertools.permutations(self.orders)
        
        for path in all_possible_order_paths:
            if not path:
                continue

            total_time = 0
            route = []
            current_location = self.base_location
            
            # Calculate the total time for the current permutation
            for order in path:
                route.append(order)
                total_time += current_location.calculate_travel_time(order.restaurant_location)
                total_time += order.get_order_time()
                current_location = order.customer_location
            
            if total_time < shortest_time:
                shortest_time = total_time
                best_route = route

        return best_route, shortest_time