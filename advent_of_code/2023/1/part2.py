import re

conversion = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7", 
    "eight": "8",
    "nine": "9"
    }

reverse_conversion = {
    "eno": "1",
    "owt": "2",
    "eerht": "3",
    "ruof": "4",
    "evif": "5",
    "xis": "6",
    "neves": "7", 
    "thgie": "8",
    "enin": "9"
    }


def compute(line):
    numbers = re.findall(r'(one|two|three|four|five|six|seven|eight|nine|\d)', line)
    first = numbers[0]

    reverse_numbers = re.findall(r'(eno|owt|eerht|ruof|evif|xis|neves|thgie|enin|\d)', line[::-1])
    second = reverse_numbers[0]
    if first in conversion:
        first = conversion[first]
    if second in reverse_conversion:
        second = reverse_conversion[second]
    number = first + second
    #print(reverse_numbers)
    #print(f"{line}: {numbers}: {number}")
    return int(number)
    

with open('input.txt', 'r') as f:
    total = 0
    for line in f:
        try:
            total += compute(line.strip())
        except Exception as e: 
            print(f" exception: {line}")
            print(e)

    print(total)
