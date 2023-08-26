from bisect import bisect,bisect_left

def minLength(n, k, a):
    freq = dict()
    a1 = a[:]
    a1.sort()
    for i in a:
        c = bisect(a1,i) - bisect_left(a1,i)
        if c > k:
            freq[i] = c-k
    if not freq:
        return 0
    else:
        to_remove = list(freq.keys())
        start = 0
        end = n-1
        while(a[end] not in to_remove):
            end-=1
        low = n
        while start<=end:
            while (a[start] not in to_remove):
                start+=1
            check = freq.copy()
            j = (start+end)/2
            # set flag to True if all req elements are covered in [start,j] or in other words, take j to min position which can have all req. elements.
            while j<=end:
                # use binary search to find lowest j possible
                flag = False
                while(j<=end and a[j] in check and max(check.values())>0):
                    if check[a[j]] > 0:
                        check[a[j]]-=1  
                    j+=1
                    flag = True
                while(j<=end and a[j] not in check and max(check.values())>0):
                    j+=1
                    flag = True
                if not flag:
                    break
            if j<=end or max(check.values())==0:
                low = min(low,j-start)
            if low == sum(freq.values()):
                break
            start+=1
        return low


n=9
k=1
a = [8,1,9,8,5,1,1,8,6]
print(minLength(n,k,a))