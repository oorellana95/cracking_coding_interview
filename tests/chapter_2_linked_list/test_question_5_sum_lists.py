from questions.chapter_2_linked_list.linked_list import Node
from questions.chapter_2_linked_list.question_5_sum_lists import sum_linked_lists_same_length


def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.data)
        node = node.next
    return result


def test_sum_linked_lists_same_length():
    node1 = Node(2)
    node1.next = Node(4)
    node1.next.next = Node(3)

    node2 = Node(5)
    node2.next = Node(5)
    node2.next.next = Node(6)

    result = sum_linked_lists_same_length(node1, node2)

    result_list = linked_list_to_list(result)

    assert result_list == [7, 9, 9]


def test_sum_linked_lists_same_length_with_carry():
    node1 = Node(9)
    node1.next = Node(9)
    node1.next.next = Node(9)

    node2 = Node(1)
    node2.next = Node(0)
    node2.next.next = Node(0)

    result = sum_linked_lists_same_length(node1, node2)

    result_list = linked_list_to_list(result)

    assert result_list == [0, 0, 0, 1]


def test_sum_linked_lists_same_length_empty_lists():
    node1 = None
    node2 = None

    result = sum_linked_lists_same_length(node1, node2)

    result_list = linked_list_to_list(result)

    assert result_list == []
