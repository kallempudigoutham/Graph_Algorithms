from GraphInitialization import *


def breadth_first_search(graph_list, no_of_nodes, visited):
    search_order = []
    queue = []
    for node in range(no_of_nodes):
        if visited[node] is False:
            queue.append(node)
            search_order.append(node)
            bfs(graph_list, visited, search_order, queue)
    return search_order


def bfs(graph_list, visited, search_order, queue):
    if len(queue) == 0:
        return
    node = queue[0]
    queue.remove(node)
    visited[node] = True
    for i in range(len(graph_list[node])):
        queue.append(graph_list[node][i])
        search_order.append(graph_list[node][i])
    bfs(graph_list, visited, search_order, queue)


no_of_nodes = 9
graph = initialise_graph(no_of_nodes);
graph = add_edge(graph, 0, 1)
graph = add_edge(graph, 0, 2)
graph = add_edge(graph, 0, 3)
graph = add_edge(graph, 1, 4)
graph = add_edge(graph, 1, 5)
graph = add_edge(graph, 2, 6)
graph = add_edge(graph, 2, 7)
graph = add_edge(graph, 3, 8)

visited = []
for i in range(no_of_nodes):
    visited.append(False)

print(breadth_first_search(graph, no_of_nodes, visited))
