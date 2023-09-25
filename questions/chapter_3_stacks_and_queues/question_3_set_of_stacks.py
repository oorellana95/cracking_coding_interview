"""
Stack of Plates:
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetO-fStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks. push() and SetOfStacks. pop() should behave identically to a single stack
(that is, pop () should return the same values as it would if there were just a single stack).


Implement a function popAt ( int index) which performs a pop operation on a specific sub-stack.
"""
from questions.chapter_3_stacks_and_queues.my_stack import MyStack


class SetOfStacks:
    def __init__(self, max_capacity=3):
        self.stacks = []
        self.max_capacity = max_capacity

    def push(self, item):
        if not self.stacks or len(self.stacks[-1]) >= self.max_capacity:
            self.stacks.append(MyStack([]))
        self.stacks[-1].push(item)

    def pop(self):
        if not self.stacks:
            return None

        top_stack = self.stacks[-1]
        popped_element = top_stack.pop()

        if not top_stack and len(self.stacks) > 1:
            self.stacks.pop()

        return popped_element

    def pop_at(self, index):
        if index < 0:
            return None

        current_index = 0

        for stack in self.stacks:
            if index < current_index + len(stack):
                return stack.pop_at(index - current_index)
            current_index += len(stack)

        return None
