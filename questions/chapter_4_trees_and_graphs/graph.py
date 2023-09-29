"""
TreeNode
"""
from typing import Optional


class Node:
    def __init__(self, name: str):
        self.name: str = name
        self.visited = False
        self.children: list[Node] = []


def depth_first_search(root: Node):
    """ In depth-first search (DFS), we start at the root (or another arbitrarily selected node) and explore each
    branch completely before moving on to the next branch. That is, we go deep first (hence the name depthfirst
    search) before we go wide."""

    if root:
        visit(root)
        root.visited = True
        for node in root.children:
            if not node.visited:
                depth_first_search(node)
    return None


def visit(node: Optional[Node]):
    print(node.name)
