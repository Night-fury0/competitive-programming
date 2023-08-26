# FIND_X
from math import lcm
t = int(input())


def hcf(a, b):
    if b == 0:
        return a
    return hcf(b, a % b)


for _ in range(t):
    a, b, c, d = map(int, input().split())
    if (a+1)%b == (c+1)%d:
        print(1)
    else:
        print(int(lcm(b, d) - a%b))