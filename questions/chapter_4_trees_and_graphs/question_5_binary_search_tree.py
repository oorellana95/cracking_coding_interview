"""
Validate BST:
Implement a function to check if a binary tree is a binary search tree.
"""

from questions.chapter_4_trees_and_graphs.binary_tree_node import BinaryTreeNode


def is_valid_bst(root):
    def is_valid_bst_helper(node: BinaryTreeNode, lower=float('-inf'), upper=float('inf')):
        if node is None:
            return True

        if node.value <= lower or node.value >= upper:
            return False

        return (is_valid_bst_helper(node.left, lower, node.value) and
                is_valid_bst_helper(node.right, node.value, upper))

    return is_valid_bst_helper(root)
