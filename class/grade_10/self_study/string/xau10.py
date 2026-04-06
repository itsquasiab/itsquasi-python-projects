import sys
input = sys.stdin.readline

s = input()
st = s.split()
s1 = ""
for i in st:
    s1 += i + " "
print(s1.strip())