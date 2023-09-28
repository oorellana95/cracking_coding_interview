from questions.chapter_3_stacks_and_queues.question_6_queue_shelter import QueueShelter, Animal


def test_empty_queue():
    shelter = QueueShelter()
    assert shelter.dequeue_any() is None


def test_enqueue_and_dequeue_any():
    shelter = QueueShelter()

    shelter.enqueue("Buddy", Animal.DOG)
    shelter.enqueue("Mittens", Animal.CAT)
    shelter.enqueue("Whiskers", Animal.CAT)

    assert shelter.dequeue_any() == "Buddy"
    assert shelter.dequeue_any() == "Mittens"
    assert shelter.dequeue_any() == "Whiskers"
    assert shelter.dequeue_any() is None


def test_dequeue_by_dog():
    shelter = QueueShelter()

    shelter.enqueue("Rex", Animal.DOG)
    shelter.enqueue("Fluffy", Animal.CAT)
    shelter.enqueue("Simba", Animal.CAT)

    assert shelter.dequeue_by_kind(Animal.DOG) == "Rex"
    assert shelter.dequeue_by_kind(Animal.DOG) is None


def test_dequeue_by_cat():
    shelter = QueueShelter()

    shelter.enqueue("Rex", Animal.DOG)
    shelter.enqueue("Fluffy", Animal.CAT)
    shelter.enqueue("Simba", Animal.CAT)

    assert shelter.dequeue_by_kind(Animal.CAT) == "Fluffy"
    assert shelter.dequeue_by_kind(Animal.CAT) == "Simba"
    assert shelter.dequeue_by_kind(Animal.CAT) is None


def test_dequeue_by_not_found_kind():
    shelter = QueueShelter()

    shelter.enqueue("Rex", Animal.DOG)
    shelter.enqueue("Fluffy", Animal.CAT)
    shelter.enqueue("Simba", Animal.CAT)

    assert shelter.dequeue_by_kind(Animal.BIRD) is None
