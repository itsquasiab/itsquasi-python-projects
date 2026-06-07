import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))
last_pos = -1
for i in range(0, n):
    if arr[i] == m:
        last_pos = i
if last_pos == -1: print("NO")
else: print(last_pos + 1)