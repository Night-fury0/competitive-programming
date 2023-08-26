# MATDIF
from math import ceil, floor

t = int(input())

for _ in range(t):
    n = int(input())
    no_even = 1
    no_odd = (n * ceil(n/2)) + 1
    for i in range(n):
        if i % 2 == 0:
            diff = ceil(n/2)
            print(*range(no_even, no_even+(diff*(n-1))+1, diff))
            no_even += 1
        else:
            diff = floor(n/2)
            print(*range(no_odd, no_odd+(diff*(n-1))+1, diff))
            no_odd += 1