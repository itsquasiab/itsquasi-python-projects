n, m = map(int, input().split())
for i in range(1, min(m, n) + 1):
    if m % i == 0 and n % i == 0:
        print(i, end=" ")