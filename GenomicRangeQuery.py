S = 'CAGCCTA'
def solution(S, P, Q):
    result = []
    def prefix_sums(S):
        n = len(S)
        prefix_sums_A = [0] * (n + 1)
        prefix_sums_C = [0] * (n + 1)
        prefix_sums_G = [0] * (n + 1)
        prefix_sums_T = [0] * (n + 1)
        for k in range(1, n + 1):
            prefix_sums_A[k] = prefix_sums_A[k - 1] + (S[k - 1] == 'A')
            prefix_sums_C[k] = prefix_sums_C[k - 1] + (S[k - 1] == 'C')
            prefix_sums_G[k] = prefix_sums_G[k - 1] + (S[k - 1] == 'G')
            prefix_sums_T[k] = prefix_sums_T[k - 1] + (S[k - 1] == 'T')
        return prefix_sums_A, prefix_sums_C, prefix_sums_G, prefix_sums_T

    def count_total(P, x, y):
        return P[y + 1] - P[x]

    prefix_sums = prefix_sums(S)
    for i in range(len(P)):
        start_index = P[i]
        end_index = Q[i]

        count_total_A = count_total(prefix_sums[0], start_index, end_index)
        if count_total_A != 0:
            result.append(1)
            continue
        count_total_C = count_total(prefix_sums[1], start_index, end_index)
        if count_total_C != 0:
            result.append(2)
            continue
        count_total_G = count_total(prefix_sums[2], start_index, end_index)
        if count_total_G != 0:
            result.append(3)
            continue
        count_total_T = count_total(prefix_sums[3], start_index, end_index)
        if count_total_T != 0:
            result.append(4)
    return result

print(solution('CAGCCTA', P = [2, 5, 0], Q = [4, 5, 6]))