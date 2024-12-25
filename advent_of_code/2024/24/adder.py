import copy

lines = ""
with open("input.txt","r") as f:
    lines = f.read().strip().split("\n\n")

source1 = dict()
initial = lines[0].split("\n")
for i in initial:
    k,v = i.split(": ")
    source1[k] = int(v)


gates1 = lines[1].split("\n")

gates1 = [k.split(" ") for k in gates1]

gates1 = {k[-1]:k for k in gates1}
# exchanging z08 and cdj
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

def adder(x=None, y=None):
    source = copy.deepcopy(source1)
    gates = copy.deepcopy(gates1)

    if x is not None:
        for k in source:
            if k.startswith("x"):
                no = int(k[1:])
                source[k] = (x>>no) & 1

    if y is not None:
        for k in source:
            if k.startswith("y"):
                no = int(k[1:])
                source[k] = (y>>no) & 1

    gates = list(gates.values())
    while gates:
        a,op,b,_,out = gates.pop(0)
        if a in source and b in source:
            if op == 'XOR':
                source[out] =  source[a] ^ source[b]
            elif op == 'AND':
                source[out] =  source[a] & source[b]
            elif op == 'OR':
                source[out] =  source[a] | source[b]
        else:
            gates.append((a,op,b,'->',out))
    
    count = 0
    for k, v in source.items():
        if k.startswith("z"):
            count += 1
    
    
    val = [0] * count
    for k, v in source.items():
        if k.startswith("z"):
            val[int(k[1:])] = v
    
    power = 1
    total = 0
    for i in val:
        total += power*i
        power *= 2
    
    return total

for i in range(45):
    no = 2**i
    actual = adder(no,no)
    expected = no+no
    if actual != expected:
        print(i, f"actual {actual}, expected {expected}")
        print(bin(actual))
        print(bin(expected))
        bit = 1
        while actual!=0 or expected!=0:
            if (actual>>1 & 1) != (expected>>1 & 1):
                print(f"incorrect at bit {bit}")
            bit += 1
            actual = actual >> 1
            expected = expected >> 1

# something wrong with z08 calculation


