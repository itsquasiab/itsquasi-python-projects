n = int(input())
s = 0
for i in range(0, n):
    a = int(input())
    if a % 2 == 0:
        s += a
print(s)