# BETDEAL

t = int(input())

for i in range(t):
    a, b = [int(x) for x in input().split(" ")]
    cost_first = (100 - a) * 100
    cost_second = (100 - b) * 200
    if cost_first < cost_second:
        print("FIRST")
    elif cost_first == cost_second:
        print("BOTH")
    else:
        print("SECOND")


