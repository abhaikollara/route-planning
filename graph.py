from collections import namedtuple

Edge = namedtuple("Edge", ["node", "weight"])


class DirectedGraph:
    def __init__(self, nodes={}) -> None:
        self.nodes = nodes
        self.edges = {}

    def add_node(self, node) -> None:
        self.nodes[node.name] = node

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

    def __repr__(self) -> str:
        return f"DirectedGraph({repr(self.nodes)})"

    def __str__(self) -> str:
        return f"DirectedGraph({repr(self.nodes)})"


class Node:
    def __init__(self, name: str) -> None:
        self.name = name

    def __repr__(self) -> str:
        return f"Node({self.name})"

    def __str__(self) -> str:
        return f"Node({self.name})"
