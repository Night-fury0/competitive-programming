t = int(input())
for _ in range(t):
    n,c,d = map(int,input().split())
    a = list(map(int,input().split()))
    a = list(set(a))
    duplicates = n-len(a)
    result = duplicates * c
    a.sort()
    consecutive = a[0]
    gaps_to_fill = 0
    n= len(a)
    for i in range(n):
        if i!= 0:
            if a[i] != a[i-1] + 1:
                gaps_to_fill = a[i] - a[i-1] - 1
                # print("current ", a[i]," previous ", a[i-1])
                # print("at ", i, " ",gaps_to_fill * d, "or ", (n-i) * c)
                if (gaps_to_fill * d) < (n-i) * c:
                    result += gaps_to_fill * d
                else:
                    result += (n-i) * c
                    break
        else:
            if a[i] != 1:
                gaps_to_fill = a[i] - 1
                # print("at ", i, " ",gaps_to_fill * d, "or ", (n-i) * c + d)
                if (gaps_to_fill * d) < (n-i) * c + d:
                    result += gaps_to_fill * d
                else:
                    result += (n-i)*c + d
                    break

    print(min(result, c*(n+ duplicates) + d))
    
