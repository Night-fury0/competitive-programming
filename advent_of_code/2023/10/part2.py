import numpy as np
import re
import copy

lines = ""

with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

start_position = []
for idx, line in enumerate(lines):
    if 'S' in line:
        start_position = tuple((idx, line.index('S')))

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

matrix = [[0] * len(lines[0]) for i in range(len(lines)) ]

path = paths[0]
print(path)

horizontal_edge_cases = ['-']


for i, line in enumerate(lines):
    for j, val in enumerate(line):
        if tuple((i,j)) not in path:
            lines[i][j] = "."

point1 = path[-1]
point2 = path[0]
point3 = path[1]

second_diff = tuple((point1[0] - point2[0], point1[1] - point2[1]))
first_diff = tuple((point2[0] - point3[0], point2[1] - point3[1]))
print("diff")
print(second_diff)
print(first_diff)

if (first_diff == ((-1,0)) and second_diff == ((0,1))) or (second_diff == ((1,0)) and first_diff == ((0,-1))):
    lines[start_position[0]][start_position[1]] = 'F'
elif (first_diff == ((1,0)) and second_diff == ((0,1))) or (second_diff == ((-1,0)) and first_diff == ((0,-1))):
    lines[start_position[0]][start_position[1]] = 'L'
elif (first_diff == ((1,0)) and second_diff == ((0,-1))) or (second_diff == ((-1,0)) and first_diff == ((0,1))):
    lines[start_position[0]][start_position[1]] = 'J'
elif (first_diff == ((-1,0)) and second_diff == ((0,-1))) or (second_diff == ((1,0)) and first_diff == ((0,1))):
    lines[start_position[0]][start_position[1]] = '7'
elif (first_diff == ((-1,0)) and second_diff == ((-1,0))) or (second_diff == ((1,0)) and first_diff == ((1,0))):
    lines[start_position[0]][start_position[1]] = '|'
elif (first_diff == ((0,1)) and second_diff == ((0,1))) or (second_diff == ((0,-1)) and first_diff == ((0,-1))):
    lines[start_position[0]][start_position[1]] = '-'
else:
    Exception("invalid S case")

total = 0

for i, line in enumerate(lines):

    if i == start_position[0]:
        print("for row containing S")
    for j, val in enumerate(line):
        if tuple((i,j)) not in path:
            s = "".join(lines[i][j:])
            count  = re.findall(r"\||L-*7|F-*J",s)
            if len(count) % 2 != 0:
                total += 1
                if i == start_position[0]:
                    print(tuple((i,j)))

print(total)
print(np.array(lines))

         




