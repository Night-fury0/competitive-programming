from math import ceil
import numpy as np

lines = ""
with open("sample_input.txt","r") as f:
    lines = f.read().strip().split("\n")

print(lines)
coords = []

size_x = 101
size_y = 103

size_x = 11
size_y = 7

for line in lines:
    p,v = line.split(" ")
    p = p.split("=")[-1]
    v = v.split("=")[-1]
    px,py = map(int,p.split(","))
    vx,vy = map(int,v.split(","))

    space = False
    #while _ in range(100):
    px = px + 100*vx
    py = py + 100*vy

    if px >= size_x or px < 0:
        mult_x = px//size_x
        if 0 <= px - mult_x * (size_x ) < size_x:
            px = px - mult_x * (size_x)
        else:
            
            print("failure")

    if py >= size_y or py < 0:
        mult_y = py//size_y
        if 0 <= py - mult_y * (size_y) < size_y:
            py = py - mult_y * (size_y)
        
        else:

            print("failure")
    coords.append((px,py))
    print((px,py))

q1 = 0
q2 = 0
q3 = 0
q4 = 0
matrix = [[0]*size_y for i in range(size_x)]
for pos in coords:
    matrix[pos[0]][pos[1]] = '*'
    if pos[0] < size_x//2 and pos[1] < size_y//2:
        q1 += 1
    if pos[0] < size_x//2 and pos[1] >= ceil(size_y/2) :
        q2 += 1
    if pos[0] >= ceil(size_x/2) and pos[1] < size_y//2:
        q3 += 1
    if pos[0] >= ceil(size_x/2) and pos[1] >=  ceil(size_y/2):
        q4 += 1

print(q1*q2*q3*q4)
print(np.array(matrix))
