"""
Intersection:
Given two (singly) linked lists, determine if the two lists intersect. Return the intersecting
node. Note that the intersection is defined based on reference, not value. That is, if the kth
node of the first linked list is the exact same node (by reference) as the jth node of the second
linked list, then they are intersecting.
"""


def is_intersection(f_head, s_head):
    values = {}

    while f_head:
        values[id(f_head)] = f_head.data
        f_head = f_head.next

    while s_head:
        data = values.get(id(s_head))
        if data:
            return data
        s_head = s_head.next
    return None
