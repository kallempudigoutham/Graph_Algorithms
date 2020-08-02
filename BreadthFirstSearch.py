from GraphInitialization import *


def breadth_first_search(graph_list, no_of_nodes, visited):
    search_order = []
    queue = []
    for node in range(no_of_nodes):
        if visited[node] is False:
            queue.append(node)
            visited[node] = True
            search_order.append(node)
            bfs(graph_list, visited, search_order, queue)
    return search_order


def bfs(graph_list, visited, search_order, queue):
    if len(queue) == 0:
        return
    node = queue[0]
    queue.remove(node)
    for i in range(len(graph_list[node])):
        if visited[graph_list[node][i]] is False:
            queue.append(graph_list[node][i])
            visited[graph_list[node][i]] = True
            search_order.append(graph_list[node][i])
    bfs(graph_list, visited, search_order, queue)


no_of_nodes = 13
graph = initialise_graph(no_of_nodes);
graph = add_edge(graph, 0, 9)
graph = add_edge(graph, 0, 7)
graph = add_edge(graph, 0, 11)
graph = add_edge(graph, 3, 2)
graph = add_edge(graph, 3, 4)
graph = add_edge(graph, 6, 5)
graph = add_edge(graph, 7, 6)
graph = add_edge(graph, 7, 3)
graph = add_edge(graph, 7, 11)
graph = add_edge(graph, 8, 1)
graph = add_edge(graph, 8, 12)
graph = add_edge(graph, 9, 10)
graph = add_edge(graph, 9, 8)
graph = add_edge(graph, 10, 1)
graph = add_edge(graph, 12, 2)

visited = []
for i in range(no_of_nodes):
    visited.append(False)

print(breadth_first_search(graph, no_of_nodes, visited))
