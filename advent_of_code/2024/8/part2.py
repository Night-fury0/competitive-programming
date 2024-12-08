import numpy as np
from itertools import combinations
import re

lines = ""
with open("input.txt","r") as f:
    lines = f.read().strip()


values = re.findall("[A-Za-z0-9\d]{1}",lines)
unique = set(values)

lines = lines.split('\n')
lines = [list(i) for i in lines]

print(np.array(lines))

coordinates = {i:[] for i in unique}

for value in unique:
    for idx, line in enumerate(lines):
        for j,val in enumerate(line):
            if val == value:
                coordinates[value].append(tuple((idx,j)))

# for every two
antennas = set()
conditions = set()

for val, points in coordinates.items():
    pairs = list(combinations(points,2))

    print(f"pairs for {val}")
    print(pairs)

    for pair in pairs:
        point1 = pair[0]
        point2 = pair[1]
        x1, y1 = point1
        x2, y2 = point2
        m = (y2-y1)/(x2-x1)
        c = y1 - m*x1
        conditions.add((m,c))
        if tuple((1,8)) in pair and tuple((4,4)) in pair:
            print("special condition")
            print(tuple((m,c)))

print(len(conditions))

for cond in conditions:
    print(f"for condition {cond}")
    for i in range(len(lines)):
        m = cond[0]
        c = cond[1]
        y1 = m*i+c
        if i==7:
            print(y1)
        y1 = round(y1,10)
        if 0<=y1<len(lines[0]) and y1 == int(y1):
            antennas.add(tuple((i,int(y1))))
            

print(conditions)
for a in antennas:
    lines[a[0]][a[1]] = '#'

print(np.array(lines)) 
print(len(antennas))

