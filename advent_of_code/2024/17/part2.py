from math import floor

lines = ""
with open("input.txt","r") as f:
    lines = f.read().strip().split("\n\n")

registers, program = lines

a,b,c = registers.split("\n")
a = int(a.split(":")[-1].strip())
b = int(b.split(":")[-1].strip())
c = int(c.split(":")[-1].strip())

program = program.split(":")[-1].strip().split(",")

res = []

def func(a,b,c):
    b = a % 8
    b = b ^ 2
    c = a >> b
    b = b ^ 3
    b = b ^ c
    result = b % 8
    a = a >> 3
    return a,b,c,result
#
#while a != 0:
#    a,b,c,result = func(a,b,c)
#    res.append(result)
#
#print(result)

for i in range(8):
    print(f"for i={i}, {func(i,0,0)[-1]}")

# by reverse engineering, in last iteration  a = 1 is only possible value 
# which means in penultimate iteration, 'a' can be 1<<3 to 1<<3 + 2**3-1 i.e. [8,15]
print("for penultimate iteration")

for i in range(8,16):
    print(f"for i={i}, {func(i,0,0)[-1]}")

# here in penultimate iteration, only value of 'a' that gives 3 is a = 8
# so in 14th iteration, 'a' can be 8<<3 to 8<<3+2**3-1
# identify which value here gives corresponding value for that particular index in program array


def find(x, pos):
    return [(x,pos) for x in range(x<<3,(x<<3)+2**3)]

possibilities = []
stack = [(1,15)]

while stack:
    print(stack)
    x, pos = stack.pop(0)
    print((x,pos))
    if pos == 0:
        possibilities.append(x)
        continue
    values = find(x,pos-1)
    for val in values:
        print(func(val[0],0,0)[3])
        print(program[val[1]])
        if func(val[0],0,0)[3] == int(program[val[1]]):
            print("success")
            print(val)
            stack.append(val)


print(min(possibilities))
