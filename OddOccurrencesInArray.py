A = [9, 3, 9, 3, 9, 7, 9]
A = sorted(A)
number = None
for i in range(0, len(A), 2):
    if A[i+1] != A[i]:
        number = A[i]
        break

print(number)
