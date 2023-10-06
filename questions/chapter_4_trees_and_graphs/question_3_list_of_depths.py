"""
List of Depths:
Given a binary tree, design an algorithm which creates a linked list of all the nodes
at each depth (e.g., if you have a tree with depth D, you'll have D linked lists).
"""
from typing import Optional

from questions.chapter_2_linked_list.linked_list import LinkedList
from questions.chapter_4_trees_and_graphs.binary_tree_node import BinaryTreeNode


def list_of_depths(node: Optional[BinaryTreeNode], dictionary=None, depth=0):
    if dictionary is None:
        dictionary = {}

    if node is not None:
        dictionary[depth] = dictionary.get(depth, LinkedList())
        dictionary[depth].append(node.value)
        list_of_depths(node.left, dictionary, depth+1)
        list_of_depths(node.right, dictionary, depth+1)

    return dictionary
