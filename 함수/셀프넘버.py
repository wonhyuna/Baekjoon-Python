def self_num(n):
    result = n
    while n != 0:
        result += n % 10
        n //= 10
    return result

list = []
for i in range(1, 10001):
    list.append(self_num(i))
    if i not in list:
        print(i)

