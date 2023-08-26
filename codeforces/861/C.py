t = int(input())

for _ in range(t):
    l, r = input().split(" ")
    result = l
    result_luck = int(max([*str(l)])) - int(min([*str(l)]))
    for i in range(int(l),int(r)+1):
        luck = int(max([*str(i)])) - int(min([*str(i)]))
        if luck == 9:
            result = i
            break
        elif luck > result_luck:
            result = i
            result_luck = luck
    print(result)