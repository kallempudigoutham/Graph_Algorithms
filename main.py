from GraphInitialization import *
from DepthFirstSearch import depth_first_search
from ConnectedComponents import no_connected_components

no_of_nodes = 18

graph = initialise_graph(no_of_nodes);
graph = add_edge(graph, 0, 8)
graph = add_edge(graph, 1, 5)
graph = add_edge(graph, 2, 9)
graph = add_edge(graph, 3, 9)
graph = add_edge(graph, 4, 0)
graph = add_edge(graph, 5, 16)
graph = add_edge(graph, 5, 17)
graph = add_edge(graph, 6, 11)
graph = add_edge(graph, 7, 6)
graph = add_edge(graph, 8, 4)
graph = add_edge(graph, 8, 14)
graph = add_edge(graph, 9, 15)
graph = add_edge(graph, 11, 7)
graph = add_edge(graph, 13, 0)
graph = add_edge(graph, 14, 0)
graph = add_edge(graph, 14, 13)
graph = add_edge(graph, 15, 10)
graph = add_edge(graph, 15, 2)


visited = []
for i in range(no_of_nodes):
    visited.append(False)

print(graph)
depth_first_search_order = depth_first_search(graph, no_of_nodes, visited)

visited = []
for i in range(no_of_nodes):
    visited.append(False)

number_of_connected_components, search_order = no_connected_components(graph, no_of_nodes, visited)

print(number_of_connected_components)
print(search_order)
