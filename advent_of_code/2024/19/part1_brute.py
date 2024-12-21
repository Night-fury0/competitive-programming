import copy

lines = ""
with open("input.txt","r") as f:
    lines = f.read().strip().split("\n\n")

patterns, designs = lines

patterns = patterns.split(", ")

designs = designs.split("\n")

memo = {i: False for i in designs}

count = 0
idx = 0
for design in designs[:1]:
    print(f"at idx {idx}")
    idx += 1
    possible = False
    design1 = list(design)
    possibilities = [[[],design1]]
    while possibilities:
        print(len(possibilities))
        case,rest = possibilities.pop(0)

        if  len(case)>0 and len(rest) == 0:
            possible = True
            print(f"{case} is possible")
            count+=1
            break

        if len(case) > 0 and len(rest)>0:
            case1 = copy.deepcopy(case)
            p = case1.pop()
            rest1 = copy.deepcopy(rest)
            val = copy.deepcopy(p)
            while rest1:
                latest = rest1.pop(0)
                val = val + latest
                #print(val)
                if val in patterns:
                    #print(f"happened for {val} at {rest1} for condition {case},{rest}")
                    #print(f"happened for {val} for condition {case}")
                    case1 = copy.deepcopy(case)[:-1]
                    case1.extend([val])
                    possibilities.append([case1,copy.deepcopy(rest1)])
                if len(val[len(p):])>0 and val[len(p):] in patterns:
                    #print(f"2nd happened for {val[1:]} at {rest1} for condition {case},{rest}")
                    #print(f"2nd happened for {val[1:]} for condition {case}")
                    case1 = copy.deepcopy(case)
                    case1.extend([val[len(p):]])
                    possibilities.append([case1,copy.deepcopy(rest1)])

        elif len(case) == 0 and len(rest) > 0:
            rest1 = copy.deepcopy(rest)
            val = ''
            while rest1:
                latest = rest1.pop(0)
                val = val + latest
                if val in patterns:
                    case1 = copy.deepcopy(case)
                    case1.extend([val])
                    possibilities.append([case1,copy.deepcopy(rest1)])

                
print(count)
