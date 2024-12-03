
lines = ""
with open("input.txt") as f:
    lines = f.read().strip().split("\n")

lines = [i.strip() for i in lines]
magnitude = [1 for i in lines]

for idx, line in enumerate(lines):
    winning = [int(i) for i in line.split("|")[0].split(":")[-1].strip().split()]
    numbers = [int(i) for i in line.split("|")[-1].strip().split()]
    value = sum([True for i in winning if i in numbers])
    for j in range(idx+1, idx+1+value):
        if j<len(lines):
            magnitude[j] += (1*magnitude[idx])

#print(magnitude)
print(sum(magnitude))

        

