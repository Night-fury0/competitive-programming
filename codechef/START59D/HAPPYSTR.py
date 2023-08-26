# https://www.codechef.com/START59D/problems/HAPPYSTR

t = int(input())

for i in range(t):
    a = list(input())
    if any([True for x in range(len(a)-2) if set(a[x:x+3]).issubset(['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'])]):
        print("Happy")
    else:
        print("Sad")


