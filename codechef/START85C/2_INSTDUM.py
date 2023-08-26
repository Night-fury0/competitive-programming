# INSTDUM 

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    sum = 0
    count = 0
    for i in range(len(a)):
        sum += a[i]
        if sum == i+1:
            count += 1
    print(count)
    