from questions.chapter_2_linked_list.linked_list import Node
from questions.chapter_2_linked_list.question_6_palindrome_linked_list import is_palindrome_linked_list


def test_palindrome_linked_list():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(1)
    assert is_palindrome_linked_list(head) is True


def test_non_palindrome_linked_list():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    assert is_palindrome_linked_list(head) is False


def test_empty_linked_list():
    head = None
    assert is_palindrome_linked_list(head) is True


def test_single_node_linked_list():
    head = Node(1)
    assert is_palindrome_linked_list(head) is True
