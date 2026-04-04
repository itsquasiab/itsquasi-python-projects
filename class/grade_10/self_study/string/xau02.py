import sys
input = sys.stdin.readline

s = input()
c = 0
for i in s:
    if i == "a" or i == "A":
        c += 1
print(c)