from questions.chapter_2_linked_list.linked_list import LinkedList
from questions.chapter_2_linked_list.question_6_palindrome_linked_list import palindrome_linked_list

if __name__ == '__main__':

    root = LinkedList().list_to_nodes([6, 8, 6, 6, 8, 6])
    print(palindrome_linked_list(root))
