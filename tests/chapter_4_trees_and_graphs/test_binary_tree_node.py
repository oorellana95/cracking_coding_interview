import pytest

from questions.chapter_4_trees_and_graphs.binary_tree_node import BinaryTreeNode, in_order_transversal, \
    pre_order_transversal, post_order_transversal


@pytest.fixture
def sample_tree():
    root = BinaryTreeNode("A")

    root.left = BinaryTreeNode("B")
    root.left.left = BinaryTreeNode("D")
    root.left.right = BinaryTreeNode("E")

    root.right = BinaryTreeNode("C")
    root.right.left = BinaryTreeNode("F")
    root.right.right = BinaryTreeNode("G")

    return root


# Test cases for traversal functions
@pytest.mark.parametrize("traversal_func, expected_output", [
    (in_order_transversal, "D\nB\nE\nA\nF\nC\nG"),
    (pre_order_transversal, "A\nB\nD\nE\nC\nF\nG"),
    (post_order_transversal, "D\nE\nB\nF\nG\nC\nA"),
])
def test_tree_traversal(traversal_func, expected_output, sample_tree):
    import io
    from contextlib import redirect_stdout

    with io.StringIO() as output:
        with redirect_stdout(output):
            traversal_func(sample_tree)
        printed_output = output.getvalue()

    assert printed_output.strip() == expected_output


if __name__ == "__main__":
    pytest.main()
