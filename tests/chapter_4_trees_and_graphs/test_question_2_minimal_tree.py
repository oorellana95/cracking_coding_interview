from questions.chapter_4_trees_and_graphs.question_2_minimal_tree import sorted_array_to_bst


def test_sorted_array_to_bst_empty():
    arr = []
    result = sorted_array_to_bst(arr)
    assert result is None


def test_sorted_array_to_bst_single_element():
    arr = [5]
    result = sorted_array_to_bst(arr)
    assert result.value == 5
    assert result.left is None
    assert result.right is None


def test_sorted_array_to_bst_multiple_elements():
    arr = [1, 2, 3, 4, 5, 6, 7]
    result = sorted_array_to_bst(arr)

    # Assert the root node and its left and right children
    assert result.value == 4
    assert result.left.value == 2
    assert result.right.value == 6

    # Assert the left subtree
    assert result.left.left.value == 1
    assert result.left.right.value == 3

    # Assert the right subtree
    assert result.right.left.value == 5
    assert result.right.right.value == 7


