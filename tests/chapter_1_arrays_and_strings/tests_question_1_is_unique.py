from questions.chapter_1_arrays_and_strings.question_1_is_unique import is_unique


def test_unique_characters():
    assert is_unique("abcdefg") is True


def test_empty_string():
    assert is_unique("") is True


def test_single_character():
    assert is_unique("a") is True


def test_duplicate_characters():
    assert is_unique("hello") is False


def test_mixed_case_characters():
    assert is_unique("AbCdEfG") is True


def test_special_characters():
    assert is_unique("!@#$%^&*") is True


def test_mixed_characters():
    assert is_unique("abcdeabcde") is False


def test_whitespace():
    assert is_unique("  ") is False


def test_long_string():
    assert is_unique("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") is True
