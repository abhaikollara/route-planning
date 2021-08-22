from collections.abc import Iterable
from location import Location, travel_time
from graph import Graph, Node

class Restaurant:
    def __init__(self, name: str, location: Location) -> None:
        self.name = name
        self.location = location


class Customer:
    def __init__(self, name: str, location: Location) -> None:
        self.name = name
        self.location = location

class StartLocation:
    def __init__(self, location: Location) -> None:
        self.location = location

class Order:
    def __init__(self, customer: Customer, restaurant: Restaurant, prep_time: float):
        self.customer = customer
        self.restaurant = restaurant
        self.prep_time = prep_time


def generate_graph(start_position: Location, orders: Iterable[Order]) -> Graph:
    g = Graph()
    start = Node('START', data=StartLocation(start_position))
    g.add_node(start)

    for order in orders:
        g.add_node(Node(id=order.customer.name, data=order.customer))
        g.add_node(Node(id=order.restaurant.name, data=order.restaurant))

    for n1 in g.nodes.values():
        for n2 in g.nodes.values():
            if n1 is not n2:
                print(n1.data == n2.data)
                weight = travel_time(n1.data.location, n2.data.location, 20)
                g.add_edge(n1, n2, weight)

    return g

def find_optimal_delivery_path(start_position: Location, order_list: Iterable[Order]) -> Iterable[Location]:
    g = generate_graph(start_position, order_list)

    # Generate the minimum spanning tree here ?

    return g