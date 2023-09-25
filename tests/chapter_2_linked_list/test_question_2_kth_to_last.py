from questions.chapter_2_linked_list.linked_list import LinkedList
from questions.chapter_2_linked_list.question_2_kth_to_last import kth_to_last


def test_empty_list():
    linked_list = LinkedList()
    result = kth_to_last(linked_list, 0)
    assert result == []


def test_k_equals_zero():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    result = kth_to_last(linked_list, 0)
    assert result == [1, 2, 3]


def test_k_within_bounds():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)
    linked_list.append(5)
    result = kth_to_last(linked_list, 2)
    assert result == [3, 4, 5]


def test_k_greater_than_length():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    result = kth_to_last(linked_list, 5)
    assert result == []


def test_negative_k():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    result = kth_to_last(linked_list, -1)
    assert result == []
