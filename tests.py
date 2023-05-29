def countingSort(A, k):
    n = len(A)
    count = [0] * (k + 1)
    for i in range(n):
        count[A[i]] += 1
    p = 0
    for i in range(k + 1):
        for j in range(count[i]):
            A[p] = i
            p += 1
    return A


A = [2, 5, 3, 0, 2, 3, 0, 3]
k = max(A)  # The maximum number in the list, which is 5 in this case

print(countingSort(A, k))  # Output: [0, 0, 2, 2, 3, 3, 3, 5]
