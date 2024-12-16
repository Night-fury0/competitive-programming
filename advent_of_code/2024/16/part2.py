import copy

lines = ""
with open("input.txt","r") as f:
    lines = f.read().strip().split("\n")

start_pos = ()
end_pos = ()

for i,line in enumerate(lines):
    if "S" in line:
        start_pos = (i,line.index('S'))
    if "E" in line:
        end_pos = (i,line.index('E'))

start = (start_pos[0], start_pos[1], 0, 1, [(start_pos)], 0)
end = (end_pos[0], end_pos[1], 0,0, [], 0)

turn = {
        (0,1): [(1,-1),(-1,-1)],
        (1,0): [(-1,-1),(-1,1)],
        (0,-1): [(-1,1),(1,1)],
        (-1,0): [(1,1),(1,-1)],
}

score_dir = {}
stack = [start]
scores = {}
min_score = 7036
min_score = 11048
min_score = 143580
tiles = set()
while stack:
    val = stack.pop(0)
    x,y,dx,dy,path, score1 = val
    print(len(stack))
    if (x,y,dx,dy) not in score_dir:
        score_dir[(x,y,dx,dy)] = score1
    elif score1 > score_dir[(x,y,dx,dy)]:
        if (x,y) == (9,3):
            print(f'harbor: {score1} > {score_dir[(x,y,dx,dy)]}')
        continue
    elif min_score and score1 > min_score:
        continue
    if x == end[0] and y == end[1]:
        if score1 == min_score:
            tiles.update(path)
            print(f"reached {score1}: {len(path)}")
        if min_score is None or score1<min_score:
            min_score = score1
            tiles = set()
        
    else:
        if lines[x+dx][y+dy] != '#' and (x+dx,y+dy) not in path:
            score = score1 + 1 
            path1 = copy.deepcopy(path)
            path1.append((x+dx,y+dy))
            stack.append((x+dx, y+dy, dx,dy, path1, score))

        for r in list(turn.keys()):
            if r != (dx,dy) and (x+r[0],y+r[1]) not in path and lines[x+r[0]][y+r[1]] != '#':
                if abs(r[0]-dx) == 2 or abs(r[1]-dy) == 2:
                    score = score1 +  2001
                else:
                    score = score1 + 1001

                path1 = copy.deepcopy(path)
                path1.append((x+r[0],y+r[1]))

                if (x,y) == (11,3):
                    print(f"there {path1}")
                stack.append((x+r[0],y+r[1], r[0],r[1],path1,score))

#print(min_score)
print(len(tiles))
#print(tiles)
#lines = [list(i) for i in lines]
#
#for i in tiles:
#    lines[i[0]][i[1]] = 'O'
#
#for i in lines:
#    print("".join(i))
#        
