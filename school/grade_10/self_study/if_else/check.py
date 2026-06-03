n = int(input())
frh1 = n // 1000
frh2 = n % 1000 // 100
sch1 = n % 100 // 10
sch2 = n % 10
if (frh1 + frh2 == 10 and sch1 + sch2 == 10): print("YES")
else: print("NO")