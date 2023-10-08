import pytest

from questions.chapter_4_trees_and_graphs.question_6_in_order_successor_bst import TreeNode, find_inorder_successor


@pytest.fixture
def sample_bst():
    root = TreeNode(10)
    root.left = TreeNode(5, parent=root)
    root.right = TreeNode(15, parent=root)
    root.left.left = TreeNode(3, parent=root.left)
    root.left.right = TreeNode(7, parent=root.left)
    root.right.left = TreeNode(12, parent=root.right)
    root.right.right = TreeNode(20, parent=root.right)
    return root


def test_successor_with_right_child(sample_bst):
    node = sample_bst.left  # Node with value 5
    successor = find_inorder_successor(node)
    assert successor.val == 7


def test_successor_without_right_child(sample_bst):
    node = sample_bst.left.left  # Node with value 3
    successor = find_inorder_successor(node)
    assert successor.val == 5


def test_successor_of_last_node(sample_bst):
    node = sample_bst.right.right  # Node with value 20
    successor = find_inorder_successor(node)
    assert successor is None  # No successor, should be None


def test_successor_of_root_node(sample_bst):
    node = sample_bst  # Root node with value 10
    successor = find_inorder_successor(node)
    assert successor.val == 12


def test_successor_with_no_parent_pointers():
    node = TreeNode(5)  # Single node with value 5
    successor = find_inorder_successor(node)
    assert successor is None  # No successor, should be None


def test_successor_with_single_left_child():
    root = TreeNode(5)
    root.left = TreeNode(3, parent=root)
    successor = find_inorder_successor(root)
    assert successor is None


def test_successor_with_single_right_child():
    root = TreeNode(5)
    root.right = TreeNode(6, parent=root)
    successor = find_inorder_successor(root)
    assert successor.val is 6


def test_successor_with_multiple_ancestors():
    root = TreeNode(10)
    root.left = TreeNode(5, parent=root)
    root.left.left = TreeNode(3, parent=root.left)
    root.left.right = TreeNode(7, parent=root.left)
    root.right = TreeNode(15, parent=root)
    root.right.left = TreeNode(12, parent=root.right)
    root.right.right = TreeNode(20, parent=root.right)
    node = root.left.right  # Node with value 7
    successor = find_inorder_successor(node)
    assert successor.val == 10

