from collections import deque

def grocery_store(A):
    n = len(A)
    size, result = 0, 0
    for i in range(n):
        if A[i] == 0:
            size += 1
        else:
            size -= 1
            result = max(result, -size)
    return result

print(grocery_store(A = [1, 0, 1, 1, 0, 0, 1, 0]))