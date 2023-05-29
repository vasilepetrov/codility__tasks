def solution(A):
    A.sort()
    n = len(A)
    if n == 0:
        return 0
    result = 1
    for i in range(n-1):
        if A[i] != A[i + 1]:
            result += 1

    return result