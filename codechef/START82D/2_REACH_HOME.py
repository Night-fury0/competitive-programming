# REACH_HOME

t = int(input())

for _ in range(t):
    x, y = map(int, input().split())
    if 5 * x >= y:
        print("YES")
    else:
        print("NO")
