"""
Minimal Tree:
Given a sorted (increasing order) array with unique integer elements, write an algorithm
to create a binary search tree with minimal height.
"""
from questions.chapter_4_trees_and_graphs.binary_tree_node import BinaryTreeNode


def sorted_array_to_bst(arr):
    if not arr:
        return None

    mid = (len(arr)) // 2
    root = BinaryTreeNode(arr[mid])
    root.left = sorted_array_to_bst(arr[:mid])
    root.right = sorted_array_to_bst(arr[mid + 1:])

    return root


def pre_order(node):
    if not node:
        return

    print(node.value),
    pre_order(node.left)
    pre_order(node.right)
