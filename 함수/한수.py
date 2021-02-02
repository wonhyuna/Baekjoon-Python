def han(n):
    if n < 100:
        return n
    elif 100 <= n <= 1000:
        count = 0
        for i in range (100, n+1):
            first = i // 100
            second = (i % 100) // 10
            third = i % 10
            if first - second == second - third:
                count += 1
        return (99 + count)

num = int(input())
print(han(num))   