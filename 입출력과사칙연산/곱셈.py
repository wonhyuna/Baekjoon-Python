A = int(input())
B = int(input())
num1 = B//100
num2 = (B%100)//10
num3 = B%10
print(A*num3)
print(A*num2)
print(A*num1)
print(A*B)