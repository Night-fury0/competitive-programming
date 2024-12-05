import re

lines = ""
with open('input.txt', 'r') as f:
    lines = f.read().strip().split("\n\n")

direction = lines[0].strip()
path = lines[-1].split("\n")

path_dict = dict()

for i in path:
    val, left, right = re.findall(r"([A-Z]{3}?)", i)
    path_dict[val] = (left, right)

stack = list(direction)
initial = 'AAA'
count = 0

while stack:
    if initial == 'ZZZ':
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

print(count)


        

    





