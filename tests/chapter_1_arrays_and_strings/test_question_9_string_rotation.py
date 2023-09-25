from questions.chapter_1_arrays_and_strings.question_9_string_rotation import is_substring


def test_empty_string():
    assert is_substring("", "substring") == False


def test_substring_at_beginning():
    assert is_substring("substring", "sub") == True


def test_substring_in_middle():
    assert is_substring("substring", "str") == True


def test_substring_at_end():
    assert is_substring("substring", "ring") == True


def test_not_substring():
    assert is_substring("substring", "not") == False


# Test cases for checking rotation
def test_rotation_empty_strings():
    assert is_substring("", "") == True


def test_rotation_same_string():
    assert is_substring("abc", "abc") == True


def test_rotation_true():
    assert is_substring("waterbottle", "erbottlewat") == True


def test_rotation_false():
    assert is_substring("abcdef", "abcxyz") == False
