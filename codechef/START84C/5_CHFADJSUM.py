from bisect import bisect_left, bisect
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a.sort()
    if a[0] == a[-1] or n==2:
        print("NO")
    else:
        max_no = a[-1]
        z = a[-1] + a[-2]

        if a[-1] == a[-2]:
            no = n-bisect_left(a, max_no)
            # print("no. of times max is found: ", no )
            if 2*no-1<=n: 
                print("YES")
            else:
                print("NO")
        else:
            no1 = n - 1 - bisect_left(a,a[-2])
            if no1 < n - 1:
                print("YES")
            else:
                print("NO")

