#Circular Linked List

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None

    def __len__(self):
        cur_node = self.head
        count = 0

        if self.head:
            if self.head.next == self.head:
                count = 1
            else:
                while cur_node:
                    count += 1
                    cur_node = cur_node.next
                    if cur_node == self.head:
                        break
            return count

    def prepend(self, data):
        new_node = Node(data)
        cur_node = self.head
        new_node.next = self.head

        if not self.head:
            new_node.next = self.head
        else:
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = new_node
        self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            cur_node = self.head
            while cur_node.next != self.head:
                cur_node = cur_node.next
            cur_node.next = new_node
            new_node.next = self.head

    def print_list(self):
        cur = self.head 

        while cur:
            print(cur.data)
            cur = cur.next
            if cur == self.head:
                break

    def remove(self, key):
        if self.head:
            if self.head.data == key:
                cur_node = self.head
                while cur_node.next != self.head:
                    cur_node = cur_node.next
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur_node.next = self.head.next
                    self.head = self.head.next
            else:
                cur_node = self.head
                prev = None
                while cur_node.next != self.head:
                    prev = cur_node
                    cur_node = cur_node.next
                    if cur_node.data == key:
                        prev.next = cur_node.next
                        cur_node = cur_node.next

    def remove_node(self, node):
        if self.head == node:
            cur_node = self.head
            while cur_node.next != self.head:
                cur_node = cur_node.next
            if self.head == self.head.next:
                self.head = None
            else:
                cur_node.next = self.head.next
                self.head = self.head.next
        else:
            cur_node = self.head
            prev = None
            while cur_node.next != self.head:
                prev = cur_node
                cur_node = cur_node.next
                if cur_node == node:
                    prev.next = cur_node.next
                    cur_node = cur_node.next

    def josephus_circle(self, step):
        cur_node = self.head
        length = len(self)
        
        while length > 1:
            count = 1
            while count != step:
                cur_node = cur_node.next
                count += 1
            print("KILL:" + str(cur_node.data))
            self.remove_node(cur_node)
            cur_node = cur_node.next
            length -= 1

    def split_list(self):
        size = len(self)

        if size == 0:
            return None
        if size == 1:
            return self.head

        mid = size // 2

        count = 0

        prev = None
        cur_node = self.head

        while cur_node and count < mid:
            count +=1
            prev = cur_node
            cur_node = cur_node.next
        prev.next = self.head

        split_cllist = CircularLinkedList()
        while cur_node.next != self.head:
            split_cllist.append(cur_node.data)
            cur_node = cur_node.next
        split_cllist.append(cur_node.data)

        self.print_list()
        print('\n')
        split_cllist.print_list()
            

#Test Prepend, Append and Print List
# cllist = CircularLinkedList()
# cllist.append("C")
# cllist.append("D")
# cllist.prepend("B")
# cllist.prepend("A")
# cllist.print_list()

#Test Remove Func
# cllist = CircularLinkedList()
# cllist.append("A")
# cllist.append("B")
# cllist.append("C")
# cllist.append("D")

# cllist.remove("A")
# cllist.remove("C")
# cllist.print_list()
# print(cllist.__len__())

#Test Split Circular Linked List
# A -> B -> C -> D -> ...
# A -> B -> ... and C -> D -> ...

# cllist = CircularLinkedList()
# cllist.append("A")
# cllist.append("B")
# cllist.append("C")
# cllist.append("D")
# cllist.append("E")
# cllist.append("F")

# cllist.split_list()

#Test Josephus Circle
cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)


cllist.josephus_circle(2)
cllist.print_list()