import sys
input = sys.stdin.readline

def findgcd(a, b):
    if b == 0: return a
    else: return findgcd(b, a % b)

m, n = map(int, input().split())
print(findgcd(m, n))
