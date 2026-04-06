import sys
input = sys.stdin.readline

s = input()
lst = s.split()
cnt = 0
for i in lst:
    if i == i[::-1]:
        cnt += 1
print(cnt)