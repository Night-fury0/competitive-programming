
permutation = []

def get_permutations(n):
    if len(permutation) == n:
        print(*[my_string[x] for x in permutation])
    else:
        for i in range(n):
            if chosen[i]: 
                continue
            chosen[i] = True
            permutation.append(i)
            get_permutations(n)
            chosen[i] = False
            permutation.pop()

my_string = "hello"
n = len(my_string)
chosen = [False] * n
get_permutations(n)
            