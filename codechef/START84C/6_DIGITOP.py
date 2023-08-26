from bisect import bisect, bisect_left
t = int(input())

for _ in range(t):
    n,k = map(int,input().split())
    a = input().split(" ")
    b = input().split(" ")

    flag = True
    for i in range(len(a)):
        if len(a[i]) != len(b[i]):
            flag = False
            break

    a = sorted("".join(a))
    b = sorted("".join(b))
    c = ['0','1','2','3','4','5','6','7','8','9']
    positive = 0
    negative = 0
    result = 0
    for i in c:
        counta = bisect(a,i) - bisect_left(a,i)
        countb = bisect(b,i) - bisect_left(b,i)
        if counta <  countb:
            negative += countb - counta
        elif counta > countb:
            positive += counta - countb
    if negative > positive:
        result = negative - positive
    else:
        result = negative

    if flag and result <=k:
        print("YES")
    else:
        print("NO")
