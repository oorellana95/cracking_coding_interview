"""
First Common Ancestor: Design an algorithm and write code to find the first common ancestor
of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not
necessarily a binary search tree.
"""


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def find_common_ancestor(root, node1, node2):
    if root is None:
        return None

    # If either of the nodes is the root, the root itself is the common ancestor
    if root == node1 or root == node2:
        return root

    # Recursively search for the nodes in the left and right subtrees
    left_ancestor = find_common_ancestor(root.left, node1, node2)
    right_ancestor = find_common_ancestor(root.right, node1, node2)

    # If both nodes are found in different subtrees, then the current root is the common ancestor
    if left_ancestor and right_ancestor:
        return root

    # Otherwise, return the non-None ancestor (if found)
    return left_ancestor if left_ancestor else right_ancestor
