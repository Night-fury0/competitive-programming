# DISTMAT

t = int(input())

for i in range(t):
    n = int(input())
    if n <= 2:
        print('-1')
    else:
        row = [0] * n
        row[0] = 1
        print(*row, sep="")
        for i in range(1, n):
            row[n-i] = 1
            print(*row, sep="")
            row[n-i] = 0

