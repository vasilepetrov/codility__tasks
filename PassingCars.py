def solution(A):

    def prefix_sums(array):
        n = len(array)
        P = [0] * (n + 1)
        for k in range(1, n + 1):
            P[k] = P[k - 1] + array[k - 1]
        return P

    def count_total(P, x, y):
        return P[y+1] - P[x]

    prefix_sums = prefix_sums(A)
    result = 0
    for i in range(len(A)):
        if A[i] == 0:
            result += count_total(prefix_sums, i, len(A) - 1)

    if result > 1000000000:
        return -1
    return result
