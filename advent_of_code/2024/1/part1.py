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
    print(a)
    print(b)
    print(len(a))
    print(len(b))
    total = 0
    for i in range(len(a)):
        total += abs(a[i]-b[i]) 
    print(total)


