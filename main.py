from questions.chapter_2_linked_list.linked_list import Node, LinkedList
from questions.chapter_2_linked_list.question_2_kth_to_last import kth_to_last

if __name__ == '__main__':
    root = Node(0)

    root.append_to_tail(Node(1))
    root.append_to_tail(Node(4))
    root.append_to_tail(Node(5))
    root.append_to_tail(Node(6))
    root = root.delete_specific_node_by_index(0)

    linked_list = LinkedList(100).list_to_nodes([0, 0, 0, 2, 3, 7, 6, 4, 3, 2])
    print(kth_to_last(linked_list, 12))
