import re
import numpy as np

lines = ""
with open("input.txt") as f:
    lines = f.read().strip().split("\n")

count = 0


matrix = [list(line) for line in lines]
transpose = [list(row) for row in zip(*matrix)]
vertical = ["".join(line) for line in transpose]

a = np.array(matrix)
print(a)

temp = 0
# horizontally
for line in lines:
    vals = re.findall("XMAS", line)
    count += len(vals)
    vals = re.findall("SAMX", line)
    count += len(vals)


print("horizontal")
print(count)


# vertically
for line in vertical:
    vals = re.findall("XMAS", line)
    count += len(vals)
    vals = re.findall("SAMX", line)
    count += len(vals)


print("vertical")
print(count)

# diagonally

def get_diagonals(matrix):
    np_matrix = np.array(matrix)
    main_diagonals = [np_matrix.diagonal(offset=i) for i in range(-np_matrix.shape[0] + 1, np_matrix.shape[1])]
    anti_diagonals = [np.fliplr(np_matrix).diagonal(offset=i) for i in range(-np_matrix.shape[0] + 1, np_matrix.shape[1])]
    return main_diagonals, anti_diagonals

main_diagonals, anti_diagonals = get_diagonals(matrix)

temp = 0
print("main_diag")
for diag in main_diagonals:
    print(diag)
    line = "".join(list(diag))

    vals = re.findall("XMAS", line)
    temp += len(vals)
    vals = re.findall("SAMX", line)
    temp += len(vals)
    
print(temp)
count += temp

temp = 0
print("anti main_diag")
for diag in anti_diagonals:
    print(diag)
    line = "".join(list(diag))

    vals = re.findall("XMAS", line)
    temp += len(vals)
    vals = re.findall("SAMX", line)
    temp += len(vals)

print(temp)
count += temp

print(count)

