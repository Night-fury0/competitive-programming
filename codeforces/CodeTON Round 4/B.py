t = int(input())




for _ in range(t):
    n = int(input())
    result = []
    if n&1 == 0 or n > 2199023255551:
        print(-1)
    else:
        while(n != 1):
            n = n/2
            if int(n) & 1 == 1:
                result.append(2)
            else:
                result.append(1)
            n = int(n)

        print(len(result))
        print(*result[::-1])


