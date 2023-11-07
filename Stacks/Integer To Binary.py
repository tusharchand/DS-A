#Integer To Binary
from Stack import Stack

def convert_int_to_bin(dec_num):
    stack = Stack()
    binary = ''

    while dec_num != 0:
        remainder = dec_num % 2
        stack.push(str(remainder))
        dec_num = int(dec_num/2)

    while not stack.is_empty():
        binary += stack.pop()

    return binary

#Test
print(convert_int_to_bin(55))