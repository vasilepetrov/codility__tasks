import sys

def solution(A):
    sum_array = sum(A)
    sum_until_now = 0
    result = sys.maxsize
    for i in range(0, len(A) - 1):
        sum_until_now += A[i]
        right_sum = sum_array - sum_until_now
        current_result = abs(sum_until_now - right_sum)
        if current_result < result:
            result = current_result
    return result


print(solution([2000, 0]))