import re

lines = ""
with open("input.txt", "r") as f:
    maps = f.read()[:-1].split("\n\n")

seeds = maps[0].split(":")[-1].split()
seeds = [int(i) for i in seeds]
maps = [i.split("\n")[1:] for i in maps[1:]]

seed_intervals = [(seeds[i],seeds[i] + seeds[i+1], 0) for i in range(0,len(seeds),2)]

min_location = seed_intervals[0][0]

while seed_intervals:
    beg, end, seg = seed_intervals.pop()
    print((beg,end,seg))

    if seg == 7:
        min_location = min(beg, min_location)
        continue

    m = maps[seg]

    for k in m:
        destination, start, delta = map(int, re.findall("\d+", k))
        diff = destination - start
        if beg >= start + delta or end <= start:
            continue
        if beg < start:
            seed_intervals.append((beg, start, seg))
            beg = start
        if end > start + delta:
            seed_intervals.append((start + delta, end, seg))
            end = start + delta
        seed_intervals.append((beg + diff, end + diff, seg + 1))
        break

    else:
        seed_intervals.append((beg, end, seg+1))
            
print(min_location)

