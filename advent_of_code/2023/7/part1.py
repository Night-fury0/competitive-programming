from collections import Counter
from functools import cmp_to_key

lines = ""
with open("input.txt","r") as f:
    lines = f.read().strip().split("\n")

order = [[1, 1, 1, 1, 1], [2, 1, 1, 1], [2, 2, 1], [3, 1, 1], [3, 2], [4, 1], [5]]
replacement_dict = {'A':'a', 'K':'b', 'Q':'c', 'J':'d', 'T':'e', '9':'f', '8':'g', '7':'h', '6':'i', '5':'j', '4':'k', '3':'l', '2':'m'}

def sort_card(a,b):
    type1 = a[0]
    type2 = b[0]

    counter1 = dict(Counter(list(type1)))
    counter2 = dict(Counter(list(type2)))

    counter_values1 = sorted(list(counter1.values()), reverse=True)
    counter_values2 = sorted(list(counter2.values()), reverse=True)

    if counter_values1 > counter_values2:
        return 1
    elif counter_values1 < counter_values2:
        return -1
    else:
        translation_table = str.maketrans(replacement_dict)
        type1 = type1.translate(translation_table)
        type2 = type2.translate(translation_table)

        if type1 < type2:
            return 1
        else:
            return -1

master = []

for line in lines:
    hand, bid = line.split()
    master.append((hand,bid))

master = sorted(master, key=cmp_to_key(sort_card))

total = 0
for i in range(len(master)):
    total += int(master[i][1])*(i+1)

print(total)

    
