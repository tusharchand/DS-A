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

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None

        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data < q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next

            new_head = s

        while p and q:
            if p.data < q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p

        self.head = new_head
        return self.head

    def remove_duplicates(self):
        cur = self.head
        prev = None
        dup_values = dict()

        while cur:
            if cur.data in dup_values:
                prev.next = cur.next
                cur = None
            else:
                dup_values[cur.data]=1
                prev = cur
            cur = prev.next

    def print_nth_from_last(self, n, method):
        if method == 1:
            #Method 1:
            total_len = self.len_iterative()
            cur = self.head 
            while cur:
                if total_len == n:
                #print(cur.data)
                    return cur.data
                total_len -= 1
                cur = cur.next
            if cur is None:
                return

        elif method == 2:
            # Method 2:
            p = self.head
            q = self.head

            if n > 0:
                count = 0
                while q:
                    count += 1
                    if(count>=n):
                        break
                    q = q.next

                if not q:
                    print(str(n) + " is greater than the number of nodes in list.")
                    return

                while p and q.next:
                    p = p.next
                    q = q.next
                return p.data
            else:
                return None

    def count_occurences_iterative(self, data):
        count = 0
        cur_node = self.head

        while cur_node:
            if cur_node.data == data:
                count += 1
            cur_node = cur_node.next

        return count

    def rotate(self, k):
        if self.head and self.head.next:
            p = self.head
            q = self.head
            prev = None
            count = 0

            while p and count < k:
                prev = p
                p = p.next
                q = q.next
                count += 1

            p = prev

            while q:
                prev = q
                q = q.next

            q = prev

            q.next = self.head
            self.head = p.next
            p.next = None

    def is_palindrome_1(self):
        s = ''
        p = self.head

        while p:
            s += p.data
            p = p.next

        return s == s[::-1]

    def is_palindrome_2(self):
        p = self.head
        s = []

        while p:
            s.append(p.data)
            p = p.next
        p = self.head
        while p:
            data = s.pop()
            if data != p.data:
                return False
            p = p.next
        return True

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

# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")

# print(llist.print_list())

# print ('Iterative Reversed:')

# llist.reverse_iterative()

# llist.print_list()

# print ('Recursive Reversed:')

# llist.reverse_recursive()

# llist.print_list()

#Test Merge Sorted
# llist_1 = LinkedList()
# llist_2 = LinkedList()

# llist_1.append(1)
# llist_1.append(5)
# llist_1.append(7)
# llist_1.append(9)
# llist_1.append(10)

# llist_2.append(2)
# llist_2.append(3)
# llist_2.append(4)
# llist_2.append(6)
# llist_2.append(8)

# llist_1.merge_sorted(llist_2)
# llist_1.print_list()

#Test Remove Duplicates
# llist = LinkedList()
# llist.append(1)
# llist.append(6)
# llist.append(1)
# llist.append(4)
# llist.append(2)
# llist.append(2)
# llist.append(4)

# print("Original Linked List")
# llist.print_list()
# print("Linked List After Removing Duplicates")
# llist.remove_duplicates()
# llist.print_list()

#Test Print Nth from last
# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")

# print(llist.print_nth_from_last(4,1))
# print(llist.print_nth_from_last(4,2))

#Test count occurences of input
# llist = LinkedList()
# llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.append(4)
# llist.append(5)
# llist.append(6)

# llist_2 = LinkedList()
# llist_2.append(1)
# llist_2.append(2)
# llist_2.append(1)
# llist_2.append(3)
# llist_2.append(1)
# llist_2.append(4)
# llist_2.append(1)
# print(llist_2.count_occurences_iterative(1))

#Test Rotate LList
# llist = LinkedList()
# llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.append(4)
# llist.append(5)
# llist.append(6)

# llist.rotate(4)
# llist.print_list()

#Test for Palindrome

llist = LinkedList()
llist.append('B')
llist.append('o')
llist.append('B')

llist_2 = LinkedList()
llist_2.append("A")
llist_2.append("B")
llist_2.append("C")

if llist.is_palindrome_1:
    print('Palindrome')
if llist.is_palindrome_2:
    print('Palindrome')

if llist_2.is_palindrome_1:
    print('Palindrome')
else:
    print('Not Palindrome')
llist_2.is_palindrome_2