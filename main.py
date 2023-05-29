A = [2]
A = sorted(A)
missing = None

if len(A) == 1:
    if A[0] == 1:
        missing = A[0] + 1
    else:
        missing = A[0] - 1

for i in range(0, len(A) - 1):
    if A[i + 1] != A[i] + 1 or (i + 1) == len(A):
        missing = A[i] + 1

print(A)
print(missing)