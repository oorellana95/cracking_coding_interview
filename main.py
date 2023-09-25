from questions.chapter_3_stacks_and_queues.my_queue import MyQueue

if __name__ == '__main__':
    my_queue = MyQueue([1, 2, 3, 4, 5])

    my_queue.add(6)
    print(my_queue.peek())
    print(my_queue)
