from questions.chapter_2_linked_list.linked_list import LinkedList
from questions.chapter_2_linked_list.question_3_delete_middle_nodes import delete_specific_nodes_by_data

if __name__ == '__main__':

    linked_list = LinkedList(100).list_to_nodes([0, 0, 0, 2, 3, 7, 6, 4, 3, 2])
    print(delete_specific_nodes_by_data(linked_list, 6))
