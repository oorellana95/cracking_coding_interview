from questions.chapter_2_linked_list.linked_list import LinkedList
from questions.chapter_2_linked_list.question_3_delete_middle_nodes import delete_specific_nodes_by_data, \
    delete_specific_node_by_index


def test_delete_nodes():
    # Create a linked list with some sample data
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(2)  # Duplicate value
    linked_list.append(4)

    # Delete nodes with data equal to 2
    result = delete_specific_nodes_by_data(linked_list, 2)

    # Convert the result to a list for assertion
    result_list = result.to_list()

    # Verify that nodes with data equal to 2 are deleted
    assert result_list == [1, 3, 4]

def test_delete_nodes_by_index():
    # Create a linked list with some sample data
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)

    # Delete nodes with data equal to 2
    result = delete_specific_node_by_index(linked_list, 1)

    # Convert the result to a list for assertion
    result_list = result.to_list()

    # Verify that nodes with data equal to 2 are deleted
    assert result_list == [1, 3, 4]
