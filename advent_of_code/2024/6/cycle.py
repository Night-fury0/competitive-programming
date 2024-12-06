import re
import numpy as np

lines = ""
with open("sample_input.txt","r") as f:
    lines = f.read().strip().split("\n")

original = [list(i) for i in lines]
lines = original.copy()

print(lines)

symbols = ['>','v','^','<']

initial = [0,0]
for i, line in enumerate(lines):
    for j, val in enumerate(line):
        if val in symbols:
            initial = [i,j]
            break


def solve(lines):
    outside = False
    value = lines[initial[0]][initial[1]] 
    
    while not outside:
        if value == '^':
            while (0<=initial[0]<len(lines) and 0<=initial[1]<len(lines[0])) and lines[initial[0]][initial[1]] != '#':
                lines[initial[0]][initial[1]] = 'X'
                initial[0] -= 1
            if not (0<=initial[0]<len(lines) and 0<=initial[1]<len(lines[0])):
                outside = True
                break
            value = '>'
            initial[0] += 1
        elif value == '>':
            while (0<=initial[0]<len(lines) and 0<=initial[1]<len(lines[0])) and lines[initial[0]][initial[1]] != '#':
                lines[initial[0]][initial[1]] = 'X'
                initial[1] += 1
            if not (0<=initial[0]<len(lines) and 0<=initial[1]<len(lines[0])):
                outside = True
                break
            value = 'v'
            initial[1] -= 1
        elif value == 'v':
            while (0<=initial[0]<len(lines) and 0<=initial[1]<len(lines[0])) and lines[initial[0]][initial[1]] != '#':
                lines[initial[0]][initial[1]] = 'X'
                initial[0] += 1
            if not (0<=initial[0]<len(lines) and 0<=initial[1]<len(lines[0])):
                outside = True
                break
            value = '<'
            initial[0] -= 1
        elif value == '<':
            while (0<=initial[0]<len(lines) and 0<=initial[1]<len(lines[0])) and lines[initial[0]][initial[1]] != '#':
                lines[initial[0]][initial[1]] = 'X'
                initial[1] -= 1
            if not (0<=initial[0]<len(lines) and 0<=initial[1]<len(lines[0])):
                outside = True
                break
            value = '^'
            initial[1] += 1
    total = 0
    for i in lines:
        total += i.count("X")
    return total

print(solve(lines))
