"""
Check Balanced:
Implement a function to check if a binary tree is balanced. For the purposes of
this question, a balanced tree is defined to be a tree such that the heights of the two subtrees of any
node never differ by more than one.
"""
from typing import Optional

from questions.chapter_4_trees_and_graphs.binary_tree_node import BinaryTreeNode


def is_balanced(node: Optional[BinaryTreeNode], register=None, depth=0):
    if register is None:
        register = {'min': float('+inf'), 'max': float('-inf')}  # It can be done using a tuple too

    if node is not None:
        is_balanced(node.left, register, depth+1)
        is_balanced(node.right, register, depth+1)
    else:
        if depth < register.get('min'):
            register['min'] = depth
        elif depth > register.get('max'):
            register['max'] = depth

    return register.get('max') - register.get('min') < 2
