from collections import Counter
t = int(input())


for _ in range(t):
    n  = int(input())
    u = input()
    freq = Counter(u)
    result = ""
    curr_char = u[0]
    count = 1
    for i in range(1, len(u)):
        if u[i] == curr_char:
            count += 1;
        else:
            if count%2 == 0:
                result += curr_char*2
            else:
                result += curr_char
            curr_char = u[i]
            count = 1
    if count%2 == 0:
        result += curr_char*2
    else:
        result += curr_char
    print(result)