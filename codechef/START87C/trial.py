inp = "87 986 15"
a,b,c = map(int,inp.split())
X = pow(2,c)-1
m_val = (0|b) - (0&a)
x_val = [0]
count = 0
for i in range(pow(2,c)):
    if (i|b) - (i&a) > m_val:
        count = 1
        x_val = [i]
        m_val = (i|b) - (i&a)
    elif (i|b) - (i&a) == m_val:
        count += 1
        x_val.append(i)
print("count",count)
print("x_val",x_val)
print("m_val", m_val)
    
        
        
    