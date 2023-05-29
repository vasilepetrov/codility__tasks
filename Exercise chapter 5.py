def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P


def count_total(P, x, y):
    return P[y+1] - P[x]


def mushrooms(A, k, m):
    pref_sums = prefix_sums(A)
    max_result = 0
    if k == 0:
        positions_left_for_right_direction = m
    else:
        for i in range(m+1):
            if (k - i) > 0:
                left_position = k-i
            else:
                left_position = 0
            positions_left_for_right_direction = m - (2 * i)
            if k + positions_left_for_right_direction < len(A):
                right_position = k + positions_left_for_right_direction
            else:
                right_position = len(A) - 1
            curren_result = count_total(pref_sums, left_position, right_position)
            if curren_result > max_result:
                max_result = curren_result

    return max_result

print(mushrooms([2,3,7,5,1,3,9], 4, 6))