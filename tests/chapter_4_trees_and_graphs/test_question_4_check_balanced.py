import pytest

from questions.chapter_4_trees_and_graphs.binary_tree_node import BinaryTreeNode
from questions.chapter_4_trees_and_graphs.question_4_check_balanced import is_balanced


@pytest.fixture
def balanced_tree():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    root.left.left = BinaryTreeNode(4)
    root.left.right = BinaryTreeNode(5)
    root.right.left = BinaryTreeNode(6)
    root.right.right = BinaryTreeNode(7)
    return root


@pytest.fixture
def unbalanced_tree():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.left.left = BinaryTreeNode(3)
    root.left.left.left = BinaryTreeNode(4)
    return root


def test_balanced_tree(balanced_tree):
    assert is_balanced(balanced_tree) is True


def test_unbalanced_tree(unbalanced_tree):
    assert is_balanced(unbalanced_tree) is False


def test_empty_tree():
    assert is_balanced(None) is True


def test_single_node_tree():
    root = BinaryTreeNode(1)
    assert is_balanced(root) is True

