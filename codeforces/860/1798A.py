t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    max_a = max(a)
    max_b = max(b)

    if (a[-1] == max_a and b[-1] == max_b) or (a[-1] == max_b and b[-1] == max_a):
        print("Yes")
    else:
        flag = True
        for i in range(n-1):
            if a[-1] < a[i]:
                if a[-1] < b[i] or b[-1] < a[i]:
                    flag = False
                    break
            elif b[-1] < b[i]:
                if a[-1] < b[i] or b[-1] < a[i]:
                    flag = False
                    break
        if flag:
            print("Yes")
        else:
            print("No")
