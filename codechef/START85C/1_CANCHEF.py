# CANCHEF

t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    if 15*x>=2*y:
        print("YES")
    else:
        print("NO")
    