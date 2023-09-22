"""
Sum Lists:
You have two numbers represented by a linked list, where each node contains a single
digit. The digits are stored in reverse order, such that the 1 's digit is at the head of the list. Write a
function that adds the two numbers and returns the sum as a linked list.

EXAMPLE
Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295.
Output: 2 -> 1 -> 9. That is, 912.

Suppose the digits are stored in forward order. Repeat the above problem.
EXAMPLE
lnput:(6 -> 1 -> 7) + (2 -> 9 -> 5).That is,617 + 295.
Output: 9 - > 1 -> 2. That is, 912.
"""
from questions.chapter_2_linked_list.linked_list import Node


def sum_linked_lists_same_length(node1, node2):
    rnode = Node()
    rnode_tail = rnode
    tens = 0
    while node1:
        result = node1.data + node2.data + tens
        tens = result // 10
        ones = result % 10

        rnode_tail.next = Node(data=ones)
        rnode_tail = rnode_tail.next
        node1 = node1.next
        node2 = node2.next

    if tens > 0:
        rnode_tail.next = Node(data=tens)

    return rnode.next
