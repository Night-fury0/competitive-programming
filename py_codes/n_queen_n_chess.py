# no of ways n queens can be positioned in nxn chess board without being in attack range of each other
count = 0
n = 8
board = [[False]*n]*n
col = [False] * n
diag1  = [False] * (2*n-1)
diag2 = [False] * (2*n-1)

def solve(j):
    if j == n:
        return 1
    else:
        count = 0
        for i in range(n):
            if col[i] or diag1[i+j] or diag2[i-j+n-1]: continue
            else:
                col[i] = diag1[i+j]  = diag2[i-j+n-1] = True
                count += solve(j+1)
                col[i] = diag1[i+j]  = diag2[i-j+n-1] = False
        return count


print(solve(0))


