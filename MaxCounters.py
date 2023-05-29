def solution(N, A):
    counters = [0] * N
    min_value = 0
    max_value = 0

    for i in range(len(A)):
        if A[i] > N:
            min_value = max_value
        else:
            if counters[A[i] - 1] < min_value:
                counters[A[i] - 1] = min_value

            counters[A[i]-1] += 1
            if counters[A[i]-1] > max_value:
                max_value += 1
    for j in range(len(counters)):
        if counters[j] < min_value:
            counters[j] = min_value
    return counters


print(solution(5, A=[3, 4, 4, 6, 1, 4, 4]))
print(solution(1, [1]))