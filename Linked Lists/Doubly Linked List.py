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
