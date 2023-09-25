from questions.chapter_3_stacks_and_queues.my_queue import MyQueue
from questions.chapter_3_stacks_and_queues.my_stack import MyStack

if __name__ == '__main__':
    my_stack = MyStack([1, 2, 3, 4, 5])

    my_stack.push(10)
    print(my_stack.peek())
    print(my_stack.peek())
    print(my_stack.is_empty())
    print(my_stack)

    my_queue = MyQueue([1, 2, 3, 4, 5])

    my_queue.add(6)
    print(my_queue.peek())
    print(my_queue)
