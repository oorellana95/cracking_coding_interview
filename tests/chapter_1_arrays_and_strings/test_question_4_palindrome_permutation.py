from questions.chapter_1_arrays_and_strings.question_4_palindrome_permutation import is_palindrome_permutation

def test_empty_string():
    assert is_palindrome_permutation("") == True


def test_single_character():
    assert is_palindrome_permutation("a") == True


def test_palindrome_permutation_with_spaces():
    assert is_palindrome_permutation("taco cat") == False


def test_palindrome_permutation_odd_length():
    assert is_palindrome_permutation("racecar") == True


def test_not_palindrome_permutation_even_length():
    assert is_palindrome_permutation("hello world") == False


def test_not_palindrome_permutation_odd_length():
    assert is_palindrome_permutation("coding") == False


def test_mixed_case():
    assert is_palindrome_permutation("A man, a plan, a canal, Panama") == False


def test_special_characters():
    assert is_palindrome_permutation("12$%$21") == True
