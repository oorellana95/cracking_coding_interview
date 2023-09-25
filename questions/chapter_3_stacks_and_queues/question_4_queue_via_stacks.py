"""
Queue via Stacks:
Implement a MyQueue class which implements a queue using two stacks.
"""
from questions.chapter_3_stacks_and_queues.my_stack import MyStack


class QueueViaStacks:
    def __init__(self):
        self.queue = MyStack([])

    def enqueue(self, item):
        self.queue.push(item)

    def dequeue(self):
        temp = MyStack([])

        while self.queue:
            temp.push(self.queue.pop())

        popped_value = temp.pop()
        while temp:
            self.queue.push(temp.pop())

        return popped_value
