import math
lines = ""

times = []
distances = []

with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

times = lines[0].split(":")[-1].split()
times = [int(i) for i in times]
distances = lines[1].split(":")[-1].split()
distances = [int(i) for i in distances]

values = []
for i in range(len(times)):
    d = distances[i]
    t = times[i]
    possible = 0
    for j in range(1, t+1):
        value = (t-j)*j
        if value > d:
            possible += 1
    values.append(possible)

print(math.prod(values))





