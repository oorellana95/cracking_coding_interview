"""
URLify:
Write a method to replace all spaces in a string with '%20'. You may assume that the string
has sufficient space at the end to hold the additional characters, and that you are given the "true"
length of the string.
"""


def urlify_inefficient(s: str):
    """
    The str.replace method creates a new string every time it's called
    """
    return s.replace(' ', '%20')


def urlify_error(s: str):
    """
    TypeError: 'str' object does not support item assignment
    """
    try:
        for i in range(len(s)):
            if s[i] == ' ':
                s[i] = '%20'
    except TypeError:
        raise


def urlify(s: str):
    """
    Iteration through the string and build the URL-encoded string character by character
    """
    url_encoded = []
    for c in s:
        if c == ' ':
            url_encoded.append('%20')
        else:
            url_encoded.append(c)
    return ''.join(url_encoded)
