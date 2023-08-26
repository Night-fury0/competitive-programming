# GUESSPFMX

# https://www.codechef.com/problems/GUESSPFMX

t = int(input())

for _ in range(t):
    n = int(input())

    if n == 1:
        print("! 1")
        result = int(input())
    else:
        P = [0] * n
        Q = list(range(1,n+1))
        trials = 0
        large = n
        while(trials < n):
            print("?", *Q)
            a = list(map(int,input().split()))
            if a != [-1]:
                P[Q[a[-trials-1]-1]-1] = large

                large -= 1
                if P.count(0) == 1:
                    P = [i if i!=0 else 1 for i in P]
                    print("!", *P)
                    result = int(input())
                    if result == 1:
                        break
                ele = Q[a[-trials-1]-1]
                Q.remove(Q[a[-trials-1]-1])
                Q.insert(n-trials-1, ele)
                trials += 1
            else:
                break
    


