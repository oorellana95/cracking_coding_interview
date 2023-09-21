"""
Return Kth to Last:
Implement an algorithm to find the kth to last element of a singly linked list.
"""
from questions.chapter_2_linked_list.linked_list import LinkedList


def kth_to_last_(linked_list: LinkedList, k: int):
    node = linked_list.root
    if node is None or k < 0:
        return []

    counter = 0
    while node is not None:
        if counter == k:
            return node.to_list()
        counter += 1
        node = node.next
    return []


def kth_to_last(linked_list: LinkedList, k: int):
    if k < 0:
        return []

    node = linked_list.root
    for _ in range(k):
        if node is None:
            return []
        node = node.next

    return node.to_list() if node is not None else []