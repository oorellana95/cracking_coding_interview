"""
Queue
"""

from collections import deque


class MyQueue:
    def __init__(self, items=[]):
        self.queue = deque()
        for item in items:
            self.queue.append(item)

    def __iter__(self):
        for item in self.queue:
            yield item

    def __repr__(self):
        items = []
        for item in self.queue:
            items.append(str(item))
        return "MyQueue: " + " -> ".join(items)

    def add(self, item):
        self.queue.append(item)

    def peek(self):
        return self.queue.popleft()

    def clear(self):
        self.queue.clear()

