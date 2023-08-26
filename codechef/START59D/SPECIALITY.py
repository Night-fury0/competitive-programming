# https://www.codechef.com/START59D/problems/SPECIALITY

t = int(input())

for i in range(t):
    a = [int(x) for x in input().split(" ")]
    if a[0] > a[1] and a[0] > a[2]:
        print("Setter")
    elif a[1] > a[2] and a[1] > a[0]:
        print("Tester")
    else:
        print("Editorialist")




