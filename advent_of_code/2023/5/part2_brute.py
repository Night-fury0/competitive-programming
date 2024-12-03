
lines = ""
with open("input.txt", "r") as f:
    maps = f.read()[:-1].split("\n\n")
seeds = maps[0].split(":")[-1].split()
seeds = [int(i) for i in seeds]
maps = [i.split("\n")[1:] for i in maps[1:]]

values = list()
for i in range(0, int(len(seeds)), 2):
    part_list = [j + seeds[i] for j in list(range(seeds[i+1]))]
    values.extend(part_list)
    print(part_list)

seeds = list(set(values))

print(len(seeds))
exit()
final_values = list()
for i in seeds:
    curr_value = int(i)
    for j in maps:
        # goes through all the different transformations
        for k in j:
            # goes through all possible mapping ranges
            k = k.split()
            k = [int(val) for val in k]
            if k[1] <= curr_value <= k[1]+k[2]:
                curr_value = curr_value + k[0] - k[1]
                break 
        break
    final_values.append(curr_value)

print(final_values)
print(min(final_values))

    
