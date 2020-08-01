def no_connected_components(graph_list, no_of_nodes, visited):
    search_order = []
    count = 0
    for node in range(no_of_nodes):
        if visited[node] is False:
            count = count + 1
            dfs(graph_list, node, visited, search_order)
    return count, search_order


def dfs(graph_list, node, visited, search_order):
    visited[node] = True
    search_order.append(node)
    for i in range(len(graph_list[node])):
        if visited[graph_list[node][i]] is False:
            visited[graph_list[node][i]] = True
            dfs(graph_list, graph_list[node][i], visited, search_order)

