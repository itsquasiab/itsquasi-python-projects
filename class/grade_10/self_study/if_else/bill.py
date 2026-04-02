n = int(input())
sum = 0
if (n <= 100): print(n * 2000)
else: sum += 100 * 2000; n -= 100
if (n <= 100): print(sum + n * 3000)
else: sum += 100 * 3000; n -= 100
if (n <= 100): print(sum + n * 5000)
else: sum += 100 * 5000; n -= 100; print(sum + n * 10000)