from collections import namedtuple
from typing import Iterable

Edge = namedtuple("Edge", ["node", "weight"])

class Node:
    def __init__(self, id: str, data=None) -> None:
        self.id = id
        self.data = data # Any data associated with the node

    def __repr__(self) -> str:
        return f"Node({self.id})"

    def __str__(self) -> str:
        return f"Node({self.id})"

class Graph:
    def __init__(self, nodes={}) -> None:
        self.nodes = nodes
        self.edges = {}

    def add_node(self, node) -> None:
        self.nodes[node.id] = node

    def add_multiple_nodes(self, node_list) -> None:
        for n in node_list:
            self.add_node(n)

    def add_edge(self, n1: str, n2: str, weight=0, bidirectional=False) -> None:
        if n1 in self.edges:
            self.edges[n1].add(Edge(n2, weight))
        else:
            self.edges[n1] = {Edge(n2, weight)}

        if bidirectional:
            if n2 in self.edges:
                self.edges[n2].add(Edge(n1, weight))
            else:
                self.edges[n2] = {Edge(n1, weight)}

    def add_bidirectional_edges(self, n1: str, n2: str) -> None:
        self.add_directed_edge(n1, n2)
        self.add_directed_edge(n2, n1)

    def path_cost(self, nodes: Iterable[Node]) -> float:
        total_cost = 0.0
        for i, n in enumerate(nodes[1:]):
            edges = self.edges.get(n)
            if edges:
                for e in edges:
                    if e.node == nodes[i-1]:
                        total_cost += e.weight
        
        return total_cost


    def __repr__(self) -> str:
        return f"DirectedGraph({repr(self.nodes)})"

    def __str__(self) -> str:
        return f"DirectedGraph({repr(self.nodes)})"

