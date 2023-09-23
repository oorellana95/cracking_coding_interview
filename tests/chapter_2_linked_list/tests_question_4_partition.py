from questions.chapter_2_linked_list.linked_list import LinkedList
from questions.chapter_2_linked_list.question_4_partition import partition_linked_list


def test_partition_values_less_than_partition():
    linked_list = LinkedList()
    linked_list.append(3)
    linked_list.append(2)
    linked_list.append(1)
    linked_list.append(4)
    linked_list.append(5)

    result_linked_list = partition_linked_list(linked_list.root, 4)
    result_list = result_linked_list.to_list()

    assert result_list == [3, 2, 1, 4, 5]

def test_partition_values_greater_than_partition():
    linked_list = LinkedList()
    linked_list.append(6)
    linked_list.append(7)
    linked_list.append(8)
    linked_list.append(9)
    linked_list.append(10)

    result_linked_list = partition_linked_list(linked_list.root, 5)

    result_list = result_linked_list.to_list()

    assert result_list == [6, 7, 8, 9, 10]


def test_partition_empty_linked_list():
    linked_list = LinkedList()

    result_linked_list = partition_linked_list(linked_list.root, 5)

    assert result_linked_list == None
