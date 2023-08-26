# https://www.codechef.com/problems/RUNCOMPARE

t = int(input())

for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    b = [int(x) for x in input().split(" ")]
    both_happy = sum([True for i in range(n) if max(a[i], b[i])/min(a[i], b[i]) <= 2])
    print(both_happy)
