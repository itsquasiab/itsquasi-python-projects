a, b, c = map(int, input().split())
if a > b: a, b = b, a
if a > c: a, c = c, a
if b > c: b, c = c, b
if (b - a > c - b): print(a + (c - b))
elif (b - a < c - b): print(b + (b - a))
else: print(c + (c - b))