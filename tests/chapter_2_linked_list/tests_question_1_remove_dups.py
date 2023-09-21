from questions.chapter_2_linked_list.linked_list import LinkedList
from questions.chapter_2_linked_list.question_1_remove_dups import remove_duplicates


def test_empty_list():
    # Test with an empty linked list
    linked_list = LinkedList()
    result = remove_duplicates(linked_list)
    assert result == []


def test_no_duplicates():
    # Test with a linked list without duplicates
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    result = remove_duplicates(linked_list)
    assert result.to_list() == [1, 2, 3]


def test_duplicates_removed():
    # Test with a linked list containing duplicates
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(3)
    linked_list.append(3)
    result = remove_duplicates(linked_list)
    assert result.to_list() == [1, 2, 3]
