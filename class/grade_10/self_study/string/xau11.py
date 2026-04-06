import sys
input = sys.stdin.readline

s = input()
s1 = ""
for i in s:
    if (i.islower()):
        s1 += i.upper()
    elif (i.isupper()):
        s1 += i.lower()
    else: s1 += i
print(s1.strip())