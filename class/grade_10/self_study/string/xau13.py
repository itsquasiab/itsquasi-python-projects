import sys
input = sys.stdin.readline

s = input()
s1 = ""
tmp = ""
for i in s:
    if i >= "0" and i <= "9":
        tmp += i
    elif tmp != "":
        s1 += tmp + "\n"
        tmp = ""
print(s1.strip())