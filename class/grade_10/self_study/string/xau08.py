import sys
input = sys.stdin.readline

s = input()
c = ""
for i in s:
    if not i.isnumeric():
        c += str(i)
print(c)