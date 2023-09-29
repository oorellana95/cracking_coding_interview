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


def pre_order_transversal(node: Optional[BinaryTreeNode]):
    if node is not None:
        visit(node)
        pre_order_transversal(node.left)
        pre_order_transversal(node.right)


def post_order_transversal(node: Optional[BinaryTreeNode]):
    if node is not None:
        post_order_transversal(node.left)
        post_order_transversal(node.right)
        visit(node)


def visit(node: Optional[BinaryTreeNode]):
    print(node.value)
