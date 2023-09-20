"""
Check Permutation:
Given two strings, write a method to decide if one is a permutation of the other
"""


def is_permutation_inefficient(s1: str, s2: str):
    if len(s1) != len(s2):
        return False

    dictionary1, dictionary2 = {}, {}
    for i in range(len(s1)):
        dictionary1[s1[i]] = dictionary1.get(s1[i], 0) + 1
        dictionary2[s2[i]] = dictionary2.get(s2[i], 0) + 1

    return True if dictionary1 == dictionary2 else False


def is_permutation(s1: str, s2: str):
    """
    This reduces code duplication.
    This eliminates the need for creating two separate dictionaries.
    The code is more concise and easier to understand
    """
    if len(s1) != len(s2):
        return False

    char_count = {}

    for c in s1:
        char_count[c] = char_count.get(c, 0) + 1

    for c in s2:
        if c not in char_count:
            return False
        char_count[c] -= 1
        if char_count[c] < 0:
            return False
    return True

