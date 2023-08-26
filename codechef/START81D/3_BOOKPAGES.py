# BOOKPAGES

t = int(input())

for i in range(t):
    n = int(input())
    a = [int(x) % 2 for x in input().split(" ")]
    if n >= 2 and sum(a) % 2 == 0:
        print("YES")
    else:
        print("NO")

