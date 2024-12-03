
lines = ""
with open("input.txt", "r") as f:
    maps = f.read()[:-1].split("\n\n")
seeds = maps[0].split(":")[-1].split()
maps = [i.split("\n")[1:] for i in maps[1:]]

values = []
for i in seeds:
    curr_value = int(i)
    for j in maps:
        # goes through all the different transformations
        mapping = False
        for k in j:
            # goes through all possible mapping ranges
            k = k.split()
            k = [int(val) for val in k]
            if k[1] <= curr_value <= k[1]+k[2]:
                curr_value = curr_value + k[0] - k[1]
                mapping = True
                break 
    values.append(curr_value)
print(min(values))

    
