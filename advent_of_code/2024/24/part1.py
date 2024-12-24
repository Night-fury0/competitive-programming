
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
        print(f"{k}: {v}")
        count += 1


val = [0] * count
for k, v in source.items():
    if k.startswith("z"):
        val[int(k[1:])] = v

print(val)

power = 1
total = 0
for i in val:
    total += power*i
    power *= 2

print(total)



