"""
Sort Stack:
Write a program to sort a stack such that the smallest items are on the top. You can use
an additional temporary stack, but you may not copy the elements into any other data structure
(such as an array). The stack supports the following operations: push, pop, peek, and is Empty.
"""


class SortedStack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        temp_stack = []
        while self.stack and self.stack[-1] < value:
            temp_stack.append(self.stack.pop())
        self.stack.append(value)
        while temp_stack:
            self.stack.append(temp_stack.pop())

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]

    def is_empty(self):
        return not self.stack

