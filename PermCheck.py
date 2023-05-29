A = [4, 1, 3, 2]

counter = 0


def solution(A):
    if len(A) == 1:
        if A[0] == 1:
            return 1
        return 0

    A = sorted(A)
    if A[0] != 1:
        return 0

    for i in range(len(A) - 1):
        if A[i] + 1 != A[i + 1]:
            return 0
    return 1

print(solution(A))