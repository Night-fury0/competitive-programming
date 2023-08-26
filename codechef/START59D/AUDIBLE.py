# https://www.codechef.com/START59D/problems/AUDIBLE

n = int(input())

for i in range(n):
    a = int(input())
    if 67 <= a <= 45000:
        print("YES")
    else:
        print("NO")