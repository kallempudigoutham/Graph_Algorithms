from GraphInitialization import *
from DepthFirstSearch import depth_first_search

no_of_nodes = 6

graph = initialise_graph(no_of_nodes);
graph = add_edge(graph, 0, 1)
graph = add_edge(graph, 0, 5)
graph = add_edge(graph, 1, 2)
graph = add_edge(graph, 1, 3)
graph = add_edge(graph, 3, 4)


visited = []
for i in range(no_of_nodes):
    visited.append(False)

print(graph)
print(depth_first_search(graph, no_of_nodes, visited))
