from questions.chapter_3_stacks_and_queues.question_4_queue_via_stacks import QueueViaStacks

if __name__ == '__main__':
    queue = QueueViaStacks()
    queue.enqueue(5)
    queue.enqueue(10)
    queue.enqueue(15)
    queue.enqueue(20)
    queue.enqueue(25)
    print(queue.dequeue())
    print(queue.dequeue())
    print(queue.dequeue())
