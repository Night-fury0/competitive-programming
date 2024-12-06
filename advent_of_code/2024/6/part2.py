import re
import copy
import numpy as np

lines = ""
with open("input.txt","r") as f:
    lines = f.read().strip().split("\n")

original = [list(i) for i in lines]
lines = copy.deepcopy(original)


symbols = ['>','v','^','<']

initial = [0,0]
for i, line in enumerate(lines):
    for j, val in enumerate(line):
        if val in symbols:
            initial = [i,j]
            break

initial_position = tuple((initial[0], initial[1]))

outside = False

value = lines[initial[0]][initial[1]] 

variations = []
positions = []


while not outside:
    if value == '^':
        while (0<=initial[0]<len(lines) and 0<=initial[1]<len(lines[0])) and lines[initial[0]][initial[1]] != '#':
            lines[initial[0]][initial[1]] = 'X'
            positions.append(tuple((initial[0],initial[1])))
            initial[0] -= 1
        if not (0<=initial[0]<len(lines) and 0<=initial[1]<len(lines[0])):
            outside = True
            break
        value = '>'
        initial[0] += 1
        lines[initial[0]][initial[1]] = '*'
    elif value == '>':
        while (0<=initial[0]<len(lines) and 0<=initial[1]<len(lines[0])) and lines[initial[0]][initial[1]] != '#':
            lines[initial[0]][initial[1]] = 'X'
            positions.append(tuple((initial[0],initial[1])))
            initial[1] += 1
        if not (0<=initial[0]<len(lines) and 0<=initial[1]<len(lines[0])):
            outside = True
            break
        value = 'v'
        initial[1] -= 1
        lines[initial[0]][initial[1]] = '*'
    elif value == 'v':
        while (0<=initial[0]<len(lines) and 0<=initial[1]<len(lines[0])) and lines[initial[0]][initial[1]] != '#':
            lines[initial[0]][initial[1]] = 'X'
            positions.append(tuple((initial[0],initial[1])))
            initial[0] += 1
        if not (0<=initial[0]<len(lines) and 0<=initial[1]<len(lines[0])):
            outside = True
            break
        value = '<'
        initial[0] -= 1
        lines[initial[0]][initial[1]] = '*'
    elif value == '<':
        while (0<=initial[0]<len(lines) and 0<=initial[1]<len(lines[0])) and lines[initial[0]][initial[1]] != '#':
            lines[initial[0]][initial[1]] = 'X'
            positions.append(tuple((initial[0],initial[1])))
            initial[1] -= 1
        if not (0<=initial[0]<len(lines) and 0<=initial[1]<len(lines[0])):
            outside = True
            break
        value = '^'
        initial[1] += 1
        lines[initial[0]][initial[1]] = '*'

positions = list(set(positions[1:]))
positions.remove(initial_position)

for pos in positions:
    variation = copy.deepcopy(original)
    variation[pos[0]][pos[1]] = '#'
    variations.append(variation)


def solve(x,y,variation):
    outside = False
    visited_positions = set() 
    value = variation[x][y] 

    while not outside:
        current_position = (x, y, value)
        #print(current_position)
        if current_position in visited_positions:
            return None 
        
        visited_positions.add(current_position)

        if value == '^':
            while (0 <= x < len(variation) and 0 <= y < len(variation[0])) and variation[x][y] != '#':
                variation[x][y] = 'X'
                x -= 1
            if not (0 <= x < len(variation) and 0 <= y < len(variation[0])):
                outside = True
                break
            value = '>' 
            x += 1 
        elif value == '>':
            while (0 <= x < len(variation) and 0 <= y < len(variation[0])) and variation[x][y] != '#':
                variation[x][y] = 'X'
                y += 1
            if not (0 <= x < len(variation) and 0 <= y < len(variation[0])):
                outside = True
                break
            value = 'v' 
            y -= 1  
        elif value == 'v':
            while (0 <= x < len(variation) and 0 <= y < len(variation[0])) and variation[x][y] != '#':
                variation[x][y] = 'X'
                x += 1
            if not (0 <= x < len(variation) and 0 <= y < len(variation[0])):
                outside = True
                break
            value = '<' 
            x -= 1 
        elif value == '<':
            while (0 <= x < len(variation) and 0 <= y < len(variation[0])) and variation[x][y] != '#':
                variation[x][y] = 'X'
                y -= 1
            if not (0 <= x < len(variation) and 0 <= y < len(variation[0])):
                outside = True
                break
            value = '^'  
            y += 1  

    #print("visited_positions: ",visited_positions)
    return variation

count = 0
total = 0

for variation in variations:
    total += 1
    print(f"processing {total} of {len(variations)}")
    value = solve(initial_position[0],initial_position[1],variation)
    #print(initial_position)
    if value is None:
        count += 1
    else:
        #print(np.array(value))
        pass

print(count)
