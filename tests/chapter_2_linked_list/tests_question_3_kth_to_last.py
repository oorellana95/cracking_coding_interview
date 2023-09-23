from questions.chapter_2_linked_list.linked_list import LinkedList
from questions.chapter_2_linked_list.question_3_delete_middle_nodes import delete_specific_nodes_by_data, \
    delete_specific_node_by_index


def test_delete_nodes():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(2)  # Duplicate value
    linked_list.append(4)

    result = delete_specific_nodes_by_data(linked_list, 2)
    result_list = result.to_list()

    assert result_list == [1, 3, 4]

def test_delete_nodes_by_index():
    linked_list = LinkedList()
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)

    result = delete_specific_node_by_index(linked_list, 1)
    result_list = result.to_list()

    assert result_list == [1, 3, 4]
