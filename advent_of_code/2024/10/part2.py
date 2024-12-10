import numpy as np
lines = ""
with open("input.txt","r") as f:
    lines = f.read().strip().split("\n")

lines = [list(i) for i in lines]

trailheads = set()
for i,line in enumerate(lines):
    for j, val in enumerate(line):
        if val != '.':
            lines[i][j] = int(lines[i][j])
        if lines[i][j] == 0:
            trailheads.add(tuple((i,j)))
            
print(trailheads)
stack = []

count = 0
for pos in trailheads:
    x,y = pos
    stack.append([0,tuple((x,y))])

while stack:
    val = stack.pop()
    if val[0] == 9:
        count += 1
        continue
    x,y = val[1]
    print(val[0])
    values = []
    if 0<=x+1<len(lines) and lines[x+1][y] == val[0]+1:
        values.append([val[0]+1,tuple((x+1,y))])
    if 0<=x-1<len(lines) and lines[x-1][y] == val[0]+1:
        values.append([val[0]+1,tuple((x-1,y))])
    if 0<=y+1<len(lines[0]) and lines[x][y+1] == val[0]+1:
        values.append([val[0]+1,tuple((x,y+1))])
    if 0<=y-1<len(lines[0]) and lines[x][y-1] == val[0]+1:
        values.append([val[0]+1,tuple((x,y-1))])
    stack.extend(values)

print(count)

