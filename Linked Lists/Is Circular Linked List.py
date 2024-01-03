#Is Circular Linked List

from SinglyLinkedLists import LinkedList
from CircularLinkedList import CircularLinkedList

def is_circular_linked_list(input_list):
    if input_list.head:
        cur_node = input_list.head
        while cur_node.next:
            cur_node = cur_node.next
            if cur_node.next == input_list.head:
                return True
        return False
    else:
        return False
    
cllist = CircularLinkedList()
cllist.append(1)
cllist.append(2)
cllist.append(3)
cllist.append(4)

llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.append(4)

print(is_circular_linked_list(input_list=cllist))
print(is_circular_linked_list(input_list=llist))