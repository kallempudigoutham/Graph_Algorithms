from GraphInitialization import *


def get_shortest_path(start, end, graph_list, visited, prev):
    prev = bfs(start, graph_list, visited, prev)
    return reconstruct_path(start, end, prev)


def bfs(start, graph_list, visited, prev):
    queue = []
    queue = enqueue(queue, start)
    visited[start] = True
    while len(queue) != 0:
        node, queue = dequeue(queue)
        for neighbour in graph_list[node]:
            if visited[neighbour] is False:
                queue = enqueue(queue, neighbour)
                visited[neighbour] = True
                prev[neighbour] = node
    return prev


def reconstruct_path(start, end, prev):
    at = end
    path = []
    while at is not None:
        path.append(at)
        at = prev[at]

    path.reverse()
    if path[0] == start:
        return path

    return []


def enqueue(queue, element):
    queue.append(element)
    return queue;


def dequeue(queue):
    element = queue[0]
    queue.remove(element)
    return element, queue


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
prev = []
for i in range(no_of_nodes):
    visited.append(False)
    prev.append(None)

# [0, 9, 7, 11, 10, 8, 6, 3, 1, 12, 5, 2, 4]
# [None, 10, 3, 7, 3, 6, 7, 0, 9, 0, 9, 0, 8]
print(graph)
print(get_shortest_path(0, 2, graph, visited, prev))
