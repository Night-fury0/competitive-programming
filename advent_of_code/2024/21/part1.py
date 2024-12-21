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
    controls = [[]]
    for i in line:
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

        if not (len(h)>0 and len(v)>0):
            if len(h)>0:
                control = []
                control.extend(h)
                control.append('A')
                controls = [k+control for k in controls]
            else:
                control = []
                control.extend(v)
                control.append('A')
                controls = [k+control for k in controls]
        else:
            controls1 = copy.deepcopy(controls)
            controls2 = copy.deepcopy(controls)
            flag1 = False
            if initial+d.real in list(pad.values()):
                flag1 = True
                control = []
                control.extend(v)
                control.extend(h)
                control.append('A')
                controls1 = [k+control for k in controls1]
                
            flag2 = False
            if initial+d-d.real in list(pad.values()):
                flag2 = True
                control = []
                control.extend(h)
                control.extend(v)
                control.append('A')
                controls2 = [k+control for k in controls2]

            if flag1 and flag2:
                controls = controls1 + controls2
            elif flag1:
                controls =  controls1
            else:
                controls = controls2
        initial = pad[i]
    return controls
 

total = 0
for line in lines:
    line = list(line)
    controls = solve(line, numpad)

    min_size = min([len(i) for i in controls])
    controls = [i for i in controls if len(i) == min_size]

    second = []
    for i in controls:
        val = solve(i, dirpad)
        second.extend(val)

    controls = second
    min_size = min([len(i) for i in controls])
    controls = [i for i in controls if len(i) == min_size]

    third = []
    for i in controls:
        third.extend(solve(i, dirpad))

    controls = third
    min_size = min([len(i) for i in controls])
    controls = [i for i in controls if len(i) == min_size]

    print("final")
    controls = controls[0]
    print("".join(controls))

    a = len(controls)
    b = int(re.findall("\d+","".join(line))[0])
    print(f"{line}: {a}*{b}")
    total += a*b 

print(total)

#f = "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A"
#print(f.count('A'))


