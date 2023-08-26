# DISTOPPSUMS

t = int(input())

for i in range(t):
    n = int(input())
    a = []
    for i in range(1, n+1):
        if i <= n/2:
            a.append(str(int(n/2-i+1)))
        else:
            a.append(str(i))

    print(" ".join(a))


