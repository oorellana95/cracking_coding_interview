from questions.chapter_1_arrays_and_strings.question_3_urlify import urlify


def test_empty_string():
    assert urlify("") == ""


def test_no_spaces():
    assert urlify("abc") == "abc"


def test_single_space():
    assert urlify("a b") == "a%20b"


def test_multiple_spaces():
    assert urlify("a b c") == "a%20b%20c"


def test_spaces_at_start_and_end():
    assert urlify("  hello world  ") == "%20%20hello%20world%20%20"


def test_special_characters():
    assert urlify("a b!c") == "a%20b!c"


def test_spaces_and_special_characters():
    assert urlify("a$ b c@") == "a$%20b%20c@"
