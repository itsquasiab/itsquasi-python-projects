import sys
input = sys.stdin.readline

s = input()
t = input()
s = s.strip()
t = t.strip()
cnt = 0
for i in range(0, len(s) - len(t) + 1):
    if s[i:i + len(t)] == t:
        cnt += 1
print(cnt)