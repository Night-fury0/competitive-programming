from bisect import bisect, bisect_left
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a1 = a[:]
    a1.sort()
    no_liars = 0
    result = -1
    for i in set(a):
        no = bisect(a1,i) - bisect_left(a1,i)
        if i >= n:
            no_liars+=no
        if no <= n-i:
            result = n-no
            break
    if result == -1 and no_liars > 0:
        result = no_liars
    print(result)
