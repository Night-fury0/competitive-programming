
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

print(rules)
print(updates)

for i in updates:
    relevant = [j for j in rules if any([(True if k in j else False) for k in i])]
    flag = True
    for j in relevant:
        if j[0] in i and j[1] in i and i.index(j[0]) > i.index(j[1]):
            flag = False
            break
    if flag:
        ordered.append(i)

print(ordered)
total = 0
for i in ordered:
    total += int(i[len(i)//2])
print(total)


