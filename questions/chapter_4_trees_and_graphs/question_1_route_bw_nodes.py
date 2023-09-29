"""
Route Between Nodes:
Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

Graphs can be either directed (like the following graph) or undirected. While directed edges are like a one-way street,
undirected edges are like a two-way street.
"""
from collections import deque
from questions.chapter_4_trees_and_graphs.graph import Node


# DFS
def has_route_dfs(start: Node, end: Node) -> bool:
    def dfs(node: Node, visited: set) -> bool:
        if node == end:
            return True
        visited.add(node)
        for neighbor in node.children:
            if neighbor not in visited:
                if dfs(neighbor, visited):
                    return True
        return False

    visited_nodes = set()
    return dfs(start, visited_nodes)


# BFS
def has_route_bfs(start: Node, end: Node) -> bool:
    if start == end:
        return True

    visited = set()
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node == end:
            return True
        visited.add(node)
        for neighbor in node.children:
            if neighbor not in visited:
                queue.append(neighbor)

    return False
