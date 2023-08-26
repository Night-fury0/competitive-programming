# MAKE_AB_SAME

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    flag = True
    if a[0] != b[0] or a[-1] != b[-1]:
        flag = False
    elif 1 not in a and 1 in b:
        flag = False
    elif 0 not in a and 0 in b:
        flag = False
    else:
        for i in range(1, len(a) - 1):
            if a[i] == 1 and b[i] == 0:
                flag = False
                break
    if flag:
        print("YES")
    else:
        print("NO")



    # elif any([True for i in range(1, len(a) - 1) if a[i]])
    #     for i in range(1, len(a) - 1):
    #         if a[i] == 0 and b[i] == 1:
    #             if 1 not in (a[:i] + a[i+1:]):
    #                 flag = False
    #                 break


