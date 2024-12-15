import numpy as np

lines = ""
with open("input.txt","r") as f:
    lines = f.read().strip().split("\n\n")
     

box = lines[0].split("\n")
directions = list(lines[1])
directions = [i for i in directions if i!="\n"]

pos = ((0,0))
for i,b in enumerate(box):
    box[i] = box[i].replace("#","##")
    box[i] = box[i].replace("O","[]")
    box[i] = box[i].replace(".","..")
    box[i] = box[i].replace("@","@.")
    if '@' in box[i]:
        pos = ((i,box[i].index('@')))


count = 0
while directions:
    val = directions.pop(0)

    if val == '<': 
        if box[pos[0]][pos[1]-1] in ['[',']']:
            temp = box[pos[0]][:pos[1]]
            try:
                idx = len(temp)-1-temp[::-1].index('.')
                hash_idx = len(temp)-1-temp[::-1].index('#')
                if hash_idx > idx:
                    raise ValueError
                box[pos[0]] = box[pos[0]][:idx] + box[pos[0]][idx+1:pos[1]] + '@.' + box[pos[0]][pos[1]+1:]
                pos = (pos[0],pos[1]-1)
            except ValueError as e:
                pass
        elif box[pos[0]][pos[1]-1] == '.':
            box[pos[0]] = box[pos[0]][:pos[1]-1] + '@.' + box[pos[0]][pos[1]+1:]
            pos = (pos[0],pos[1]-1)

    elif val == '>': 
        if box[pos[0]][pos[1]+1] in ['[',']']:
            temp = box[pos[0]][pos[1]+1:]
            try:
                idx = pos[1] + 1 + temp.index('.')
                if temp.index('#') < temp.index('.'):
                    raise ValueError
                box[pos[0]] = box[pos[0]][:pos[1]] + '.@' + box[pos[0]][pos[1]+1:idx]  + box[pos[0]][idx+1:]
                pos = (pos[0],pos[1]+1)
            except ValueError as e:
                pass
        elif box[pos[0]][pos[1]+1] == '.':
            box[pos[0]] = box[pos[0]][:pos[1]] + '.@' + box[pos[0]][pos[1]+2:]
            pos = (pos[0],pos[1]+1)


    elif val == 'v':
        if box[pos[0]+1][pos[1]] in ['[',']']:
            stack1 = [(pos[0]+1,pos[1])]
            stack = []
            for pos1 in stack1:
                if 0<pos1[0]<len(box)-1 and 1<pos1[1]<len(box[0])-1:
                    stack.append(pos1)
            coords = set()
            while stack:
                pos1 = stack.pop(0)
                if box[pos1[0]][pos1[1]] in ['[',']'] and pos1 not in coords:
                    coords.add(pos1)
                    if box[pos1[0]][pos1[1]] == '[':
                        stack.append((pos1[0],pos1[1]+1))
                    elif box[pos1[0]][pos1[1]] == ']':
                        stack.append((pos1[0],pos1[1]-1))
                if box[pos1[0]+1][pos1[1]] in ['[',']']:
                    stack.append((pos1[0]+1,pos1[1]))

            # move the chunk till it gets stuck
            #print(coords)
            flag = True
            for coord in coords:
                if box[coord[0]+1][coord[1]] == '#':
                    flag = False
                    break
            if flag:
                coords = sorted(coords, reverse=True)
                for coord in coords:
                    box[coord[0]+1] = box[coord[0]+1][:coord[1]] + box[coord[0]][coord[1]] + box[coord[0]+1][coord[1]+1:]
                    box[coord[0]] = box[coord[0]][:coord[1]] +  '.' + box[coord[0]][coord[1]+1:]
                box[pos[0]+1] = box[pos[0]+1][:pos[1]] + '@' + box[pos[0]+1][pos[1]+1:]
                box[pos[0]] = box[pos[0]][:pos[1]] + '.' + box[pos[0]][pos[1]+1:]
                pos = (pos[0]+1,pos[1])


        elif box[pos[0]+1][pos[1]] == '.':
            box[pos[0]+1] = box[pos[0]+1][:pos[1]] + '@' + box[pos[0]+1][pos[1]+1:]
            box[pos[0]] = box[pos[0]][:pos[1]] + '.' + box[pos[0]][pos[1]+1:]
            pos = (pos[0]+1,pos[1])


    elif val == '^':
        if box[pos[0]-1][pos[1]] in ['[',']']:
            stack1 = [(pos[0]-1,pos[1])]
            stack = []
            for pos1 in stack1:
                if 0<pos1[0]<len(box)-1 and 1<pos1[1]<len(box[0])-1:
                    stack.append(pos1)
            coords = set()
            while stack:
                pos1 = stack.pop(0)
                if box[pos1[0]][pos1[1]] in ['[',']'] and pos1 not in coords:
                    coords.add(pos1)
                    if box[pos1[0]][pos1[1]] == '[':
                        stack.append((pos1[0],pos1[1]+1))
                    elif box[pos1[0]][pos1[1]] == ']':
                        stack.append((pos1[0],pos1[1]-1))
                if box[pos1[0]-1][pos1[1]] in ['[',']']:
                    stack.append((pos1[0]-1,pos1[1]))
            # move the chunk till it gets stuck
            #print(coords)
            flag = True
            for coord in coords:
                if box[coord[0]-1][coord[1]] == '#':
                    flag = False
                    break
            if flag:
                coords = sorted(coords)
                for coord in coords:
                    box[coord[0]-1] = box[coord[0]-1][:coord[1]] + box[coord[0]][coord[1]] + box[coord[0]-1][coord[1]+1:]
                    box[coord[0]] = box[coord[0]][:coord[1]] +  '.' + box[coord[0]][coord[1]+1:]
                box[pos[0]-1] = box[pos[0]-1][:pos[1]] + '@' + box[pos[0]-1][pos[1]+1:]
                box[pos[0]] = box[pos[0]][:pos[1]] + '.' + box[pos[0]][pos[1]+1:]
                pos = (pos[0]-1,pos[1])

        elif box[pos[0]-1][pos[1]] == '.':
            box[pos[0]-1] = box[pos[0]-1][:pos[1]] + '@' + box[pos[0]-1][pos[1]+1:]
            box[pos[0]] = box[pos[0]][:pos[1]] + '.' + box[pos[0]][pos[1]+1:]
            pos = (pos[0]-1,pos[1])

    count += 1

score = 0
for i, line in enumerate(box):
    for j, val in enumerate(line):
        if val == '[':
            score += 100*i + j
print(score)
    

