#Circular Singly Linked List

class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
            return

        current = self.head

        while current.next != self.head:
            current = current.next

        current.next = new_node
        new_node.next = self.head

    def deleteNode(self, key):
        if self.head is None:
            return
        
        last = self.head
        
        #if the list only contains single element
        if self.head.next == self.head and self.head.data == key:
            self.head = None

        #if the list has more than 1 element and the first element is the key
        if self.head.data == key:
            current = self.head
            
            while current.next != self.head:
                current = current.next

            current.next = self.head.next
            self.head = self.head.next
            
            return

        # Either the node to be deleted is 
        # not found or the end of list 
        # is not reached 
        while last.next != self.head and last.next.data != key:
            last = last.next
        
        if last.next.data == key:
            d = last.next
            last.next = d.next
            d = None
        else:
            print('Node not found')
            return

    def printList(self):
        current = self.head
        if self.head is None:
            print('Empty List')
            return
        while current.next != self.head:
            print(current.data)
            current = current.next