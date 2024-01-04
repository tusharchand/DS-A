#DoublyLinkedList

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            cur_node = self.head
            while cur_node.next:
                cur_node = cur_node.next
            new_node = Node(data)
            cur_node.next = new_node
            new_node.prev = cur_node

    def prepend(self, data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            new_node = Node(data)
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def add_after_node(self, key, data):
        cur_node = self.head
        while cur_node:
            if cur_node.next is None and cur_node.data == key:
                self.append(data)
                return
            elif cur_node.data == key:
                new_node = Node(data)
                next = cur_node.next
                cur_node.next = new_node
                new_node.next = next
                next.prev = new_node
                new_node.prev = cur_node
                return
            cur_node = cur_node.next

    def add_before_node(self, key, data):
        cur_node = self.head
        while cur_node:
            if cur_node.next is None and cur_node.data == data:
                self.prepend(data)
                return
            elif cur_node.data == key:
                new_node = Node(data)
                prev = cur_node.prev
                cur_node.prev = new_node
                new_node.next = cur_node
                new_node.prev = prev
                prev.next = new_node
                return
            cur_node = cur_node.next

#TestCases

#Test for Appened, Prepend and Print List
dllist = DoublyLinkedList()
dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(5)

#Test for add after node
dllist.add_after_node(3,6)
dllist.add_before_node(4,9)

dllist.print_list()