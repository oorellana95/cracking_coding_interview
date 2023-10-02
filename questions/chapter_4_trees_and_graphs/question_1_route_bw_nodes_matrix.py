"""
Route Between Nodes:
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

Graphs can be either directed (like the following graph) or undirected. While directed edges are like a one-way street,
undirected edges are like a two-way street.
"""
from collections import deque


class GraphMatrix:
    def __init__(self, num_nodes):
        self.num_nodes = num_nodes
        self.adj_matrix = [[0] * num_nodes for _ in range(num_nodes)]

    def add_edge(self, from_node, to_node):
        if 0 <= from_node < self.num_nodes and 0 <= to_node < self.num_nodes:
            self.adj_matrix[from_node][to_node] = 1


def has_route_dfs(graph, start, end):
    def dfs(node):
        if node == end:
            return True
        visited.add(node)
        for neighbor in range(graph.num_nodes):
            if graph.adj_matrix[node][neighbor] == 1 and neighbor not in visited:
                if dfs(neighbor):
                    return True
        return False

    visited = set()
    return dfs(start)


def has_route_bfs(graph, start, end):
    if start == end:
        return True

    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node == end:
            return True
        visited.add(node)
        for neighbor in range(graph.num_nodes):
            if graph.adj_matrix[node][neighbor] == 1 and neighbor not in visited:
                queue.append(neighbor)

    return False


if __name__ == '__main__':
    # Example usage
    graph = GraphMatrix(5)

    # Add edges to represent the graph structure
    graph.add_edge(0, 1)
    graph.add_edge(0, 2)
    graph.add_edge(1, 3)
    graph.add_edge(1, 4)

    # Check if there is a route from node 0 to node 3
    result_dfs = has_route_dfs(graph, 0, 3)
    print(result_dfs)  # Output: True

    result_bfs = has_route_bfs(graph, 0, 3)
    print(result_bfs)  # Output: True