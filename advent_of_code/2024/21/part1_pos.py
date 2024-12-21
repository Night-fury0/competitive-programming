import copy
import re

lines = ""
with open("input.txt","r") as f:
    lines = f.read().strip().split("\n")

numpad = {
    'A': 0+0j,
    '0': 0-1j ,
     '3': -1+0j,
     '2':-1-1j,
     '1':-1-2j,
     '6':-2-0j,
     '5':-2-1j,
     '4':-2-2j,
     '9':-3-0j,
     '8':-3-1j,
     '7':-3-2j
}

trans = {
    '<':0-1j,
    'v':1+0j,
    '^':-1+0j,
    '>':0+1j
}

dirpad = {
    'A': 0+0j,
    '^': 0-1j,
    '>': 1+0j,
    'v': 1-1j,
    '<': 1-2j
}

def dist(dest,source):
    return dest-source

def solve(line, pad):
    initial = 0+0j
    controls = []
    for i in line:
        control = []
        d = dist(pad[i], initial)
        h = []
        if d.imag < 0:
            h.extend(['<']*int(abs(d.imag)))
        else:
            h.extend(['>']*int(abs(d.imag)))
        v = []
        if d.real < 0:
            v.extend(['^']*int(abs(d.real)))
        else:
            v.extend(['v']*int(abs(d.real)))

        # sort control such that minimum will be possible
        if len(controls)>0 and len(h)>0 and len(v)>0 and abs(dirpad[h[0]] - dirpad[controls[-1]]) < abs(dirpad[v[0]] - dirpad[controls[-1]]):
            control.extend(h)
            control.extend(v)
        else:
            control.extend(v)
            control.extend(h)
        control.append('A')
        controls.extend(control) 
        initial = pad[i]
    
    print("".join(controls))
    return controls
 

total = 0
for line in lines:
    line = list(line)
    
    controls = solve(line, numpad)
   
    second = solve(controls, dirpad)

    controls = solve(second,dirpad)

    a = len(controls)
    b = int(re.findall("\d+","".join(line))[0])
    print(f"{line}: {a}*{b}")
    total += a*b 

print(total)

