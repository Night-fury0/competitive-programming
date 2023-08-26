# https://www.codechef.com/problems/SINGLEUSE

from math import ceil
t = int(input())

for i in range(t):
    h, x, y = [int(x) for x in input().split(" ")]
    n = ceil((h-y)/x) + 1
    print(n)
