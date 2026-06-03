a, b, c = map(int, input().split())
if a + b > c and a + c > b and b + c > a:
    if a == b and b == c: print("deu")
    elif a == b or b == c or c == a: print("can")
    else: 
        mx = max(a, b, c)
        mn = min(a, b, c)
        md = 0
        if a != mx and a != mn: md = a
        elif b != mx and b != mn: md = b
        else: md = c
        if (mn * mn + md * md == mx * mx): print("vuong")
        else: print("thuong")
else: print("khong")