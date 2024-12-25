
lines = ""
with open("input.txt","r") as f:
    lines = f.read().strip().split("\n\n")

source = dict()
initial = lines[0].split("\n")
for i in initial:
    k,v = i.split(": ")
    source[k] = int(v)


gates = lines[1].split("\n")

gates = [k.split(" ") for k in gates]

gates = {k[-1]:k for k in gates}

gates1 = gates

gates1['z08'],gates1['cdj'] = gates1['cdj'],gates1['z08']
gates1['z08'][-1] = 'z08'
gates1['cdj'][-1] = 'cdj'

gates1['mrb'],gates1['z16'] = gates1['z16'],gates1['mrb']
gates1['z16'][-1] = 'z16'
gates1['mrb'][-1] = 'mrb'

#gates1['pqv'],gates1['jbc'] = gates1['jbc'],gates1['pqv']
#gates1['pqv'][-1] = 'pqv'
#gates1['jbc'][-1] = 'jbc'

gates1['z32'],gates1['gfm'] = gates1['gfm'],gates1['z32']
gates1['z32'][-1] = 'z32'
gates1['gfm'][-1] = 'gfm'

gates1['dhm'],gates1['qjd'] = gates1['qjd'],gates1['dhm']
gates1['dhm'][-1] = 'dhm'
gates1['qjd'][-1] = 'qjd'

gates = gates1

def pattern(value, depth = 0):
    if depth == 6:
        return []
    elif value not in gates:
        return []
    else:
        count = 0
        conditions = []
        val = gates[value]
        conditions.append(val)
        print(f"{'  '*depth} {val[-1]} = {val[:-2]}")
        if val[0] in gates:
            conditions.extend(pattern(val[0], depth+1))
        if val[2] in gates:
            conditions.extend(pattern(val[2], depth+1))
        return conditions

pattern('z04')
#pattern('z08')
#pattern('z09')
#pattern('z16')
#pattern('z17')
pattern('z31')
pattern('z32')
pattern('z33')
pattern('z34')
#pattern('z38')
#pattern('z39')

#for i in range(45):
#    val = gates[f'z{str(i).zfill(2)}']
#    if val[0] != 'XOR':
#        print(i)
#        print(val)

#conds = pattern('z34')
#for i in conds:
#    print(f"{i[-1]} = {i[:-1]}")
#    
#print("\n")
#conds = pattern('z32')
#for i in conds:
#    print(f"{i[-1]} = {i[:-1]}")
#
#print("\n")
#conds = pattern('z33')
#for i in conds:
#    print(f"{i[-1]} = {i[:-1]}")
# 
 
        

