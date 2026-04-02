a, b, c = map(int, input().split())
x = min(a, b, c)
y = 0
z = max(a, b, c)
if a != x and a != z: y = a
if b != x and b != z: y = b
if c != x and c != z: y = c
print(max(y - x, z - y) - 1)