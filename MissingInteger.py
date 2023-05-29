A = [1, 2, 3, 4, 5, 6, 7]
print(sorted(A))


def solution(A):
    counter = [0] * (len(A) + 1)
    for i in range(len(A)):
        if 1 <= A[i] <= len(A) + 1:
            if counter[A[i] - 1] == 0:
                counter[A[i] - 1] = 1
    for j in range(len(counter)):
        if counter[j] == 0:
            return j + 1


print(solution(A))
