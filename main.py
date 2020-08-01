from GraphInitialization import *;

graph = initialise_graph(3);
graph = add_edge(graph, 0, 2)
graph = add_edge(graph, 0, 1)
graph = add_edge(graph, 1, 2)
graph = add_edge(graph, 2, 0)
graph = remove_edge(graph, 0, 1)

print(graph)