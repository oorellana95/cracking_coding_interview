import pytest

from questions.chapter_2_linked_list.linked_list import LinkedList
from questions.chapter_4_trees_and_graphs.binary_tree_node import BinaryTreeNode
from questions.chapter_4_trees_and_graphs.question_3_list_of_depths import list_of_depths


@pytest.fixture
def sample_binary_tree():
    # Create a sample binary tree
    root = BinaryTreeNode("A")
    root.left = BinaryTreeNode("B")
    root.right = BinaryTreeNode("C")
    root.left.left = BinaryTreeNode("D")
    root.left.right = BinaryTreeNode("E")
    root.right.left = BinaryTreeNode("F")
    root.right.right = BinaryTreeNode("G")
    return root


def test_list_of_depths_empty_tree():
    root = None
    result = list_of_depths(root)
    assert result == {}


def test_list_of_depths_single_node():
    root = BinaryTreeNode("A")
    result = list_of_depths(root)
    expected = {0: LinkedList().list_to_nodes(["A"])}
    assert str(result) == str(expected)


def test_list_of_depths_sample_tree(sample_binary_tree):
    result = list_of_depths(sample_binary_tree)
    expected = {
        0: LinkedList().list_to_nodes(["A"]),
        1: LinkedList().list_to_nodes(["B", "C"]),
        2: LinkedList().list_to_nodes(["D", "E", "F", "G"])
    }
    assert str(result) == str(expected)

# You can add more test cases as needed
