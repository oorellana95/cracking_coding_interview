from questions.chapter_2_linked_list.linked_list import Node
from questions.chapter_2_linked_list.question_7_intersection import is_intersection


def test_intersection():
    list1 = Node(1)
    list1.next = Node(3)
    list1.next.next = Node(5)
    intersection_node = Node(7)
    intersection_node.next = Node(9)
    list1.next.next.next = intersection_node

    list2 = Node(2)
    list2.next = Node(4)
    list2.next.next = Node(6)
    list2.next.next.next = intersection_node

    assert is_intersection(list1, list2) == 7


def test_no_intersection():
    list1 = Node(1)
    list1.next = Node(2)
    list1.next.next = Node(3)

    list2 = Node(4)
    list2.next = Node(5)
    list2.next.next = Node(6)

    assert is_intersection(list1, list2) is None


def test_intersection_at_the_second_position():
    list1 = Node(1)
    intersection_node = Node(2)
    list1.next = intersection_node
    list1.next.next = Node(3)

    list2 = Node(8)
    list2.next = intersection_node

    assert is_intersection(list1, list2) == 2


def test_empty_lists():
    list1 = None
    list2 = None

    assert is_intersection(list1, list2) is None

