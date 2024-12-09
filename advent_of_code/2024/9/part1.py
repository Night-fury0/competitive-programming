
line = ""
with open("input.txt","r") as f:
    line = f.read().strip()

print(line)

final = []
block = True
number = 0

for i in range(len(line)):
    if block:
        block = False
        final.extend([str(number)]*int(line[i]))
        number += 1
    else:
        block = True
        final.extend(['.']*int(line[i]))


print("".join(final))

while "." in final:
    val = final.pop()
    if val == '.':
        continue
    idx = final.index(".")
    final[idx] = val

total = 0
for i, val in enumerate(final):
    total += i*int(val)
print(total)
    
