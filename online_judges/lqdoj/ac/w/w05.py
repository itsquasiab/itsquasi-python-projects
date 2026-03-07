def get_digits(n):
    x = 0
    s = 0
    while(n > 0):
        x += 1
        s += n % 10
        n //= 10
    print(x)
    print(s)

n = int(input())

get_digits(n)