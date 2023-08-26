# https://www.codechef.com/problems/SUBSEQINV

mod = 998244353
t = int(input())


for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    prefix_sum = a[0]
    suffix_sum = n*(n+1)/2 - a[0]
    count = 0 
    if a[0] == 1:
        count+=1
    for i in range(1,n):
        prefix_sum = prefix_sum + a[i]
        suffix_sum = suffix_sum - a[i]
        sum_till_ai = a[i]*(a[i]+1)/2
        if prefix_sum == sum_till_ai and suffix_sum == n*(n+1)/2 - sum_till_ai and a[i]==i+1:
            count+=1
    if count==n:
        print((pow(2,n,mod)-1)%mod)
    else:
        print(pow(2,count,mod))