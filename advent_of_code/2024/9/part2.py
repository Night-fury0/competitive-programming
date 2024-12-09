from collections import Counter

line = ""
with open("input.txt","r") as f:
    line = f.read().strip()


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


counter_dict1 = Counter(final)

unique = set(final)
counter={i:0 for i in unique}

def find_consecutive_dots(lst, n):
    count = 0  
    for idx, value in enumerate(lst):
        if value == '.':
            count += 1  
            if count == n:
                return idx - n + 1  
        else:
            count = 0  
    return None

i = len(final)-1
while i>0:
    block = final[i]
    if block == '.':
        i-=1
        continue
    else:
        block_length = 0
        while final[i] == block:
            i-=1
            block_length += 1
        #print(f"block {block} of length {block_length} found")
        if counter[block] == 0:
            try:
                idx = find_consecutive_dots(final[:i+1],block_length)
                if idx is None:
                    raise ValueError
                while (block_length>0):
                    final[idx+block_length-1] = block
                    final[i+block_length] = '.'
                    block_length -= 1
                counter[block] += 1
            except ValueError:
                #print(f"dots of length {block_length} not found")
                pass

#print("".join(final))
counter_dict2 = Counter("".join(final))

for i in counter_dict1.keys():
    if counter_dict1[i] != counter_dict2[i]:
        print(f"counter mismatch for {i} {counter_dict1[i]} != {counter_dict2[i]}")

total = 0
for i, val in enumerate(final):
    if val != '.':
        total += i*int(val)
print(total)
    
