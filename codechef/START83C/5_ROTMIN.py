from math import ceil

# https://www.codechef.com/problems/ROTMIN

# worked in cpp, not in python
    
t = int(input())
for _ in range(t):
    n, p, q = map(int, input().split())
    s = input()
    positive = []
    negative = []
    for i in s:
        if i == 'a':
            positive.append(0)
        else:
            positive.append(123  - ord(i))
        negative.append(ord(i) - 97)

    beg = -1
    end = n
    possible = 0
    p_left = p
    q_left = q

    while ( beg != end):
        mid = ceil((beg + end)/2)
        pos = 0
        neg = 0
        positive1 = positive[:mid+1]
        negative1 = negative[:mid+1]
        positive1.sort()
        negative1.sort()
        pi=0
        qi=0
        while (pos<=p and neg<=q and pi+qi<mid+1):
            if pos + positive1[pi] <= p and neg + negative1[qi] <= q:
                if positive1[pi] <= negative1[qi]:
                    pos += positive1[pi]
                    pi += 1
                else:
                    neg += negative1[qi]
                    qi += 1
            elif pos + positive1[pi] <= p:
                pos += positive1[pi]
                pi += 1
            elif neg + negative1[qi] <= q:
                neg += negative1[qi]
                qi += 1
            else:
                break
        if pi + qi < mid+1:
            end = mid-1
        else:
            beg = mid+1
            possible = mid
            p_left = p - pos
            q_left = q - neg

    p = p_left
    q = q_left
    # print("till ",possible, " position we can have 'a'")
    # print("remaining p,q = ",p_left," ", q_left)
    focus = s[possible:]
    pos = 0
    neg = 0
    # print("string on focus: ", focus)
    for i in range(len(focus)):
        if focus[i] == 'a':
            continue
        else:
            pos1 = 123 - ord(focus[i])
            neg1 = ord(focus[i]) - 97
            if pos + pos1 <= p:
                pos += pos1
                focus = focus[:i]  + 'a' + focus[i+1:]
            elif neg + neg1 <= q:
                neg += neg1
                focus = focus[:i]  + 'a' + focus[i+1:]
            elif neg < q:
                focus = focus[:i]  + chr(ord(focus[i]) - (q - neg)) + focus[i+1:]
                neg = q
            elif pos < p:
                continue
            else: 
                break
    print('a' * (possible) + focus)
        
