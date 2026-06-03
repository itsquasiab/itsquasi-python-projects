a, b = map(float, input().split())
print(int(a // b + (a % b != 0)))