from tests.chapter_4_trees_and_graphs.test_binary_tree_node import BinaryTreeNode, in_order_transversal


def test_in_order_transversal():
    # Create a binary tree
    root = BinaryTreeNode("A")

    root.left = BinaryTreeNode("B")
    root.left.left = BinaryTreeNode("D")
    root.left.right = BinaryTreeNode("E")

    root.right = BinaryTreeNode("C")
    root.right.left = BinaryTreeNode("F")
    root.right.right = BinaryTreeNode("G")

    # Capture printed output to check in-order traversal
    import io
    from contextlib import redirect_stdout

    with io.StringIO() as output:
        with redirect_stdout(output):
            in_order_transversal(root)
        printed_output = output.getvalue()

    # Check if the printed output matches the expected in-order traversal
    assert printed_output.strip() == "D\nB\nE\nA\nF\nC\nG"

