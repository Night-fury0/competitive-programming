import re

pattern = r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)"

s = ""
with open("input.txt","r") as f:
    s = f.read()

p = re.findall(pattern,s)

enabled = True
total = 0

for i in p:
    if i == "don't()":
        enabled = False
    if i == 'do()':
        enabled = True
    if enabled and i!='do()':
        pattern = r"mul\((\d+),(\d+)\)"
        matches = re.findall(pattern, i)
        for match in matches:
            x, y = match
            total += int(x)*int(y)

print(total)
