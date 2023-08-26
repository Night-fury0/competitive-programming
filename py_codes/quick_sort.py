# QUICK SORT
a = [1, 4, 2, 3, 6, 4, 4, 4]
n = len(a)


def partition(a, first, last):
    pivot = a[last]
    transfer = first - 1
    for i in range(first, last):
        if a[i] <= pivot:
            transfer += 1
            (a[transfer], a[i]) = (a[i], a[transfer])
    (a[transfer+1], a[last]) = (a[last], a[transfer+1])
    return transfer + 1


def quick_sort(a, first, last):
    if first < last:
        pi = partition(a, first, last)
        quick_sort(a, first, pi-1)
        quick_sort(a, pi+1, last)
    return a


print(quick_sort(a, 0, n-1))
