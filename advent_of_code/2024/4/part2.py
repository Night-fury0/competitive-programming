import re
import numpy as np

lines = ""
with open("input.txt") as f:
    lines = f.read().strip().split("\n")

lines = [list(line) for line in lines]
matrix = np.array(lines)


def get_3x3_subarrays(matrix):
    rows, cols = matrix.shape
    subarrays = []
    
    for i in range(rows - 2): 
        for j in range(cols - 2): 
            subarray = matrix[i:i+3, j:j+3]
            subarrays.append(subarray)
    
    return subarrays

subarrays = get_3x3_subarrays(matrix)

print(len(subarrays))

count = 0

for s in subarrays:
    diagonal = s.diagonal()
    diagonal = "".join(diagonal)
    
    anti_diagonal = s[np.arange(s.shape[0]), s.shape[1] - 1 - np.arange(s.shape[0])]
    anti_diagonal = "".join(anti_diagonal)
    allowed  = ['MAS','SAM'] 

    if diagonal in allowed and anti_diagonal in allowed:
        count += 1

print(count)



