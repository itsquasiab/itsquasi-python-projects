n = int(input())
s = 0
c = 0
for i in range(0, n):
    a = int(input())
    if a < 0:
        s += a
        c += 1
if s == 0:
    print(-1)
else:
    print(f"{s / c:.2f}")