import numpy as np
from itertools import product

lines = ""
with open ("input.txt","r") as f:
    lines = f.read().strip().split("\n\n")

locks = []
keys = []

for line in lines:
    item = line.split("\n")
    check = item[-1]
    item = [list(i) for i in item]
    item = np.array(item)
    item = item.T.tolist()
    item = [r.count("#") for r in item]
    if check == ".....":
        locks.append(item)
    else:
        keys.append(item)


count = 0
for k,v in product(locks,keys):
    val = all([k[i]+v[i]<=7 for i in range(5)])
    if val:
        count += 1
    print(f"{k}, {v} : {val}")
        
print(count)


