from bisect import bisect, bisect_left
mod = 1000000007
n = int(input())
x_co = []
for _ in range(n):
    x,y = map(int,input().split())
    x_co.append(x)
x_co.sort()
freq = []
for i in set(x_co):
    freq.append(bisect(x_co,i) - bisect_left(x_co,i))
q = n
res = 1
for i in freq:
    while i>0:
        res = (res * i * pow(q,-1,mod)) % mod
        i -= 1
        q -= 1
print(res)
    
    