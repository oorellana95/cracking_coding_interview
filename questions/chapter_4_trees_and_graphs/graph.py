"""
Graph
"""
from typing import Optional
from collections import deque


class Node:
    def __init__(self, name: str):
        self.name: str = name
        self.marked = False
        self.children: list[Node] = []


def depth_first_search(root: Node):
    """ In depth-first search (DFS), we start at the root (or another arbitrarily selected node) and explore each
    branch completely before moving on to the next branch. That is, we go deep first (hence the name depthfirst
    search) before we go wide."""

    if root:
        visit(root)
        root.marked = True
        for node in root.children:
            if not node.marked:
                depth_first_search(node)
    return None


def breadth_first_search(root: Node):
    """ In breadth-first search (BFS), we start at the root (or another arbitrarily selected node) and explore each
    neighbor before going on to any of their children. That is, we go wide (hence breadth-first search) before
    we go deep."""
    queue = deque()
    root.marked = True
    queue.append(root)

    while queue:
        node = queue.pop()
        visit(node)
        for n in node.children:
            if n.marked is False:
                n.marked = True
                queue.append(n)


def visit(node: Optional[Node]):
    print(node.name)
