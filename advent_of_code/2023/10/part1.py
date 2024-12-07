import numpy as np
import copy

lines = ""

with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

start_position = []
for idx, line in enumerate(lines):
    if 'S' in line:
        start_position = tuple((idx, line.index('S')))

print(start_position)


paths = []

# starting position
# direction [(1,0), (-1,0), (0,1), (0,-1)]

# if in that direction, movement is not possible end path
# have four paths like this

lines = [list(i) for i in lines]

def find_path(start_position, direction):
    path = []
    pos = copy.deepcopy(start_position)
    flag = True
    while tuple((pos[0],pos[1])) not in path:
        if lines[pos[0]][pos[1]] == '.' \
                or (direction == tuple((1,0)) and lines[pos[0]][pos[1]] in ['F','7','-']) \
                or (direction == tuple((-1,0)) and lines[pos[0]][pos[1]] in ['L','J','-']) \
                or (direction == tuple((0,1)) and lines[pos[0]][pos[1]] in ['L','F','|']) \
                or (direction == tuple((0,-1)) and lines[pos[0]][pos[1]] in ['J','7','|']):
            flag = False
            break
        path.append((pos[0],pos[1]))
        if direction == tuple((0,0)):
            flag = False
            break
        if lines[pos[0]][pos[1]] == 'L':
            if direction == tuple((1,0)):
                direction = tuple((0,1))
            elif direction == tuple((0,-1)):
                direction = tuple((-1,0))
            else:
                direction = tuple((0,0))
        elif lines[pos[0]][pos[1]] == 'J':
            if direction == tuple((1,0)):
                direction = tuple((0,-1))
            elif direction == tuple((0,1)):
                direction = tuple((-1,0))
            else:
                direction = tuple((0,0))
        elif lines[pos[0]][pos[1]] == 'F':
            if direction == tuple((-1,0)):
                direction = tuple((0,1))
            elif direction == tuple((0,-1)):
                direction = tuple((1,0))
            else:
                direction = tuple((0,0))
        elif lines[pos[0]][pos[1]] == '7':
            if direction == tuple((-1,0)):
                direction = tuple((0,-1))
            elif direction == tuple((0,1)):
                direction = tuple((1,0))
            else:
                direction = tuple((0,0))
        pos = tuple((pos[0] + direction[0], pos[1] + direction[1]))
        if not (0<=pos[0]<len(lines) and 0<=pos[1]<len(lines[0])):
            flag = False
            break
    
    if flag:
        return path
    else:
        return None

paths = []

# to up
direction = tuple((-1,0))
value = find_path(start_position, direction)
paths.append(value)

# to below
direction = tuple((1,0))
value = find_path(start_position, direction)
paths.append(value)

# to right
direction = tuple((0,1))
value = find_path(start_position, direction)
paths.append(value)

# to left
direction = tuple((0,-1))
value = find_path(start_position, direction)
paths.append(value)

paths = [path for path in paths if path is not None]

shortest = []
length = len(paths[0])
if length % 2 != 0:
    print(length//2 + 1)
else:
    print(length//2)



