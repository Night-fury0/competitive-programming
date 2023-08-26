
def print_two(a,b):
    print(2)
    if a-1>0:
        print(a-1,b)
        print(a,b)
    else:
        print(a,b-1)
        print(a,b)

def print_one(a,b):
    print(1)
    print(a,b)

t = int(input())
for _ in range(t):
    a,b = map(int, input().split())
    if a == 1 and b== 1: 
        print_one(a,b)
    elif a>b:
        if a%b == 0:
            print_two(a,b)
        else:
            print_one(a,b)
    else:
        if b%a == 0:
            print_two(a,b)
        else:
            print_one(a,b)

