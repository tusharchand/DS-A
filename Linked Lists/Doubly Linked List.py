#Doubly Linked List

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        new_node = Node(data)
        new_node.next = self.head

        if self.head:
            self.head.prev = new_node

        self.head = new_node

    # Adding a node at the front of the list
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        new_node.prev = None

        if self.head:
            self.head.prev = new_node

        self.head = new_node

    def insertAfter(self, prev_node, data):
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node

        if new_node.next:
            new_node.next.prev = new_node

    def insertAfter(self, next_node, new_data):
        if next_node is None:
            return

        new_node = Node(new_data)

        new_node.next = next_node
        new_node.prev = new_node.prev
        next_node.prev = new_node
        if new_node.prev is not None:
            new_node.prev.next = new_node
        else:
            self.head = new_node

    # Add a node at the end of the DLL
    def append(self, new_data):
        new_node = Node(new_data)
        new_node.next = None

        last = self.head

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        while last.next:
            last = last.next

        new_node.prev = last
        last.next = new_node