n = int(input())
pos1 = -1
pos2 = -1
numbers = list(map(int, input().split()))
for i in range(0, n):
    if numbers[i] < 0:
        if pos1 == -1:
            pos1 = i + 1
        pos2 = i + 1
print(pos1, pos2)