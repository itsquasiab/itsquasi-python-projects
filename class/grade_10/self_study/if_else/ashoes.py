a, b = map(int, input().split())
mn = min(a, b)
mx = max(a, b) - mn
print(mn, mx // 2)