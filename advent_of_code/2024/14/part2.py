from math import ceil
import numpy as np
from itertools import combinations
import copy

lines = ""
with open("input.txt","r") as f:
    lines = f.read().strip().split("\n")


size_x = 101
size_y = 103

second = 0

params = []
for line in lines:
    p,v = line.split(" ")
    p = p.split("=")[-1]
    v = v.split("=")[-1]
    px,py = map(int,p.split(","))
    vx,vy = map(int,v.split(","))
    params.append((px,py,vx,vy))

arr = [['-']*size_y for _ in range(size_x)]

for i in range(10000):
   
    for idx in range(len(params)):
        px,py,vx,vy = params[idx]
        px = px + vx
        py = py + vy
    
        if px >= size_x or px < 0:
            mult_x = px//size_x
            if 0 <= px - mult_x * (size_x ) < size_x:
                px = px - mult_x * (size_x)
    
        if py >= size_y or py < 0:
            mult_y = py//size_y
            if 0 <= py - mult_y * (size_y) < size_y:
                py = py - mult_y * (size_y)

        params[idx] = ((px,py,vx,vy))

    arr1 = copy.deepcopy(arr)    
    for pos in params:
        arr1[pos[0]][pos[1]] = '*'

    for j in arr1:
        s = "".join(j) 
        print(s)
        if "********" in s:
            print(f"{i+1} second")
            exit()

