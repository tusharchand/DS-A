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

#TestCases

#Test for Appened, Prepend and Print List
dllist = DoublyLinkedList()
dllist.prepend(0)
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.prepend(5)

dllist.print_list()