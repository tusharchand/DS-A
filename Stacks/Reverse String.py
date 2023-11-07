#Reverse String
from Stack import Stack

def reverse_string(stack, input_str):
    for i in range(len(input_str)):
        stack.push(input_str[i])

    rev_str=''

    while not stack.is_empty():
        rev_str += stack.pop()
     
    return rev_str

s = Stack()
input_str = "!evitacudE ot emocleW"
print(reverse_string(s, input_str))