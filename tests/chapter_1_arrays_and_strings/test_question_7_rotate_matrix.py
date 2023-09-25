from questions.chapter_1_arrays_and_strings.question_7_rotate_matrix import rotate_matrix


def test_empty_matrix():
    assert rotate_matrix([]) == []


def test_1x1_matrix():
    assert rotate_matrix([[1]]) == [[1]]


def test_2x2_matrix():
    input_matrix = [
        [1, 2],
        [3, 4]
    ]
    expected_matrix = [
        [3, 1],
        [4, 2]
    ]
    assert rotate_matrix(input_matrix) == expected_matrix


def test_3x3_matrix():
    input_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    expected_matrix = [
        [7, 4, 1],
        [8, 5, 2],
        [9, 6, 3]
    ]
    assert rotate_matrix(input_matrix) == expected_matrix


def test_4x4_matrix():
    input_matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    expected_matrix = [
        [13, 9, 5, 1],
        [14, 10, 6, 2],
        [15, 11, 7, 3],
        [16, 12, 8, 4]
    ]
    assert rotate_matrix(input_matrix) == expected_matrix
