a = int(input())
b = int(input())
a1 = 0
b1 = 0
while a > 0:
    a1 = a1 * 10 + (a % 10)
    a //= 10
while b > 0:
    b1 = b1 * 10 + (b % 10)
    b //= 10
print(max(a1, b1))