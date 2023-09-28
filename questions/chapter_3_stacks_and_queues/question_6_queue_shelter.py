"""
Animal Shelter:
An animal shelter, which holds only dogs and cats, operates on a strictly"first in, first
out" basis. People must adopt either the "oldest" (based on arrival time) of all animals at the shelter,
or they can select whether they would prefer a dog or a cat (and will receive the oldest animal of
that type). They cannot select which specific animal they would like. Create the data structures to
maintain this system and implement operations such as enqueue, dequeueAny, dequeueDog,
and dequeueCat. You may use the built-in Linked list data structure.
"""

from enum import Enum


class Animal(Enum):
    DOG = 'dog'
    CAT = 'cat'
    BIRD = 'bird'


class QueueShelter:
    class Node:
        def __init__(self, name, kind):
            self.next = None
            self.name = name
            self.kind = kind

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, name, kind):
        new_node = self.Node(name, kind)

        if self.head is None:
            self.head = new_node
        else:
            self.tail.next = new_node
        self.tail = new_node

    def dequeue_any(self):
        if self.head is None:
            return None

        name = self.head.name
        self.head = self.head.next
        return name

    def dequeue_by_kind(self, kind):
        prev = None
        node = self.head

        while node:
            if node.kind == kind:
                name = node.name
                if prev:
                    prev.next = node.next
                else:
                    self.head = node.next
                return name
            prev = node
            node = node.next

        return None

