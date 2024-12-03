import re

pattern = r"mul\((\d{1,3}),\s*(\d{1,3})\)"
total = 0

with open('input.txt', 'r') as f:
    for line in f:
        matches = re.findall(pattern, line.strip())
        for i in matches:
            #print(i)
            total += int(i[0]) * int(i[1])
print(total)
