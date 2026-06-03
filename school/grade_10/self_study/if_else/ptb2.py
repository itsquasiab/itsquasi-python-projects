import math

a, b, c = map(int, input().split())
delta = b * b - 4 * a * c
if delta > 0:
    x1 = (-b + round(math.sqrt(delta))) // 2 * a
    x2 = (-b - round(math.sqrt(delta))) // 2 * a
    print(x1, x2)
elif delta == 0:
    print(-b // (2 * a))
else: print("PT Vo nghiem")