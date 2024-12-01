import re


with open('input.txt', 'r') as f:
    total = 0
    a = list()
    b = list()
    for line in f:
        s = line.split(" ")
        a.append(int(s[0]))
        b.append(int(s[-1]))
    a.sort()
    b.sort()
    
    unique = set(a)
    count_a = {num: a.count(num) for num in unique}
    count_b = {num: b.count(num) for num in unique}
    print(count_a)
    total = 0
    for i in unique:
        total += i*count_a.get(i,0)*count_b.get(i,0)
    print(total)


