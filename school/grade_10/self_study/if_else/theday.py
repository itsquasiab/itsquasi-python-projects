a, b, c = map(int, input().split())
if (a == 31):
    a = 1
    if (b == 12):
        b = 1
        c += 1
elif (a == 30 and b == {4, 6, 9, 11}):
    a = 1
    b += 1
elif (a == 29 and b == 2):
    a = 1
    b += 1
elif (a == 28 and b == 2):
    if ((c % 4 == 0 and c % 100 != 0) or c % 400 == 0): a += 1
    else: a = 1; b += 1
else: a += 1
print(a, b, c)