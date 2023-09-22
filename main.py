from questions.chapter_2_linked_list.linked_list import LinkedList
from questions.chapter_2_linked_list.question_4_partition import partition_linked_list

if __name__ == '__main__':

    root = LinkedList(100).list_to_nodes([0, 0, 0, 2, 3, 7, 6, 4, 3, 2])
    print(partition_linked_list(root, 4))
