import math
lines = ""

times = []
distances = []

with open("input.txt", "r") as f:
    lines = f.read().strip().split("\n")

times = lines[0].split(":")[-1].split()
distances = lines[1].split(":")[-1].split()

t = int("".join(times))
d = int("".join(distances))

A = (t + math.sqrt(t*t-4*d))/2
B = (t - math.sqrt(t*t-4*d))/2

A, B = sorted([A,B])

start = math.ceil(A)
end = math.floor(B)

if end > d:
    end = d
if start < 0:
    start = 1

values = list(range(start, end + 1))

def equation(i, t, d):
    return t*i - i*i > d

print(equation(values[0], t, d))
print(len(values))

