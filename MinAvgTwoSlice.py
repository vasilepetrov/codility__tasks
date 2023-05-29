import sys

A = [4, 2, 2, 5, 1, 5, 8]

def solution(A):
    index = 0
    min_average = sys.maxsize
    def prefix_sums(array):
        n = len(array)
        P = [0] * (n + 1)
        for k in range(1, n + 1):
            P[k] = P[k - 1] + array[k - 1]
        return P
    def count_total(P, x, y):
        return P[y+1] - P[x]
    P = prefix_sums(A)
    for i in range(len(A)-2):
        start_index = i
        end_index = i + 1
        end_index_two = i + 2
        res = count_total(P, start_index, end_index)
        avg = res/2
        if avg < min_average:
            min_average = avg
            index = i
        res_2 = count_total(P, start_index, end_index_two)
        avg_2 = res_2/3
        if avg_2 < min_average:
            min_average = avg_2
            index = i

    last_pair_result = count_total(P, len(A) - 2, len(A) - 1) / 2
    if last_pair_result < min_average:
        min_average = last_pair_result
        index = len(A) - 2

    return index
