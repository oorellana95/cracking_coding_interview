"""
One Away: There are three types of edits that can be performed on strings: insert a character,
remove a character, or replace a character. Given two strings, write a function to check if they are
one edit (or zero edits) away.
"""


def one_away(original_str: str, one_away_str: str):
    """
    Handle the three possible cases (replace, insert, and remove) eliminating the need for multiple nested ifs.
    """
    op = len(one_away_str) - len(original_str)

    if abs(op) > 1:
        return False

    if op == 0:  # Replace
        edit_count = 0
        for c1, c2 in zip(original_str, one_away_str):
            if c1 != c2:
                edit_count += 1
                if edit_count > 1:
                    return False
        return True

    if op == 1:  # insert
        for i in range(len(original_str)):
            if original_str[i] == one_away_str[i]:
                continue
            elif original_str[i] == one_away_str[i+1]:
                continue
            return False
        return True

    if op == -1:  # remove
        for i in range(len(original_str)-1):
            if original_str[i] == one_away_str[i]:
                continue
            elif original_str[i+1] == one_away_str[i]:
                continue
            return False
        return True
