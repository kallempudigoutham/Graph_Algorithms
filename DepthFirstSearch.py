def depth_first_search(graph_list, no_of_nodes, visited):
    search_order = []
    for node in range(no_of_nodes):
        if visited[node] is False:
            dfs(graph_list, node, visited, search_order)
    return search_order


def dfs(graph_list, node, visited, search_order):
    visited[node] = True
    search_order.append(node)
    for i in range(len(graph_list[node])):
        if visited[graph_list[node][i]] is False:
            visited[graph_list[node][i]] = True
            dfs(graph_list, graph_list[node][i], visited, search_order)


