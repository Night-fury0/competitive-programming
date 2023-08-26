t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    m = min(a)
    s = sum(a)
    if n%2 != 0:
        if s%2 == 0:
            print("CHEFINA")
        else:
            print("CHEF")
    else:
        if m%2==0:
            if s%2==0:
                print("CHEFINA")
            else:
                print("CHEF")
        else:
            if s%2 == 0:
                print("CHEF")
            else:
                # print("CHEFINA")
                print("CHEF")



