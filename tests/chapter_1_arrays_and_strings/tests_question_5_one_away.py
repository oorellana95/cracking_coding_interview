from questions.chapter_1_arrays_and_strings.question_5_one_away import one_away


def test_replace():
    assert one_away("pale", "bale") == True


def test_insert():
    assert one_away("pale", "pales") == True


def test_remove():
    assert one_away("pale", "ple") == True


def test_same_strings():
    assert one_away("hello", "hello") == True


def test_empty_strings():
    assert one_away("", "") == True


def test_empty_original_string():
    assert one_away("", "a") == True


def test_empty_one_away_string():
    assert one_away("a", "") == True


def test_more_than_one_edit():
    assert one_away("pale", "bake") == False


def test_case_sensitive():
    assert one_away("PAle", "pale") == False

