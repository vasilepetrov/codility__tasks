def solution(A, B, K):
    if A % K != 0:
        first_one = A + (K - A % K)
    else:
        first_one = A
    last_one = B - B % K
    count = last_one / K - first_one / K + 1

    return count

print(solution(6, 11, 2))