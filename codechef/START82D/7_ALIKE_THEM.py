# ALIKE_THEM

MOD = 1000000007
T = int(input())

# https://www.codechef.com/problems/ALIKE_THEM
# https://www.codechef.com/viewsolution/92840074

for _ in range(T):
    N, M = map(int, input().split())
    P = list(map(int, input().split()))
    A = list(map(int, input().split()))
    count = 0
    flag = True
    no_zero = A.count(0)
    non_zero = 0
    non_zero_flag = False
    for i in range(N):
        A[i] = A[P[i]-1]
        if A[i] == 0:
            if P[i]-1 >= i:
                count += 1
        else:
            if not non_zero_flag:
                non_zero = A[i]
                non_zero_flag = True
            elif non_zero != A[i] and non_zero_flag:
                flag = False
                break
    power = no_zero - (count if non_zero_flag else count-1)
    if not flag:
        print(0)
    else:
        result = 1
        while power != 0:
            result = (result * M) % MOD
            power -= 1
        print(result)






