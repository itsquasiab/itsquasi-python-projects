a = int(input())
b = int(input())
c = a // b
if a % b != 0:
    c += 1
print(c * b - a)