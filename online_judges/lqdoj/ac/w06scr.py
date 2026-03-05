import math

n = int(input())
m = int(input())
gcd1 = math.gcd(n, m)
for i in range(1, gcd1 + 1):
    if m % i == 0 and n % i == 0:
        print(i, end=" ")