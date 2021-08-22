from graph import Node, DirectedGraph

g = DirectedGraph()
s = Node('S')
r1 = Node('R1')
r2 = Node('R2')
c1 = Node('C1')
c2 = Node('C2')

g.add_multiple_nodes([s,r1,r2,c1,c2])
g.add_edge(r1,r2)

print(g)
print(g.edges)