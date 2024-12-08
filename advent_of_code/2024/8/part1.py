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

coordinates = {i:[] for i in unique}

for value in unique:
    for idx, line in enumerate(lines):
        for j,val in enumerate(line):
            if val == value:
                coordinates[value].append(tuple((idx,j)))

# for every two
antennas = set()

for val, points in coordinates.items():
    pairs = list(combinations(points,2))

    print(f"pairs for {val}")
    print(pairs)

    for pair in pairs:
        # four possibilities
        point1 = pair[0]
        point2 = pair[1]
        x1,y1 = point1
        x2,y2 = point2
        
        antenna_points = set()
        P1 = tuple(((x2 + 2 * x1) / 3, (y2 + 2 * y1) / 3))
        P2 = tuple(((2 * x2 + x1) / 3, (2 * y2 + y1) / 3))
        P3 = tuple((2 * x1 - x2, 2 * y1 - y2))
        P4 = tuple((2 * x2 - x1, 2 * y2 - y1))

        antenna_points.add(P1)
        antenna_points.add(P2)
        antenna_points.add(P3)
        antenna_points.add(P4)
        for a in antenna_points:
            if 0<=a[0]<len(lines) and 0<=a[1]<len(lines[0]) and a[0] == int(a[0]) and a[1] == int(a[1]):
                antennas.add(a)

print(antennas)
    
print(len(antennas))
