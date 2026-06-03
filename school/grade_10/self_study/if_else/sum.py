a, b, c, d, e = map(int, input().split())
sum = a + b + c + d + e
mn = min(a, b, c, d, e)
mx = max(a, b, c, d, e)
print(sum - mx, sum - mn)