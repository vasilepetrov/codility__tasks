array = [3, 8, 9, 7, 6]
K = int(input())
# K = K % len(array)
new_array = [0] * len(array)

for i in range(len(array)):
    new_array[(i + K) % len(array)] = array[i]

print(new_array)