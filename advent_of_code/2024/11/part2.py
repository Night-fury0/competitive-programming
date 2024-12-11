lines = ""
with open("input.txt", "r") as f:
    lines = f.read().strip()

print(lines)
a = lines.split()
a = [int(i) for i in a]
print(a)

memo = {}

def find_count(val, no):
    if (val,no) in memo:
        return memo[(val,no)]
    
    if no == 75:
        return 1
    elif val == 0:
        result = find_count(1,no+1)
    elif len(str(val)) % 2 == 0:
        result = find_count(int(str(val)[:len(str(val))//2]), no+1) + find_count(int(str(val)[len(str(val))//2:]), no+1)
    else:
        result = find_count(val*2024,no+1)

    memo[(val, no)] = result
    return result

total = 0
for i in a:
    total += find_count(i,0)
print(total)

