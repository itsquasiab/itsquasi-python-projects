import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline()
upper = ""
tmp = 0
num = 0
isnum = False
for i in s:
    #print(i)
    if i.isupper():
        upper += i
    if i.isdigit():
        tmp = tmp * 10 + int(i)
        isnum = True
    else:
        num += tmp
        tmp = 0
num += tmp
if isnum == True:
    print(f"{upper}{num}")
else:
    print(upper)