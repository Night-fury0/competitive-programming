
lines = ""
with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

       
total = 0

for line in lines:
    test, values = line.split(":")
    test = int(test)
    values = [int(i) for i in values.strip().split()]
    operators = ["*", "+"]

    combinations = []
    incompleted = []
    completed = set()

    if len(values) == 1:
        completed.add(values[0])
    elif len(values) == 2:
        completed.add(values[0] * values[1])
        completed.add(values[0] + values[1])
    else:
        val = values
        temp = [val[0] * val[1]]
        temp.extend(val[2:])
        incompleted.append(temp)

        temp = [val[0] + val[1]]
        temp.extend(val[2:])
        incompleted.append(temp)


    while incompleted:
        val = incompleted.pop()
        if len(val) == 2:
            completed.add(val[0]*val[1])
            completed.add(val[0]+val[1])
        else:
            temp = [val[0] * val[1]]
            temp.extend(val[2:])
            incompleted.append(temp)
        
            temp = [val[0] + val[1]]
            temp.extend(val[2:])
            incompleted.append(temp)

    if test in completed:
        total += test
    print(completed)

print(total)
