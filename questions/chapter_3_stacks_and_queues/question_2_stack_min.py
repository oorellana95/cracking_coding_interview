"""
Stack Min:
How would you design a stack which, in addition to push and pop, has a function min
which returns the minimum element? Push, pop and min should all operate in 0(1) time.

To achieve O(1) time complexity for the min operation in a stack, you can indeed use a heap
(specifically, a min-heap or a priority queue).
"""


class MyMinStack:
    def __init__(self):
        self.data = []
        self.min_stack = []

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

        if not self.min_stack or item <= self.min_stack[-1]:
            self.min_stack.append(item)

    def pop(self):
        if not self.data:
            return None

        popped_element = self.data.pop()
        if popped_element >= self.min_stack[-1]:
            return popped_element
        return self.min_stack.pop()

    def min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]
