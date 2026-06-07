import sys
import math
input = sys.stdin.readline

def check_prime(n):
    if n == 2 or n == 3: return True
    if n <= 4 or n % 2 == 0 or n % 3 == 0: return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0: return False
    return True

n = int(input())
if check_prime(n): print("YES")
else: print("NO")