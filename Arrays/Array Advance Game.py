#Array Advance Game

def array_advance(A):
    furthest_reached = 0
    i = 0
    last_idx = len(A) - 1
    while furthest_reached < last_idx and i <= furthest_reached:
        furthest_reached = max(furthest_reached, A[i] + i)
        i += 1
    return furthest_reached >= last_idx

#TestCases

# True: Possible to navigate to last index in A:
# Moves: 1,3,2
A = [3, 3, 1, 0, 2, 0, 1]
print(array_advance(A))

# False: Not possible to navigate to last index in A:
A = [3, 2, 0, 0, 2, 0, 1]
print(array_advance(A))