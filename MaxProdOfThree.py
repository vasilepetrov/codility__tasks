import sys

def solution(A):
    A.sort()
    result = None
    if A[-1] <= 0:  # all negative numbers
        result = A[-3] * A[-2] * A[-1]
    if A[0] >= 0:  # all positive numbers
        result = A[-3] * A[-2] * A[-1]
    if A[0] < 0 and A[1] < 0 and A[-1] >= 0:
        result = max(A[0] * A[1] * A[-1], A[-1] * A[-2] * A[-3])
    if A[0] < 0 and A[1] >=0:
        result = A[-1] * A[-2] * A[-3]

    return result


A = [-10, -1, 0, 2]
print(solution(A))