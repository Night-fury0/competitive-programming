import re

def compute(line):
    numbers = re.findall(r'\d', line)
    number = numbers[0] + numbers[-1]
    return int(number)
    

with open('input.txt', 'r') as f:
    total = 0
    for line in f:
        total += compute(line.strip())
    print(total)
