from math import floor

with open('input.txt', 'r') as f:
    active = 50
    count = 0
    for line in f:
        initial = active
        no = int(line[1:])
        if line[0] == 'L':
           count += abs(floor((active - no)/100))
           if (active-no)%100 == 0:
               count += 1
           if active == 0:
               count -= 1
           active = (active - no) % 100
        if line[0] == 'R':
           count += floor((active+no)/100)
           active = (active + no) % 100
        #print(f"{initial} to {active} moved {line[:-1]}, faced zero {count} times")

    print(count)


 
