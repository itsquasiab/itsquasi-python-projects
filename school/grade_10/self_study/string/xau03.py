import sys
input = sys.stdin.readline

s = input()
c = ""
for i in s:
    c = max(c, i)
print(c)