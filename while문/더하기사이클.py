count = 0
total = 0
n = int(input())
check = n
new = 0

while True:
    first = n // 10
    second = n % 10
    total = first + second
    new = (second % 10) * 10 + (total % 10)
    n = new
    count += 1
    if (check == new):
        break
print(count)