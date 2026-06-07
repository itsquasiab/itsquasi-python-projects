import sys
input = sys.stdin.readline

n = int(input())
lst = []
while n > 0:
    lst.append(n % 2)
    n //= 2
for i in range(len(lst) - 1, -1, -1):
    print(lst[i], end="")