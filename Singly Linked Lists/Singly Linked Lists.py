#Singly Linked Lists

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):

        if not prev_node:
            print('Previous node does not exist.')
            return

        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def print_list(self):
        cur_node = self.head

        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def delete_node(self, key):

        cur_node = self.head

        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node.next = None
            return

        prev_node = None

        while cur_node and cur_node.data != key:
            prev_node = cur_node
            cur_node = cur_node.next
            
        if cur_node is None:
            return

        prev_node.next = cur_node.next
        cur_node.next = None

    def delete_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head

            if pos == 0:
                self.head = cur_node.next
                cur_node.next = None
                return

            prev_node = None
            count = 0

            while cur_node and count != pos:
                prev_node = cur_node
                cur_node = cur_node.next
                count += 1

            if cur_node is None:
                return

            prev_node.next = cur_node.next
            cur_node.next = None

    def len_iterative(self):
        count = 0
        cur_node = self.head

        while cur_node:
            cur_node = cur_node.next
            count += 1

        return count

    def len_recursive(self, node):
        if node is None:
            return 0
        return self.len_recursive(node.next) + 1

    def swap_nodes(self, key_1, key_2):        
        if key_1 == key_2:
            return
        
        prev_1 = None
        cur_1 = self.head
        
        while cur_1 and cur_1.data != key_1:
            prev_1 = cur_1
            cur_1 = cur_1.next

        prev_2 = None
        cur_2 = self.head
        
        while cur_2 and cur_2.data != key_2:
            prev_2 = cur_2
            cur_2 = cur_2.next
            
        if not cur_1 or not cur_2:
            return
        
        if prev_1:
            prev_1.next = cur_2
        else:
            self.head = cur_2
            
        if prev_2:
            prev_2.next = cur_1
        else:
            self.head = cur_1

        temp = cur_1.next
        cur_1.next = cur_2.next
        cur_2.next = temp
        # cur_1.next, cur_2.next = cur_2.next, cur_1.next

    def reverse_iterative(self):
        prev = None
        cur = self.head
        
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
        self.head = prev

    def reverse_recursive(self):

        def _reverse_recursive(cur, prev):
            if not cur:
                return prev
            
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        
            return _reverse_recursive(cur, prev)
        
        self.head = _reverse_recursive(cur=self.head, prev=None)
        
        
            

#TestCase
# llist = LinkedList()

# print("The length of an empty linked list is:")
# print(llist.len_recursive(llist.head))
# print('--------------')

# llist.append("A")
# llist.append("B")
# llist.append("C")

# llist.insert_after_node(llist.head.next, "D")

# llist.delete_node("B")
# llist.delete_node("E")

# llist.print_list()

# print('--------------')

# llist.delete_node_at_pos(1)

# llist.print_list()

# print('--------------')

# print("The length of the linked list calculated recursively is:")
# print(llist.len_recursive(llist.head))
# print("The length of the linked list calculated iteratively is:")
# print(llist.len_iterative())

# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")

# print("Original List")
# llist.print_list()

# llist.swap_nodes("B", "C")
# print("Swapping nodes B and C that are not head nodes")
# llist.print_list()

# llist.swap_nodes("A", "B")
# print("Swapping nodes A and B where key_1 is head node")
# llist.print_list()

# llist.swap_nodes("D", "B")
# print("Swapping nodes D and B where key_2 is head node")
# llist.print_list()

# llist.swap_nodes("C", "C")
# print("Swapping nodes C and C where both keys are same")
# llist.print_list()

llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")

print(llist.print_list())

print ('Iterative Reversed:')

llist.reverse_iterative()

llist.print_list()

print ('Recursive Reversed:')

llist.reverse_recursive()

llist.print_list()