from questions.chapter_4_trees_and_graphs.question_2_minimal_tree import sorted_array_to_bst, pre_order

if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7]
    root = sorted_array_to_bst(arr)
    pre_order(root)
