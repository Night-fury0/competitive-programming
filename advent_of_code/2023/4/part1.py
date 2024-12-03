
lines = ""
with open("input.txt") as f:
    lines = f.read().strip().split("\n")

lines = [i.strip() for i in lines]

total = 0
for line in lines:
    winning = [int(i) for i in line.split("|")[0].split(":")[-1].strip().split()]
    numbers = [int(i) for i in line.split("|")[-1].strip().split()]
    score = sum([True for i in winning if i in numbers])
    if score == 0:
        value = 0
    else:
        value = pow(2,score-1)

    total += value
print(total)

        

