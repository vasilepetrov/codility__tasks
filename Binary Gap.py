from collections import deque

n = int(input())
remainders = deque()
counter = 0
max_counter = 0
start_counting = False
while True:
    remainder = n % 2
    remainders.appendleft(remainder)
    if remainder == 1:
        start_counting = True
        if counter > max_counter:
            max_counter = counter
        counter = 0
    else:
        if start_counting:
            counter += 1
    if n != 1:
        n = n // 2
        if n == 1:
            remainders.appendleft(n)
            if counter > max_counter or start_counting == False:
                max_counter = counter
            break
    else:
        max_counter = 0
        break

print(max_counter)