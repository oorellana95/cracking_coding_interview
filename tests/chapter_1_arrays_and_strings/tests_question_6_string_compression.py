from questions.chapter_1_arrays_and_strings.question_6_string_compression import string_compression


def test_empty_string():
    assert string_compression("") == ""


def test_no_compression_needed():
    assert string_compression("abcdefg") == "a1b1c1d1e1f1g1"


def test_basic_compression():
    assert string_compression("aabcccccaaa") == "a2b1c5a3"


def test_uppercase_and_lowercase():
    assert string_compression("AAbBBccCCccDDd") == "A2b1B2c2C2c2D2d1"


def test_single_character():
    assert string_compression("a") == "a1"


def test_multiple_characters():
    assert string_compression("aa") == "a2"


def test_special_characters():
    assert string_compression("$$%##") == "$2%1#2"


def test_long_compression():
    assert string_compression("aaabbbbbbbcccdefghhh") == "a3b7c3d1e1f1g1h3"

