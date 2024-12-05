import re
import math
from functools import reduce

lines = ""
with open('input.txt', 'r') as f:
    lines = f.read().strip().split("\n\n")

direction = list(lines[0].strip())


path = lines[-1].split("\n")

path_dict = dict()

for i in path:
    val, left, right = re.findall(r"([A-Z0-9]{3}?)", i)
    path_dict[val] = (left, right)

initials = [i for i in list(path_dict.keys()) if i.endswith('A')]
finish = [i for i in list(path_dict.keys()) if i.endswith('Z')]

#initials = initials[:1]

countz = [[] for i in initials]


for idx, initial in enumerate(initials):
    count = 0
    history = [initial]
    stack = direction.copy()
    firstz = None
    while stack:
        val = stack.pop(0)
        if val == 'L':
            initial = path_dict[initial][0]
        elif val == 'R':
            initial = path_dict[initial][-1]
        count += 1

        history.append(initial)
        if firstz and initial == firstz:
            break
        elif initial.endswith('Z'):
            firstz = initial
            countz[idx].append(count)

        if len(stack)==0:
            stack = direction.copy()

    print(history)

print(countz)

numbers = [i[0] for i in countz]

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def lcm_of_list(numbers):
    return reduce(lcm, numbers)

result = lcm_of_list(numbers)

print("LCM of", numbers, "is:", result)       

