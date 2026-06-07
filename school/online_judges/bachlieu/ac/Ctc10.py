import sys
input = sys.stdin.readline

a = int(input())
b = int(input())
if a % 2 == 0: a += 1
sum = 0
for i in range(a, b + 1, 2): sum += i
print(sum)