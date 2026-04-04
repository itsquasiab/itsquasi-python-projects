import sys
input = sys.stdin.readline

s = input()
c = 0
for i in s:
    if i >= "0" and i <= "9":
        c += int(i)
print(c)