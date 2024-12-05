
lines = ""
with open("input.txt","r") as f:
    lines = f.read().strip().split("\n")

lines = [[int(j) for j in i.split()] for i in lines]

values = []

for line in lines:
    stack = [line]
    next_line = line.copy()
    while line.count(0) != len(line):
        next_line = [line[i]-line[i-1] for i in range(1,len(line))]
        stack.append(next_line)
        line = next_line
    
    reversed_stack = stack[::-1].copy()
    for idx, value in enumerate(reversed_stack):
        if idx == 0:
            reversed_stack[idx].insert(0, 0)
        else:
            reversed_stack[idx].insert(0,reversed_stack[idx][0] - reversed_stack[idx-1][0])
    final_value = reversed_stack[-1][0]
    values.append(final_value)
        
print(values)
print(sum(values))


