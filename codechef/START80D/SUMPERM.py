# https://www.codechef.com/problems/SUMPERM

t = int(input())

for i in range(t):
    n = int(input())
    if n % 2 != 0:
        print("-1")
    else:
        initial = ["1", "2"]
        final = [(str(i+2) if i % 2 == 0 else str(i)) for i in range(2, n)]
        print(" ".join((initial + final)))
