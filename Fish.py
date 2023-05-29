from collections import deque
A = [4, 3, 2, 1, 5]
B = [0, 1, 0, 0, 0]

def solution(A, B):
    fish_downstream = deque()
    B = deque(B)
    count = len(A)
    for i in range(len(B)):
        if B[i] == 1:
            fish_downstream.append(A[i])
        else:
            current_fish_upstream = A[i]
            while fish_downstream:
                fish_it_will_fight = fish_downstream.pop()
                if fish_it_will_fight > current_fish_upstream:
                    count -= 1
                    fish_downstream.append(fish_it_will_fight)
                    break
                else:
                    count -= 1
    return count


print(solution(A, B))