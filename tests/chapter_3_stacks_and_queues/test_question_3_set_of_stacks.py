from questions.chapter_3_stacks_and_queues.question_3_set_of_stacks import SetOfStacks


def test_push():
    stack = SetOfStacks(max_capacity=2)
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert len(stack.stacks) == 2
    assert len(stack.stacks[0]) == 2
    assert len(stack.stacks[1]) == 1


def test_pop():
    stack = SetOfStacks(max_capacity=2)
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1
    assert len(stack.stacks) == 1
    assert stack.pop() is None  # No more elements to pop, should return None


def test_empty_stack():
    stack = SetOfStacks(max_capacity=2)
    assert stack.pop() is None  # Pop from an empty stack should return None


def test_pop_at():
    stack = SetOfStacks(max_capacity=2)

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    assert stack.pop_at(0) == 1  # Pop from the first stack
    assert stack.pop_at(2) == 4  # Pop from the second stack
    assert stack.pop_at(1) == 3  # Pop from the first stack again
    assert stack.pop_at(14) is None
