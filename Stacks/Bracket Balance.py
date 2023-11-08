#Bracket Balance
from Stack import Stack
import pdb

def is_paren_balanced(paren_string):
    s = Stack()
    index = 0
    is_balanced = True
    pdb.set_trace()
    while index < len(paren_string) and is_balanced:
        paren = paren_string[index]
        if paren in '[{(':
            s.push(paren)
        else:
            if s.is_empty():
                is_balanced = False
                break
            else:
                top = s.pop()
                if not is_match(top, paren):
                    is_balanced = False
                    break
        index += 1

    if s.is_empty() and is_balanced == True:
        return True
    else:
        return False

def is_match(paren1, paren2):
    if paren1 == '(' and paren2 == ')':
        return True
    elif paren1 == '{' and paren2 == '}':
        return True
    elif paren1 == '[' and paren2 == ']':
        return True
    else:
        return False

#Test 1 - Good Case
print("String : (((({})))) Balanced or not?")
print(is_paren_balanced("(((({}))))"))

#Test 2 - Bad Case
print("String : [][]]] Balanced or not?")
print(is_paren_balanced("[][]]]"))

#Test 3 - Special Case
print("String : [][] Balanced or not?")
print(is_paren_balanced("[][]"))