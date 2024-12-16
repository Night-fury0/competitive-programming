import copy

lines = ""
with open("sample_input.txt","r") as f:
    lines = f.read().strip().split("\n")

start_pos = ()
end_pos = ()

for i,line in enumerate(lines):
    if "S" in line:
        start_pos = (i,line.index('S'))
    if "E" in line:
        end_pos = (i,line.index('E'))

start = (start_pos[0], start_pos[1], [])

score_dir = {}
stack = [start]
connected = set()

while stack:
    x,y,path = stack.pop()
    path.append((x,y))
    if x == end_pos[0] and y  == end_pos[1]:
        connected.update(path)
    else:
        if lines[x][y] == '#':
            continue
        else:
            if (x+1,y) not in path and lines[x+1][y] != '#':
                stack.append((x+1,y,path))
            if (x,y+1) not in path and lines[x][y+1] != '#':
                stack.append((x,y+1,path))
            if (x-1,y) not in path and lines[x-1][y] != '#':
                stack.append((x-1,y,path))
            if (x,y-1) not in path and lines[x][y-1] != '#':
                stack.append((x,y-1,path))

lines = [list(i) for i in lines]

for i in connected:
    lines[i[0]][i[1]] = 'O'

for i in lines:
    print("".join(i))

print(len(connected))

