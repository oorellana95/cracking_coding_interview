from questions.chapter_3_stacks_and_queues.question_2_stack_min import MyMinStack


def test_push_and_peek():
    stack = MyMinStack()
    stack.push(5)
    assert stack.pop() == 5


def test_push_multiple_items():
    stack = MyMinStack()
    stack.push(5)
    stack.push(3)
    stack.push(7)
    assert stack.pop() == 7


def test_min():
    stack = MyMinStack()
    stack.push(5)
    stack.push(3)
    stack.push(7)
    assert stack.min() == 3


def test_empty_stack():
    stack = MyMinStack()
    assert stack.pop() is None
    assert stack.min() is None


def test_pop():
    stack = MyMinStack()
    stack.push(5)
    stack.push(3)
    stack.push(7)
    assert stack.pop() == 7
    assert stack.pop() == 3


def test_pop_empty_stack():
    stack = MyMinStack()
    assert stack.pop() is None


def test_iteration():
    stack = MyMinStack()
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert str(stack) == "MyStack: [1 <- 2 <- 3"

