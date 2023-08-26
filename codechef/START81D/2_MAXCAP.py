# MAXCAP
t = int(input())

for i in range(t):
    a, b = [int(x) for x in input().split(" ")]
    if a * b <= 500 and a <= 8:
        print("YES")
    else:
        print("NO")