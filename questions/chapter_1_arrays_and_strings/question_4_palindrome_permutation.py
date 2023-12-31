"""
Pindrome Permutation:
Given a string, write a function to check if it is a permutation of a palindrome.
A palindrome is a word or phrase that is the same forwards and backwards. A permutation
is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.
"""


def is_palindrome_permutation(s: str):
    # Create an empty dictionary to store character counts
    char_binary_count = {}

    # Iterate through each character in the input string
    for char in s:
        # Toggle the character count between 1 (odd) and 0 (even)
        char_binary_count[char] = 1 if char_binary_count.get(char, 0) == 0 else 0

    # Calculate the total count of characters with a value of 1
    odd_count = sum(char_binary_count.values())

    # Return True if there is at most one character with a count of 1 (a palindrome permutation), otherwise False
    return True if odd_count <= 1 else False


def is_palindrome_permutation_2(s: str):
    char_count = {}
    for c in s:
        char_count[c] = char_count.get(c, 0) + 1

    # A palindrome permutation can have at most one character with an odd count
    odd_count = sum(1 for count in char_count.values() if count % 2 == 1)
    return odd_count <= 1
