# https://www.codechef.com/START59D/problems/SUSSTR

t = int(input())

for i in range(t):
    n = int(input())
    S = list(input())
    T = []
    # Alice starts with index 0 in S and wants T to be smallest
    # Bob starts with index -1 in S and wants T to be largest

    index = 0
    while S:
        a = S.pop(index)
        if a == "1":
            if index == 0:
                T = T + [a]
            else:
                T = [a] + T
        elif a == "0":
            if index == 0:
                T = [a] + T
            else:
                T = T + [a]
        if index == 0:
            index = -1
        else:
            index = 0
    print("".join(T))
