t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    flag = False
    for i in range(n):
        if a[i] <= i + 1:
            flag = True
            break
    if flag:
        print("YES")
    else:
        print("NO")

            
