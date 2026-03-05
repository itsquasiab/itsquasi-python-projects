str = input()
list = str.split()
str2 = ""
for i in list:
    str2 += " " + i
print(str2[1:])