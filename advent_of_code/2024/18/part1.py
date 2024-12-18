import numpy as np
import copy

lines = ""
with open("input.txt","r") as f:
    lines = f.read().strip().split("\n")

r_size = 71
c_size = 71
#r_size = 7
#c_size = 7
a = [[0]*c_size for _ in range(r_size)]

for i in range(1024):
    x,y = map(int,lines[i].split(","))
    a[y][x] = 'X'

stack = [(0,0,0)]
possible = []
memo = dict()

while stack:
    x,y,score = stack.pop(0)
    if (x,y) not in memo:
        memo[(x,y)] = score
    elif memo[(x,y)] > score: 
        memo[(x,y)] = score 
    else:
        continue
    if a[x][y] == 'X':
        continue
    if 0 <= x-1 < r_size and a[x-1][y]!='X':
        stack.append((x-1,y, score+1))
    if 0 <= x+1 < r_size and a[x+1][y]!='X':
        stack.append((x+1,y, score+1))
    if 0 <= y-1 < c_size and a[x][y-1]!='X':
        stack.append((x,y-1, score+1))
    if 0 <= y+1 < c_size and a[x][y+1]!='X':
        stack.append((x,y+1, score+1))
    if x == r_size-1 and y == c_size-1:
        #print("reached")
        possible.append(score)
print(min(possible))        

