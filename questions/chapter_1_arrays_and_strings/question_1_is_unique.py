"""
Is Unique:
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?
"""


def is_unique(s: str):
    dictionary = {}
    for c in s:
        dictionary[c] = dictionary.get(c, 0) + 1
        if dictionary[c] > 1:
            return False
    return True
