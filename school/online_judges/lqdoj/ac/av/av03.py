n = int(input())
s = 0
c = 0
for i in range(0, n):
    a = int(input())
    if a > 0:
        s += a
        c += 1
print(c, s)