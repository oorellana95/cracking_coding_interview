from questions.chapter_1_arrays_and_strings.question_2_check_permutation import is_permutation


def test_empty_strings():
    assert is_permutation("", "") is True


def test_permutation():
    assert is_permutation("listen", "silent") is True


def test_not_permutation_different_length():
    assert is_permutation("abc", "abcd") is False


def test_not_permutation_different_characters():
    assert is_permutation("hello", "world") is False


def test_permutation_same_characters():
    assert is_permutation("aabbc", "abcab") is True


def test_permutation_case_sensitive():
    assert is_permutation("RaceCar", "racecar") is False


def test_permutation_special_characters():
    assert is_permutation("123$%^", "%^$321") is True


def test_not_permutation_special_characters():
    assert is_permutation("!@#", "#$%") is False
