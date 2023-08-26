import timeit

code1 = """
mod = 10**9+7
def fact(n):
    res = 1
    for i in range(1,n+1):
        res = (res*i) % mod
    return res

def C(n,r):
    return fact(n) * pow(fact(r),-1,mod) * pow(fact(n-r),-1,mod)

C(10,3)

"""
print("code1: ", timeit.timeit(code1))

code2 = """
mod = 10**9+7
def C(n,r):
    res = 1
    for k in range(r):
        res = (res*(n-k)*pow(r-k,-1,mod)) % mod
    return res

C(5,3)

"""
print("code2: ", timeit.timeit(code2))