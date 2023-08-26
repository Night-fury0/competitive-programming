import itertools
import numpy as np

# highest common factor or greatest common divisor
# hcf: find the smallest difference between any pair of nos. and check the highest factor of that no. that divides all

a = [3,7,9,12,14]

n = len(a)

min_diff = max(a) - min(a)
hcf = 1

for b in list(itertools.pairwise(sorted(a))):
    diff = b[1]-b[0]
    if diff < min_diff:
        min_diff = diff

for i in range(min_diff, 0, -1):
    if min_diff % i == 0 and not any([x % i for x in a]):
        hcf = i
        print(f"HCF of {a}: {i}")
        break

# to find lcm - search from the largest no. in steps of hcf till product of all no.s to find lcm

prod = np.prod(a)
lcm = prod

for i in range(max(a), prod, hcf):
    if not any([i % x for x in a]):
        lcm = i
        break
print(f"LCM of {a}: {lcm}")

# further:  how to make it work for decimals = find max zeroes after decimal point, multiple 10s and make it int,
#           then divide obtained hcf, lcm by power of 10
