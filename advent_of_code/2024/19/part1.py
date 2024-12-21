import copy

lines = ""
with open("input.txt","r") as f:
    lines = f.read().strip().split("\n\n")

patterns, designs = lines

patterns = patterns.split(", ")
print(patterns)

designs = designs.split("\n")

count = 0
idx = 0
for design in designs:
    print(design)
    possible = False
    stack = [design]
    while stack:
        print(stack)
        d = stack.pop(0)
        change = False
        for pattern in patterns:
            d1 = copy.deepcopy(d)
            if d.startswith(pattern):
                change = True
                if len(d1) == len(pattern):
                    d1 = ""
                else:
                    d1=d1[len(pattern):]
                if len(d1) == 0:
                    possible = True
                    count += 1
                    break
                if d1 not in stack:
                    stack.append(d1)
        if possible:
            count+=1
            break
        if not change:
            continue

                
print(count)
