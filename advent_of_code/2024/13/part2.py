
cost_a = 3
cost_b = 1

lines = ""
with open("input.txt","r") as f:
    lines = f.read().strip().split("\n\n")

total_a = 0
total_b = 0
for line in lines:
    a = line.split("\n")

    flag = True
    _,values1 = a[0].split(":")
    values1 = values1.strip()
    a1, a2 = values1.split(", ")
    a1 = int(a1.split("+")[1])
    a2 = int(a2.split("+")[1])

    _,values2 = a[1].split(":")
    values2 = values2.strip()
    b1, b2 = values2.split(", ")
    b1 = int(b1.split("+")[1])
    b2 = int(b2.split("+")[1])

    _,values3 = a[2].split(":")
    values3 = values3.strip()
    c1, c2 = values3.split(", ")
    c1 = int(c1.split("=")[1]) + 10000000000000
    c2 = int(c2.split("=")[1]) + 10000000000000

    print(f"{a1}x+{b1}y={c1}")
    print(f"{a2}x+{b2}y={c2}")
    x = (b1*c2-b2*c1)/(a2*b1-a1*b2)
    print(f"x = {x}")

    if x != int(x):
        flag = False
        continue
     
    y = (c1-a1*x)/b1
    print(f"y = {y}")
    
    if y != int(y):
        flag = False
        continue
    
    #if x > 100 or y > 100:
    #    flag = False
    #    continue

    if flag:
        total_a += x*cost_a
        total_b += y*cost_b

total = total_a + total_b

print(total)


