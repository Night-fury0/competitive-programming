# OPMIN

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    count = 0
    for i in range(len(a)):
        if a[i] > min(a):
            count += 1
    print(count)