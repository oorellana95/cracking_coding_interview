"""
Stack
"""


class MyStack:
    def __init__(self, data=[]):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __iter__(self):
        for item in self.data:
            yield item

    def __repr__(self):
        items = []
        for item in self.data:
            items.append(str(item))
        return "MyStack: [" + " <- ".join(items)

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.data:
            return self.data.pop()
        return None

    def pop_at(self, index):
        return self.data.pop(index)

    def is_empty(self):
        return not self.data
