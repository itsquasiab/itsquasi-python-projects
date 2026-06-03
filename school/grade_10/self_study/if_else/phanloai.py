a, b = map(int, input().split())
f = 0
if a >= 3 and b <= 4: print(1); f = 1
if a <= 6 and b >= 2: print(2); f = 1
if a <= 2 and b <= 3: print(3); f = 1
if f == 0: print(0)