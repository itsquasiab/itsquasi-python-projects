a, b, c = map(int, input().split())
if a + b + c == 180:
    if a == 90 or b == 90 or c == 90: print("VUONG")
    elif a == b == c: print("DEU")
    elif a == b or b == c or c == a: print("CAN")
    else: print("THUONG")
else: print("0")