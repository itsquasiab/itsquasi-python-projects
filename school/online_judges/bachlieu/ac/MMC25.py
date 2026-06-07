import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
cnt = {}
for i in arr:
    cnt[i] = cnt.get(i, 0) + 1
print(max(cnt.values()))