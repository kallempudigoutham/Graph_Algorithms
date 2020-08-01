# Graph creation using Adjacent list
# Traversing takes O(n + V) n is number of nodes and V is vertices


def initialise_graph(no_of_nodes):
    graph_list = []
    for i in range(no_of_nodes):
        graph_list.append(set())
    return graph_list


def add_edge(graph_list, start, end):
    graph_list[start].add(end)
    return graph_list


def remove_edge(graph_list, start, end):
    if end in graph_list[start]:
        graph_list[start].discard(end)
    return graph_list
