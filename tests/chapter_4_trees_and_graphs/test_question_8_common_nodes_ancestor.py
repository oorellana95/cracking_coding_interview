import pytest

from questions.chapter_4_trees_and_graphs.question_8_common_nodes_ancestor import TreeNode, find_common_ancestor


@pytest.fixture
def sample_binary_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    return root


def test_common_ancestor_for_leaves(sample_binary_tree):
    node1 = sample_binary_tree.left.left  # Node with value 4
    node2 = sample_binary_tree.left.right  # Node with value 5
    common_ancestor = find_common_ancestor(sample_binary_tree, node1, node2)
    assert common_ancestor.val == 2


def test_common_ancestor_for_one_leaf_and_root(sample_binary_tree):
    node1 = sample_binary_tree.left.left  # Node with value 4
    node2 = sample_binary_tree  # Root node with value 1
    common_ancestor = find_common_ancestor(sample_binary_tree, node1, node2)
    assert common_ancestor.val == 1


def test_common_ancestor_for_two_leaf_nodes(sample_binary_tree):
    node1 = sample_binary_tree.left.left  # Node with value 4
    node2 = sample_binary_tree.right.right  # Node with value 7
    common_ancestor = find_common_ancestor(sample_binary_tree, node1, node2)
    assert common_ancestor.val == 1


def test_common_ancestor_for_nonexistent_nodes(sample_binary_tree):  # TODO Fix Test
    node1 = TreeNode(8)  # Node with value 8 (not in the tree)
    node2 = sample_binary_tree.left.right  # Node with value 5
    common_ancestor = find_common_ancestor(sample_binary_tree, node1, node2)
    assert common_ancestor is None  # No common ancestor, should be None


def test_common_ancestor_for_both_nonexistent_nodes(sample_binary_tree):
    node1 = TreeNode(8)  # Node with value 8 (not in the tree)
    node2 = TreeNode(9)  # Node with value 9 (not in the tree)
    common_ancestor = find_common_ancestor(sample_binary_tree, node1, node2)
    assert common_ancestor is None  # No common ancestor, should be None
