from questions.chapter_4_trees_and_graphs.tree_node import TreeNode


def test_tree_node_creation():
    node = TreeNode("A")
    assert node.value == "A"
    assert node.children is None


def test_tree_node_children():
    node = TreeNode("A")
    child1 = TreeNode("B")
    child2 = TreeNode("C")

    node.children = [child1, child2]

    assert node.children == [child1, child2]

