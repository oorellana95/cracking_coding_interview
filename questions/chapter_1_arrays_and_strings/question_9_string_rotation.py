"""
String Rotation:
Assume you have a method isSubstringwhich checks if one word is a substring
of another. Given two strings, sl and s2, write code to check if s2 is a rotation of sl using only one
call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").
"""


def is_substring(s1, s2):
    # waterbottlewaterbottle
    #    erbottlewat
    return s2 in s1 + s1
