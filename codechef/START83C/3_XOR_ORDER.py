# XOR_ORDER

# Problem at https://www.codechef.com/problems/XOR_ORDER
# Explanation given at https://www.codechef.com/viewsolution/93410991

t = int(input())

        
for _ in range(t):
    a,b,c = map(int,input().split())
    if a<b and b<c:
        print(0)
    else:
        flag = 0
        k = max(a,b,c).bit_length()
        status = []
        x = [0] * k
        for i in range(k):
            bit_a = (a & (1<<(k-i-1))) >> (k-i-1)
            bit_b = (b & (1<<(k-i-1))) >> (k-i-1)
            bit_c = (c & (1<<(k-i-1))) >> (k-i-1)
            status.append((bit_a, bit_b, bit_c))
        i = 0
        flag = True
        while (status[i] in [(0,0,0),(1,1,1)]):
            i += 1
        if status[i] in [(1,0,1),(0,1,0)]:
            flag = False
        else:
            if status[i] in [(1,1,0),(0,0,1)]:
                x[i] = 1 if status[i] == (1,1,0) else 0 # a=b<c
                i += 1
                while status[i] in [(1,1,0),(0,0,1),(1,1,1),(0,0,0)]:
                    x[i] = 1 if status[i] == (1,1,0) else 0
                    i += 1
                if status[i] in [(1,0,0),(0,1,1), (1,0,1), (0,1,0)]:
                    x[i] = 1 if status[i] in [(1,0,0),(1,0,1)] else 0 # a<b
                else:
                    flag = False
            elif status[i] in [(1,0,0),(0,1,1)]:
                x[i] = 1 if status[i] == (1,0,0) else 0 # a<b=c
                i += 1
                while status[i] in [(1,0,0),(0,1,1),(1,1,1),(0,0,0)]:
                    x[i] = 1 if status[i] == (1,0,0) else 0
                    i += 1
                if status[i] in [(1,1,0),(0,0,1), (1,0,1), (0,1,0)]: 
                    x[i] = 1 if status[i] in [(1,1,0),(0,1,0)] else 0 # b<c
                else:
                    flag = False
        if flag == False:
            print(-1)
        else:
            print(int("".join([str(i) for i in x]),2))
