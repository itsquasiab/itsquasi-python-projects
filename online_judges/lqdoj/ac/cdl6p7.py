n = int(input())
s = 0
numbers = list(map(float, input().split()))
for i in numbers:
    s += i
print(f"{s / n:.2f}")