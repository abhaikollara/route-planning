from collections.abc import Iterable
from itertools import permutations

from graph import Graph, Node
from location import Location, travel_time


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


def generate_graph(start_position: Location, orders: Iterable[Order]) -> Graph:
    """
    Given a start position and a list of orders, generate a weighted graph
    """

    g = Graph()

    for order in orders:
        rn = Node(
            id=order.restaurant.name,
            data={"location": order.restaurant.location, "type": "restaurant"},
        )
        cn = Node(
            id=order.customer.name,
            data={
                "location": order.customer.location,
                "pre_req": rn,
                "type": "customer",
            },
        )
        g.add_node(rn)
        g.add_node(cn)

    for n1 in g.nodes.values():
        for n2 in g.nodes.values():
            if n1 is not n2:
                weight = travel_time(n1.data["location"], n2.data["location"], 20)
                g.add_edge(n1, n2, weight, bidirectional=True)

    start = Node("START", data={"location": start_position, "type": "start"})
    g.add_node(start)

    for n in g.nodes.values():
        if n.data.get("type") == "restaurant":
            weight = travel_time(start.data["location"], n.data["location"], 20)
            g.add_edge(start, n, weight=weight, bidirectional=True)

    return g


# This should be implement the actual solution
def find_optimal_delivery_path(start_position: Location, order_list: Iterable[Order]) -> Iterable[Location]:
    g = generate_graph(start_position, order_list)

    valid_paths = generate_valid_paths(g)
    shortest_path = sorted(valid_paths, key=g.path_cost)[0]

    return [n.data["location"] for n in shortest_path]


def generate_valid_paths(graph):
    # We start from start location and generate all permutations of node visitation
    nodes = [n for n in graph.nodes.values()]

    valid_paths = []  # This will contain only the paths that satisfy the prerequiste condition
    # i.e restaurant must be visited before customer

    for path in permutations(nodes):
        if is_valid_path(path):
            valid_paths.append(path)

    return valid_paths


def is_valid_path(path):
    visited = set()  # Keep track of visited nodes to see if a prerequiste node has been visited
    if path[0].data.get("type") != "start":
        return False

    for n in path:
        visited.add(n)
        prereq = n.data.get("pre_req")
        if prereq and prereq not in visited:
            return False

    return True
