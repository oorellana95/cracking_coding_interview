from questions.chapter_2_linked_list.linked_list import LinkedList
from questions.chapter_2_linked_list.question_4_partition import partition_linked_list


def test_partition_values_less_than_partition():
    # Create a linked list with values: 3 -> 2 -> 1 -> 4 -> 5
    linked_list = LinkedList()
    linked_list.append(3)
    linked_list.append(2)
    linked_list.append(1)
    linked_list.append(4)
    linked_list.append(5)

    # Perform partitioning with a partition value of 4.
    result_linked_list = partition_linked_list(linked_list.root, 4)

    # Convert the result to a list for assertion.
    result_list = result_linked_list.to_list()

    # Verify that values less than 4 are on the left, and values greater than or equal to 4 are on the right.
    assert result_list == [3, 2, 1, 4, 5]

# Test case for partitioning with values greater than or equal to the partition value.
def test_partition_values_greater_than_partition():
    # Create a linked list with values: 6 -> 7 -> 8 -> 9 -> 10
    linked_list = LinkedList()
    linked_list.append(6)
    linked_list.append(7)
    linked_list.append(8)
    linked_list.append(9)
    linked_list.append(10)

    # Perform partitioning with a partition value of 5.
    result_linked_list = partition_linked_list(linked_list.root, 5)

    # Convert the result to a list for assertion.
    result_list = result_linked_list.to_list()

    # Verify that all values are greater than or equal to 5, and the left partition is empty.
    assert result_list == [6, 7, 8, 9, 10]

# Test case for an empty linked list.
def test_partition_empty_linked_list():
    # Create an empty linked list.
    linked_list = LinkedList()

    # Perform partitioning with any partition value (should result in an empty list).
    result_linked_list = partition_linked_list(linked_list.root, 5)

    # Verify that the result is an empty list.
    assert result_linked_list == None
