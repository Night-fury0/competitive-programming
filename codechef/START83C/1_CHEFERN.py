# CHEFEREN

from math import ceil

t = int(input())

for _ in range(t):
    n,a,b = map(int, input().split())
    print(ceil(n/2) * b + int(n/2) * a)



