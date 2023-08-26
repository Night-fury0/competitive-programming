# ONEORTWO

t = int(input())

for i in range(t):
    x, y = [int(x) for x in input().split(" ")]
    if x - y >= 2 or (x == y and y % 2 != 0) or (x - y == -1 and x % 2 != 0) or (x - y == 1 and y % 2 != 0):
        print("CHEF")
    else:
        print("CHEFINA")

