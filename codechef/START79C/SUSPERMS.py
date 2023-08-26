# SUSPERMS : https://www.codechef.com/problems/SUSPERMS
import concurrent.futures
from itertools import permutations
# given a perm, find if its sussy perm


n = int(input())


def beautiful_permutation(n, p):
    p = list(p)
    a = list(zip(p[:n], p[n:]))
    # checking if a is distinct
    if len(a) == len(set(a)):
        return True
    else:
        return False

# for p in set(permutations(list(range(1, n+1))*2)):
#     if beautiful_permutation(p,n):
#         count += 1
#         count = count % 269696969

with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = {executor.submit(beautiful_permutation, n, p): p for p in set(permutations(list(range(1, n+1))*2))}
    count = sum([future.result() for future in concurrent.futures.as_completed(futures)])
    # count = sum([future.result() for future in concurrent.futures.as_completed(futures)])

print(f"no. of {n} beautiful permutations: ", count * pow(2, n) % 269696969)

