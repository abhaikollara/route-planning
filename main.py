# from graph import DirectedGraph, Node
from lib import Customer, Location, Order, Restaurant, find_optimal_delivery_path, generate_graph
from pprint import pprint

start_location = Location(75.40322081327923, 13.222724042514256)
R1 = Restaurant("R1", Location(74.67418178783742, 13.123723901464716))
R2 = Restaurant("R2", Location(74.47418178483742, 13.223723901464716))
C1 = Customer("C1", Location(74.17428178783742, 13.323763901464716))
C2 = Customer("C2", Location(74.27418174483742, 13.423623901464716))

o1 = Order(C1, R1, 0.2)
o2 = Order(C2, R2, 0.3)

g = generate_graph(start_location, [o1, o2])
pprint(g)
pprint(g.edges)
