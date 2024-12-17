from math import floor

lines = ""
with open("input.txt","r") as f:
    lines = f.read().strip().split("\n\n")

registers, program = lines

a,b,c = registers.split("\n")
A = int(a.split(":")[-1].strip())
b = int(b.split(":")[-1].strip())
c = int(c.split(":")[-1].strip())

program = program.split(":")[-1].strip().split(",")

combo = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': A,
        '5': b,
        '6': c,
        '7': None
}


for a in range(A):
    result = []
    i = 0
    combo['4'] = a
    a_backup = a
    
    while i<len(program):
        opcode = program[i]
        operand = program[i+1]
        if opcode == '0':
            a = a//(2**combo[operand])
            combo['4'] = a
    
        elif opcode == '1':
            b = int(b ^ int(operand))
            combo['5'] = b
    
        elif opcode == '2':
            b = combo[operand] % 8
            combo['5'] = b
    
        elif opcode == '3':
            if a == 0:
                pass
            else:
                i = int(operand)
                continue
    
        elif opcode == '4':
            b = int(b ^ c)
            combo['5'] = b
    
        elif opcode == '5':
            result.append(str(combo[operand] % 8))
    
        elif opcode == '6':
            b = a//(2**combo[operand])
            combo['5'] = b
    
        elif opcode == '7':
            c = a//(2**combo[operand])
            combo['6'] = c
        i += 2
    
    if result == program:
        print(f"same for {a}")
        break
    else:
        per = (a_backup/A) * 100
        print(f"{per} done")
