"""
Palindrome:
Implement a function to check if a linked list is a palindrome.
"""


def is_palindrome_linked_list(head):
    values = []
    while head:
        values.append(head.data)
        head = head.next

    length = len(values)
    for i in range(length // 2):
        if values[i] != values[length - 1 - i]:
            return False
    return True
