t = int(input())
 
for _ in range(t):
    n, m = map(int, input().split())
    c = []
    for j in range(n):
        a = list(map(int, input().split()))
        c.append(a)
    
    sum = 0
    for i in range(m):
        b = [c[x][i] for x in range(n)]
        b.sort(reverse=True)
        result = 0
        positive = n-1
        negative = 0
        for j in range(n):
            result += positive * b[j] - negative * b[j]
            positive -= 1
            negative += 1
        sum += result
    print(sum)
