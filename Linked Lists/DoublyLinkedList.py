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

    def delete(self, key):
        cur_node = self.head
        while cur_node:
            if cur_node == self.head and cur_node.data == key:
                #If Head is the only Node
                if cur_node.next is None:
                    cur_node = None
                    self.head = None
                    return
                #If Head is not the only Node
                else:
                    next = cur_node.next
                    next.prev = None
                    cur_node.next = None
                    self.head = next
                    cur_node = None
                    return
            elif cur_node.data == key:
                if cur_node.next:
                    prev = cur_node.prev
                    next = cur_node.next
                    next.prev = prev
                    prev.next = next
                    cur_node.next = None
                    cur_node.prev = None
                    cur_node = None
                    return
                else:
                    prev = cur_node.prev
                    prev.next = None
                    cur_node.prev = None
                    cur_node = None
                    return
            cur_node = cur_node.next

    def reverse(self):
        temp = None
        cur_node = self.head
        while cur_node:
            temp = cur_node.prev
            cur_node.prev = cur_node.next
            cur_node.next = temp
            cur_node = cur_node.prev
        if temp:
            self.head = temp.prev

#TestCases

#Test for Appened, Prepend and Print List
# dllist = DoublyLinkedList()
# dllist.prepend(0)
# dllist.append(1)
# dllist.append(2)
# dllist.append(3)
# dllist.append(4)
# dllist.prepend(5)

# #Test for add after node
# dllist.add_after_node(3,6)
# dllist.add_before_node(4,9)

# dllist.print_list()

#Test for Deletion
# dllist = DoublyLinkedList()
# dllist.append(1)
# dllist.append(2)
# dllist.append(3)
# dllist.append(4)

# dllist.delete(1)
# dllist.delete(6)
# dllist.delete(4)

# dllist.delete(3)
# dllist.print_list()

#Test for Reversing the List
dllist = DoublyLinkedList()
dllist.append(1)
dllist.append(2)
dllist.append(3)
dllist.append(4)
dllist.reverse()
dllist.print_list()