import re

lines = ""
with open('input.txt', 'r') as f:
    lines = f.read().strip().split("\n\n")

direction = lines[0].strip()
path = lines[-1].split("\n")

path_dict = dict()

for i in path:
    val, left, right = re.findall(r"([A-Z0-9]{3}?)", i)
    path_dict[val] = (left, right)

stack = list(direction)
count = 0
initial = [i for i in list(path_dict.keys()) if i.endswith('A')]

print(initial)

while stack:


    print(key)
    while stack:
        if initial.endswith('Z'):
            break
        val = stack.pop(0)
        if val == 'L':
            initial = path_dict[initial][0]
            count += 1
        elif val == 'R':
            initial = path_dict[initial][-1]
            count += 1
        if len(stack) == 0:
            stack.extend(direction)




    val = stack.pop(0)
    for i in range(len(initial)):
        if val == 'L':
            initial[i] = path_dict[initial[i]][0]
        elif val == 'R':
            initial[i] = path_dict[initial[i]][-1]
    count += 1
    if len(stack) == 0:
        stack.extend(direction)
    check = all([i.endswith('Z') for i in initial])
    if check:
        break

print(count)


        
