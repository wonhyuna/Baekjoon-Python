n = int(input())
arr = []

for i in range(n):
    cnt = 0
    sum = 0
    arr = input()
    for j in range(len(arr)):
        if arr[j] == 'O':
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    print(sum)
    



