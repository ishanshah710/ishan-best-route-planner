import unittest

from exceptions import InvalidOrderError
from models.delivery_order import DeliveryOrder
from models.geo_location import GeoLocation
from models.route_planner import RoutePlanner


class TestDeliveryRoutePlanner(unittest.TestCase):

    def setUp(self):
        self.base_location = GeoLocation("Base",12.9352, 77.6241)
        self.R1_location = GeoLocation("Restaurant 1",12.9279, 77.6166)
        self.R2_location = GeoLocation("Restaurant 2",12.9350, 77.6250)
        self.C1_location = GeoLocation("Customer 1",12.9358, 77.6248)
        self.C2_location = GeoLocation("Customer 2",12.9345, 77.6234)

        self.order1 = DeliveryOrder(self.R1_location, self.C1_location, 15)
        self.order2 = DeliveryOrder(self.R2_location, self.C2_location, 20)
        self.planner = RoutePlanner(self.base_location)

    def test_add_valid_order(self):
        self.planner.set_order([self.order1])
        self.assertEqual(len(self.planner.orders), 1)

    def test_add_invalid_order(self):
        with self.assertRaises(InvalidOrderError):
            self.planner.add_order("InvalidOrder")

    def test_get_best_route(self):
        self.planner.set_order([self.order1, self.order2])
        best_route, total_time = self.planner.get_best_route()
        self.assertEqual(len(best_route), 2)
        self.assertGreater(total_time, 0)

    def test_single_order(self):
        self.planner.set_order([self.order1])
        best_route, total_time = self.planner.get_best_route()
        expected_time = (
            self.base_location.calculate_travel_time(self.order1.restaurant_location)
            + self.order1.preparation_time
            + self.order1.restaurant_location.calculate_travel_time(self.order1.customer_location)
        )
        self.assertAlmostEqual(total_time, expected_time, delta=0.1)

    def test_no_orders(self):
        self.planner.set_order([])
        best_route, total_time = self.planner.get_best_route()
        self.assertIsNone(best_route)
        self.assertEqual(total_time, float('inf'))
