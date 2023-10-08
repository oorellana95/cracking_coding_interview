import pytest

from questions.chapter_4_trees_and_graphs.binary_tree_node import BinaryTreeNode
from questions.chapter_4_trees_and_graphs.question_5_binary_search_tree import is_valid_bst


@pytest.fixture
def valid_bst():
    root = BinaryTreeNode(2)
    root.left = BinaryTreeNode(1)
    root.right = BinaryTreeNode(3)
    return root


@pytest.fixture
def invalid_bst():
    root = BinaryTreeNode(1)
    root.left = BinaryTreeNode(2)
    root.right = BinaryTreeNode(3)
    return root


@pytest.fixture
def empty_tree():
    return None


def test_valid_bst(valid_bst):
    assert is_valid_bst(valid_bst) is True


def test_invalid_bst(invalid_bst):
    assert is_valid_bst(invalid_bst) is False


def test_empty_tree(empty_tree):
    assert is_valid_bst(empty_tree) is True


def test_single_node_tree():
    root = BinaryTreeNode(42)
    assert is_valid_bst(root) is True


def test_large_valid_bst():
    root = BinaryTreeNode(10)
    root.left = BinaryTreeNode(5)
    root.right = BinaryTreeNode(15)
    root.left.left = BinaryTreeNode(3)
    root.left.right = BinaryTreeNode(7)
    root.right.left = BinaryTreeNode(12)
    root.right.right = BinaryTreeNode(20)
    assert is_valid_bst(root) is True


def test_large_invalid_bst():
    root = BinaryTreeNode(10)
    root.left = BinaryTreeNode(5)
    root.right = BinaryTreeNode(15)
    root.left.left = BinaryTreeNode(3)
    root.left.right = BinaryTreeNode(12)  # Violates the BST property
    root.right.left = BinaryTreeNode(11)  # Violates the BST property
    root.right.right = BinaryTreeNode(20)
    assert is_valid_bst(root) is False
