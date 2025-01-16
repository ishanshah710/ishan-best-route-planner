from typing import List, Tuple
from models.delivery_order import DeliveryOrder
from models.geo_location import GeoLocation
from models.route_planner import RoutePlanner


def display_intro():
    """
    Display an introduction message to the user.
    """
    print("\nWelcome to the Delivery Route Planner!")
    print("This tool calculates the optimal route to deliver multiple orders in the shortest time possible.\n")

def get_sample_orders():
    """
    Generate sample orders for demonstration.
    """
    order_1 = DeliveryOrder(
        restaurant=GeoLocation("Restaurant1", 12.935662, 77.625918),
        customer=GeoLocation("Customer1", 12.936544, 77.622244),
        preparation_time=10  # minutes
    )
    order_2 = DeliveryOrder(
        restaurant=GeoLocation("Restaurant2", 12.937762, 77.627918),
        customer=GeoLocation("Customer2", 12.938662, 77.629244),
        preparation_time=15  # minutes
    )
    return [order_1, order_2]

def display_results(route: List[Tuple[GeoLocation, str]], total_time: float):
    """
    Display the results of the optimal route calculation.
    """
    print("Optimal Delivery Route:")
    for order in route:
        print(f"{order.restaurant_location.name} "
              f"-> {order.customer_location.name}")   
    
    print(f"Total Delivery Time: {total_time:.2f} minutes")

if __name__ == "__main__":
    # Main execution flow
    display_intro()
    base_location = GeoLocation("Base", 12.934533, 77.626579) # Aman's starting point
    orders = get_sample_orders()

    # Initialize the planner and calculate the best route
    planner = RoutePlanner(base_location, orders)
    best_route, total_delivery_time = planner.get_best_route()

    # Display the calculated optimal route
    display_results(best_route, total_delivery_time)
