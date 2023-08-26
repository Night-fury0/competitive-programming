t = int(input())

# TIME LIMIT EXCEEDED
# https://codeforces.com/contest/1798/problem/B

for _ in range(t):
    N = []
    A = []
    result = []
    m = int(input())
    for mi in range(m):
        N.append(int(input()))
        A = A + list(map(int, input().split()))
    left_no = 0
    for i in range(len(N)):
        if i == len(N) - 1:
            result.append(A[-1])
            break
        left = set(A[left_no:left_no + N[i]]).difference(A[left_no + N[i]:])

        if left:
            result.append(left.pop())
        else:
            result = [-1]
            break
        left_no += N[i]
    print(*result)


