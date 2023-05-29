import sys


# Solution 1 (with counting)
def solution(X, A):
    count = [0] * (X + 1)
    print(count)
    sum_counts = 0
    for i in range(len(A)):
        if count[A[i]] == 0:
            count[A[i]] = 1
            sum_counts += 1
            if sum_counts == X:
                return i
    return -1


# Solution 2 (with set())

def solution_two(X, A):
    set_A = set()
    min_time = -sys.maxsize
    for i in range(len(A)):
        set_A.add(A[i])
        if len(set_A) == X:
            min_time = i
            return min_time
    return -1
