import sys
input = sys.stdin.readline

n = int(input())
neg = 0; pos = 0
a = list(map(int, input().split()))
for i in a:
    if i < 0: neg += 1
    elif i > 0: pos += 1
print (neg, pos)