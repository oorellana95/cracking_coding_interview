"""
LinkedList
"""


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __iter__(self):
        node = self
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        node = self
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next
        nodes.append("None")
        return " -> ".join(nodes)

    def to_list(self):
        node = self
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        return nodes

    def append_to_tail(self, new_node):
        node = self
        while node.next is not None:
            node = node.next
        node.next = new_node

    def delete_specific_node_by_index(self, index):
        if index == 0:
            return self.next

        current_index = 1
        node = self
        while node.next is not None:
            if current_index == index:
                node.next = node.next.next
                return self
            node = node.next
            current_index += 1
        return self


class LinkedList:
    def __init__(self, root=None):
        self.root = None if root is None else Node(root)

    def list_to_nodes(self, nodes: list):
        if self.root is None:
            self.root = Node(nodes.pop(0))

        current_node = self.root
        for node in nodes:
            current_node.next = Node(node)
            current_node = current_node.next
        return self.root

    def append(self, new_value):
        if self.root is None:
            self.root = Node(new_value)
        else:
            self.root.append_to_tail(Node(new_value))

    def to_list(self):
        return self.root.to_list()
