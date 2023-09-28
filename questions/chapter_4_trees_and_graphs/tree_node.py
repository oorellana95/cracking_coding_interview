"""
TreeNode
"""
from typing import Optional


class TreeNode:
    def __init__(self, value: str):
        self.value: str = value
        self.children: Optional[TreeNode] = None
