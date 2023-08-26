from bisect import bisect, bisect_left
t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    a1 = a[:]
    a1.sort()
    count = 0
    for i in set(a):
        no = bisect(a1,i) - bisect_left(a1,i)
        count += int((no*(no-1))/2)
    print(int(n*(n+1)/2) - n - count)
        
    
    
    