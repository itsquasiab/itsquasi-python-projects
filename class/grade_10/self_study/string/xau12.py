import sys
input = sys.stdin.readline

a = input()
b = input()
a = a.strip()
b = b.strip()
if a > b: print(1)
elif a < b: print(-1)
else: print(0)