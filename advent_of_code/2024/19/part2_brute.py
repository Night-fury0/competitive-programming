import copy

lines = ""
with open("input.txt","r") as f:
    lines = f.read().strip().split("\n\n")

patterns, designs = lines

patterns = patterns.split(", ")

designs = designs.split("\n")

memo = {}

stack = copy.deepcopy(designs)
count = 0
while stack:
    print(count)
    #print(len(stack))
    d = stack.pop(0)
    if d in memo:
        outcomes, count_d = memo[d]
        count+=count_d
    else:
        change = False
        count_d = 0
        inner_stack = [d]
        while inner_stack:
            print(f"len of inner stack: {len(inner_stack)}")
            d1 = inner_stack.pop(0)
            for pattern in patterns:
                d2 = copy.deepcopy(d1)
                if d2.startswith(pattern):
                    change = True
                    d2 = d2.removeprefix(pattern)
                    if d2 == "":
                        possible = True
                        count_d += 1
                    else:
                        if d2 not in inner_stack:
                            inner_stack.append(d2)
        memo[d] = count_d
        count += count_d
print(count)
