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
    '''
        Wrapper class for start location
        which is neither a restaurant or a customer
    '''

    def __init__(self, location: Location) -> None:
        self.location = location

class Order:
    def __init__(self, customer: Customer, restaurant: Restaurant, prep_time: float):
        self.customer = customer
        self.restaurant = restaurant
        self.prep_time = prep_time

def generate_graph(start_position: Location, orders: Iterable[Order]) -> Graph:
    '''
        Given a start position and a list of orders, generate a weighted graph
    '''

    g = Graph()

    for order in orders:
        g.add_node(Node(id=order.customer.name, data=order.customer))
        g.add_node(Node(id=order.restaurant.name, data=order.restaurant))

    for n1 in g.nodes.values():
        for n2 in g.nodes.values():
            if n1 is not n2:
                print(n1.data == n2.data)
                weight = travel_time(n1.data.location, n2.data.location, 20)
                g.add_edge(n1, n2, weight, bidirectional=True)

    start = Node('START', data=StartLocation(start_position))
    g.add_node(start)

    for n in g.nodes.values():
        if isinstance(n.data, Restaurant):
            g.add_edge(start, n, bidirectional=True)

    return g

# This should be implement the actual solution
def find_optimal_delivery_path(start_position: Location, order_list: Iterable[Order]) -> Iterable[Location]:
    g = generate_graph(start_position, order_list)

    # Generate all possible valid paths here and check the sum of weights ?
    # Minimum spanning tree here ?

    return g