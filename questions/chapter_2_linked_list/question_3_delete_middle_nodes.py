"""
Delete Middle Node:
Implement an algorithm to delete a node in the middle (i.e., any node but the first and last node,
not necessarily the exact middle) of a singly linked list, given only access to that node.
"""
from questions.chapter_2_linked_list.linked_list import LinkedList


def delete_specific_node_by_index(linked_list: LinkedList, index: int):
    node = linked_list.root
    if index == 0:
        return node.next

    current_index = 1
    while node.next is not None:
        if current_index == index:
            node.next = node.next.next
            return linked_list
        node = node.next
        current_index += 1
    return linked_list


def delete_specific_nodes_by_data(linked_list: LinkedList, data: int):
    node = linked_list.root
    if node.data == data:
        return node.next

    while node.next is not None:
        if node.next.data == data:
            node.next = node.next.next
        node = node.next
    return linked_list


