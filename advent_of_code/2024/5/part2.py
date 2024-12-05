lines = ""

with open("input.txt","r") as f:
    lines = f.read().strip().split("\n\n")

rules = lines[0]
updates = lines[-1]


rules = rules.split("\n")
updates = updates.split("\n")

ordered = []
rules = [i.split("|") for i in rules]
updates = [i.strip().split(",") for i in updates]


total = 0

for i in updates:
    relevant = [j for j in rules if any([(True if k in j else False) for k in i])]

    unordered = False
    flag = True 
    rerun = True

    while rerun:
        flag = False
        for j in relevant:
            if j[0] in i and j[1] in i and i.index(j[0]) > i.index(j[1]):
                flag = True
                print(f"interchanging {j[0]} and {j[1]}")
                unordered = True
                index1 = i.index(j[0])
                index2 = i.index(j[1])
                i[index1], i[index2] = i[index2], i[index1]
                #i.pop(index2)
                #i.insert(index1-1, j[1])
                print(i)
        if not flag:
            break

    if unordered:
        print(i)
        total += int(i[len(i)//2])


print(total)


