"""

To find the in-order successor of a given node in a binary search tree (BST) when each node has a link to its parent,
you can follow these steps:

1. If the node has a right child, then the in-order successor will be the leftmost node in the right subtree. You can
find it by traversing down the right subtree and then moving left as far as possible.

2. If the node does not have a right child, you will need to go up the tree to find the first ancestor for which the
given node is in the left subtree. The in-order successor will be that ancestor.

Video: https://www.youtube.com/watch?v=5cPbNCrdotA
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None, parent=None):
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent


def find_inorder_successor(node):
    # 1. If the node has a right child, find the leftmost node in the right subtree
    if node.right:
        return find_leftmost_node(node.right)

    # 2. If the node does not have a right child, find the first ancestor for which the node is in the left subtree
    return find_ancestor_node_left_subtree(node)


def find_leftmost_node(node):
    while node.left:
        node = node.left
    return node


def find_ancestor_node_left_subtree(node):
    while node.parent and node.parent.right == node:
        node = node.parent
    return node.parent
