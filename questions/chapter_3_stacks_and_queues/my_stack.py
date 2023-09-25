"""
Stack
"""


class MyStack:
    def __init__(self, data=[]):
        self.data = data

    def __iter__(self):
        for item in self.data:
            yield item

    def __repr__(self):
        items = []
        for item in self.data:
            items.append(str(item))
        return "[" + " <- ".join(items)

    def push(self, item):
        self.data.append(item)

    def peek(self):
        return self.data.pop()

    def is_empty(self):
        return self.data is None
