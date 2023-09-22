"""
Partition:
Write code to partition a linked list around a value x, such that all nodes less than x come
before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
to be after the elements less than x (see below). The partition element x can appear anywhere in the
"right partition"; it does not need to appear between the left and right partitions.

EXAMPLE
Input:
3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1 [partition= 5]
Output:
3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
"""
from questions.chapter_2_linked_list.linked_list import LinkedList, Node


def partition_linked_list_non_optimal(node: Node, partition: int):
    array_left = []
    array_right = []
    while node is not None:
        if node.data < partition:
            array_left.append(node.data)
        else:
            array_right.append(node.data)
        node = node.next
    return LinkedList().list_to_nodes(array_left + array_right)


def partition_linked_list(head: Node, partition: int):
    # Create two dummy nodes, 'left' and 'right', to serve as the heads of the left and right partitions.
    left, right = Node(), Node()

    # Create 'ltail' and 'rtail' pointers to keep track of the tail nodes in the left and right partitions.
    ltail, rtail = left, right

    # Iterate through the original linked list.
    while head:
        # If the current node's data is less than the partition value, move it to the left partition.
        if head.data < partition:
            ltail.next = head  # Connect the current node to the 'left' partition.
            ltail = ltail.next  # Update 'ltail' to the current node.

        # If the current node's data is greater than or equal to the partition value, move it to the right partition.
        else:
            rtail.next = head  # Connect the current node to the 'right' partition.
            rtail = rtail.next  # Update 'rtail' to the current node.

        # Move to the next node in the original linked list.
        head = head.next

    # Connect the tail of the left partition to the head of the right partition.
    ltail.next = right.next

    # Set the tail of the right partition to None to terminate the list.
    rtail.next = None

    # Return the head of the combined partitioned linked list (left + right).
    return left.next
