from questions.chapter_3_stacks_and_queues.question_5_stored_stack import SortedStack


def test_push_and_peek():
    stack = SortedStack()
    stack.push(3)
    stack.push(1)
    stack.push(2)
    assert stack.peek() == 1


def test_pop():
    stack = SortedStack()

    stack.push(3)
    stack.push(1)
    stack.push(2)

    assert stack.pop() == 1
    assert stack.pop() == 2
    assert stack.pop() == 3
    assert stack.pop() is None


def test_is_empty():
    stack = SortedStack()
    assert stack.is_empty() is True  # Stack is initially empty


def test_is_not_empty():
    stack = SortedStack()
    stack.push(1)
    assert stack.is_empty() is False  # Stack is not empty after pushing an element
