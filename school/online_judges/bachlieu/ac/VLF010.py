import sys
input = sys.stdin.readline

n = int(input())

i = 1
sum = 0
while sum + i <= n:
    sum += i
    i += 1
print(sum)