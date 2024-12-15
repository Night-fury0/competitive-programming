            
lines = ""
with open("input.txt","r") as f:
    lines = f.read().strip().split("\n\n")
     

box = lines[0].split("\n")
box = [list(i) for i in box]
directions = list(lines[1])

pos = ((0,0))
for i,b in enumerate(box):
    if "@" in b:
        pos = (i,b.index('@'))

while directions:
    val = directions.pop(0)
    x,y = pos
    #print(pos)
    #print(val)
    if val == "<":
        if box[x][y-1] == '.':
            box[x][y-1] = '@'
            box[x][y] = '.'
            pos = ((x,y-1))
        elif box[x][y-1] == 'O':
            idx = y - 1
            flag = False
            while 0< idx < len(box[0])-1 and box[x][idx] == 'O':
                idx -= 1
                if box[x][idx] == '.':
                    flag = True
                    break
            if flag:
                box[x][y-1] = '@'
                box[x][y] = '.'
                box[x][idx] = 'O'
                pos = ((x,y-1))

    elif val == ">":
        if box[x][y+1] == '.':
            box[x][y+1] = '@'
            pos = ((x,y+1))
            box[x][y] = '.'
        elif box[x][y+1] == 'O':
            idx = y + 1
            flag = False
            while idx < len(box[0])-1 and box[x][idx] == 'O':
                idx += 1
                if box[x][idx] == '.':
                    flag = True
                    break
            if flag:
                box[x][y+1] = '@'
                box[x][y] = '.'
                box[x][idx] = 'O'
                pos = ((x,y+1))
 
    elif val == '^': 
        if box[x-1][y] == '.':
            box[x-1][y] = '@'
            box[x][y] = '.'
            pos = ((x-1,y))
        elif box[x-1][y] == 'O':
            idx = x - 1
            flag = False
            while 0 < idx < len(box) and box[idx][y] == 'O':
                idx -= 1
                if box[idx][y] == '.':
                    flag = True
                    break
            if flag:
                box[x-1][y] = '@'
                box[x][y] = '.'
                box[idx][y] = 'O'
                pos = ((x-1,y))

    elif val == "v":
        if box[x+1][y] == '.':
            box[x+1][y] = '@'
            box[x][y] = '.'
            pos = (x+1,y)
        elif box[x+1][y] == 'O':
            idx = x + 1
            flag = False
            while 0 < idx < len(box)-1 and box[idx][y] == 'O':
                idx += 1
                if box[idx][y] == '.':
                    flag = True
                    break
            if flag:
                box[x+1][y] = '@'
                box[x][y] = '.'
                box[idx][y] = 'O'
                pos = ((x+1,y))
    #for b in box:
    #    print("".join(b))

score = 0
for i,line in enumerate(box):
    for j, val in enumerate(line):
        if val == 'O':
            score += i*100 + j
print(score)
            

 
