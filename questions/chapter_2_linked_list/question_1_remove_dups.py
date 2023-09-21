"""
Remove Dups!
Write code to remove duplicates from an unsorted linked list.
How would you solve this problem if a temporary buffer is not allowed?
"""
from questions.chapter_2_linked_list.linked_list import LinkedList


def remove_duplicates(linked_list: LinkedList):
    if linked_list.root.data is None:
        return []

    node = linked_list.root
    duplicates = {node.data}

    while node.next is not None:
        if node.next.data in duplicates:
            node.next = node.next.next
        else:
            duplicates.add(node.next.data)
            node = node.next

    return linked_list
