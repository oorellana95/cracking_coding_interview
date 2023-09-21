from questions.chapter_1_arrays_and_strings.question_8_zero_matrix import zero_matrix


def test_empty_matrix():
    matrix = []
    assert zero_matrix(matrix) == []


def test_no_zeros():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    assert zero_matrix(matrix) == [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]


def test_rows_and_columns_with_zeros():
    matrix = [
        [1, 0, 3],
        [4, 0, 6],
        [7, 8, 0]
    ]
    assert zero_matrix(matrix) == [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]


def test_mixed_zeros():
    matrix = [
        [1, 0, 3],
        [4, 5, 6],
        [7, 0, 9]
    ]
    assert zero_matrix(matrix) == [
        [0, 0, 0],
        [4, 0, 6],
        [0, 0, 0]
    ]
