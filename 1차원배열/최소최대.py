n = int(input())
arr = list(map(int, input().split()))
max = -1000001
min = 1000001

for i in range(n):
    if arr[i] > max:
        max = arr[i]
    if arr[i] < min:
        min = arr[i]
print(min, max)
