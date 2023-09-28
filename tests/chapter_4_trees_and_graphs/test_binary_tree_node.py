"""
TreeNode
"""
from typing import Optional


class BinaryTreeNode:
    def __init__(self, value: str):
        self.value: str = value
        self.left: Optional[BinaryTreeNode] = None
        self.right: Optional[BinaryTreeNode] = None


def in_order_transversal(node: Optional[BinaryTreeNode]):
    if node is not None:
        in_order_transversal(node.left)
        visit(node)
        in_order_transversal(node.right)


def visit(node: Optional[BinaryTreeNode]):
    print(node.value)
