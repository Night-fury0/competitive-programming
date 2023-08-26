# https://www.codechef.com/problems/EQUALELE

import collections

t = int(input())

for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    max_count = max(dict(collections.Counter(a)).values())
    print(len(a) - max_count)


