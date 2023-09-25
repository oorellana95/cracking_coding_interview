from questions.chapter_3_stacks_and_queues.question_4_queue_via_stacks import QueueViaStacks


def test_enqueue_and_dequeue():
    queue = QueueViaStacks()

    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)

    assert queue.dequeue() == 1
    assert queue.dequeue() == 2
    assert queue.dequeue() == 3
    assert queue.dequeue() is None  # No more elements to dequeue, should return None


def test_empty_queue():
    queue = QueueViaStacks()

    assert queue.dequeue() is None  # Dequeue from an empty queue should return None
