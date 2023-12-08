# Test File

# Creating a Node
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

# Creating Singly Linked List
class SinglyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def push(self, data):
        new_node = Node(data)

        # Not required
        # if self.head is None:
        #     self.head = new_node
        #     return

        new_node.next = self.head
        self.head = new_node

    def insertAfter(self, prev_node, data):
        if not prev_node:
            return

        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last = self.head

        while last.next:
            last = last.next

        last.next = new_node

    def search(self, x):
        current = self.head

        while current != None and current.data != x:
            current = current.next
        
        if current and current.data == x:
            return True
        else:
            return False

    def getCount(self):
        count = 0
        current = self.head
        
        while current:
            current = current.next
            count += 1
        
        return count

    def reverse(self):
        prev = None
        current = self.head
        
        while current:
            next = current.next
            current.next = prev
            prev = current
            current = next

        self.head = prev
    
    def print_list(self):
        current = self.head
        if self.head.data is None:
            print('Empty LList')
            return

        while current:
            print(current.data)
            current = current.next
    
    def deleteN(self, position):
        if self.head:
            current_node = self.head

            if position == 0:
                temp = self.head.next
                self.head = temp
                return
            prev = None
            count = 0
            while current_node and count != position:
                count+=1
                prev = current_node
                current_node = current_node.next
            
            if current_node is None:
                return
            
            prev.next = current_node.next
            current_node.next = None
    
    def deleteList(self):
        current = self.head

        while current:
            next = current.next
            current.data = None
            # current.next = None
            del current.next
            current = next

    def getNth(self, index):
        if self.head:
            current = self.head
            
            if index == 0:
                return current.data
            
            count = 0
            
            while current and count != index:
                current = current.next
                count += 1
            # import pdb
            # pdb.set_trace()
            if current is None:
                print('Nth element does not exist')
                return

            print("Element at index {index} is : {data}".format(index=index, data=current.data))
            return

    def printNthFromLast(self, n):
        if self.head:
            current = self.head
            count = 0

            while current.next:
                current = current.next
                count += 1
            
            x_from_n = count - n + 1
            count = 0
            current = self.head
            while current and count !=x_from_n:
                current = current.next
                count += 1
            
            if current is None:
                return
            
            return current.data
                    

#Test Cases

#Test Case 1: Test the Search Function
# llist = SinglyLinkedList()
# x = 3

# llist.push(10)
# llist.push(30)
# llist.push(11)
# llist.push(21)
# llist.push(14)
 
# # Function call
# if llist.search(10):
#     print("Yes")
# else:
#     print("No")

#Test Case 2: Test the Count Function
# llist = SinglyLinkedList()
# llist.push(1)
# llist.push(3)
# llist.push(1)
# llist.push(2)
# llist.push(1)
    
# # Function call
# print("Count of nodes is :", llist.getCount())

#Test Case 3: Test Reverse and Print List Function
# Driver code
llist = SinglyLinkedList()
llist.push(20)
llist.push(4)
llist.push(15)
llist.push(85)
 
print ("Given linked list")
llist.print_list()
llist.reverse()
print ("\nReversed linked list")
llist.print_list()
 
#Test Case 4: Delete any position from list
pos_to_rem=0
llist.deleteN(pos_to_rem)
print ("Linked list after removing element at position " + str(pos_to_rem))
llist.print_list()

#Test Case 5: Delete the LList
# print("Deleting LList")
# llist.deleteList()
# llist.print_list()
 
 #Test Case 6: Get n-th element
n = 2
llist.getNth(n)

print('Element {n} from end: {x}'.format(n=n, x=llist.printNthFromLast(n)))