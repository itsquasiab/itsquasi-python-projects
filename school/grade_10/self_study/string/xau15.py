import sys
input = sys.stdin.readline

s = input()
t = input()
s = s.strip()
t = t.strip()

cnt = 0
while s < t:
    s = s[1:] + s[0]
    t = t[1:] + t[0]
    cnt += 1
print(cnt)