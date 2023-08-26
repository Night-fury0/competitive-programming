# CRZBISHOP

t = int(input())
for _ in range(t):
    n = int(input())
    if n==1 or n==2:
        print(0)
    else:
        count = int(n/2)
        if count + 2 < n:
            count+= (n-(count+2))*2
        print(count+1)
        