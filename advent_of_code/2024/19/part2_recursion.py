import copy

lines = ""
with open("input.txt","r") as f:
    lines = f.read().strip().split("\n\n")

patterns, designs = lines

patterns = patterns.split(", ")

designs = designs.split("\n")

memo = {}

def count(a):
    if a == "":
        return 1
    elif a in memo:
        return memo[a]
    else:
        outputs = []
        for pattern in patterns:
            if a.startswith(pattern):
                b = a.removeprefix(pattern)
                outputs.append(b)
        value = sum([count(i) for i in outputs])
        memo[a] = value
        return value

total = 0
for design in designs:
    total += count(design)

print(total)
