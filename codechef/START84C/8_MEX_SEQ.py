mod = 10**9 + 7


def C(n,r):
    if n == 0 or r==0:
        return 1
    elif r==1:
        return n
    else:
        res = (fact[n] * pow(fact[r],-1,mod) * pow(fact[n-r],-1,mod)) % mod
        return res

# def C(n,r):
#     res = 1
#     for k in range(r):
#         res = (res*(n-k)*pow(r-k,-1,mod)) % mod
#     return res



# def no_of_seq(n):
#     if n==1:
#         return 1
#     elif n==2:
#         return 3
#     else:
#         X = 1 # for n=3
#         p = 1
#         for _ in range(4,n+1):
#             p = (p*2) % mod
#             X = (X*2 + p) % mod
#         p = (p * 2) % mod
#         return ((3*p) % mod + (2*X) % mod) % mod


def no_of_bad_seq(n,m):
    result = 0
    if m+1==n:
        result += 1
    elif m<n:
        result = pow(2,n-m-1,mod)
        # print("at index i=",m," subtract ",result)
        p = result
        for i in range(m+1,n):
            # for m-1 in i-1
            res_m = 0
            if m==1:
                res_m = 1
            else:
                j = 1
                for j in range(1,min(m,i-m)+1):
                    res_m = (res_m + (C(m,j) * C(i-m-1,j-1))%mod)% mod

            # for m in i-1
            res_m_plus_1 = 0
            if i==m+1:
                res_m_plus_1=1
            else:
                j = 1
                for j in range(1,min((m+1),i-(m+1))+1):
                    res_m_plus_1 = (res_m_plus_1 + C(m+1,j) * C(i-(m+1)-1,j-1)) % mod
            p = p*pow(2,-1,mod)
            result = (result + (p*((res_m + res_m_plus_1)%mod))%mod + (seq[n-i-1]*res_m_plus_1)%mod) % mod
            # result = (result + (p*((res_m + res_m_plus_1)%mod))%mod + (no_of_seq(n-i-1)*res_m_plus_1)%mod) % mod
            # print("at index i=",i," subtract ",result, " # ", pow(2,n-i-1,mod)," ",res_m," ",res_m_plus_1," ",no_of_seq(n-i))
    return int(result)


fact = [1] * (10**6 + 3)
seq = [1] * (10**6 + 3)
seq[0] = 1
seq[1] = 3
seq[2] = 8
no_3 = 2
no_2 = 1

for i in range(1,len(fact)):
    fact[i] = (fact[i-1] * i) % mod
    if i>=3:
        no_2 = (no_2*2 + no_3) % mod
        no_3 = (no_3*2) % mod
        seq[i] = ((3*no_3) % mod + (2*no_2) % mod) % mod



t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    if m == 0:
        print(1)
    else:
        result = (seq[n-1] - no_of_bad_seq(n,m) + 1) % mod
        if result<0:
            result += mod
        print(int(result))

