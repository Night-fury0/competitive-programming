# MINDIF

# sorting manually caused RE error in codechef, using a.sort() worked better.

# def partition(a, first, last):
#     pivot = a[last]
#     transfer = first - 1
#     for i in range(first, last):
#         if a[i] <= pivot:
#             transfer += 1
#             (a[transfer], a[i]) = (a[i], a[transfer])
#     (a[transfer+1], a[last]) = (a[last], a[transfer+1])
#     return transfer + 1
#
#
# def quick_sort(a, first, last):
#     if first < last:
#         pi = partition(a, first, last)
#         quick_sort(a, first, pi-1)
#         quick_sort(a, pi+1, last)
#     return a


# to check if all elements are same, just check first and last element, if both are same, all elements are same,
# since it is sorted

# def swap_first_non_equal(a, first, last, swap = True):
#     flag = 0
#     for i in range(first, last):
#         if a[i] != a[i+1]:
#             if swap:
#                 (a[i], a[i+1]) = (a[i+1], a[i])
#             flag = 1
#             break
#     return a, flag


# func() too lengthy, so optimized to func1()

# def func(n, a):
#     if n == 2:
#         a = [-1]
#     else:
#         # for n >= 3
#         a.sort()
#         min_diff = a[1] - a[0]
#         pos = (0, 1)
#         # first find if any solution is possible with minimum difference possible with given array
#         for i in range(1, n):
#             diff = a[i] - a[i-1]
#             if diff < min_diff:
#                 pos = (i-1, i)
#                 min_diff = diff
#                 if min_diff == 0:
#                     break
#         # print(f"the 2 nos are: {a[pos[0]]}, {a[pos[1]]}")
#         # two elements which make the minimum difference is swapped to first two positions of array
#         if not (pos[0] == 0 and pos[1] == 1):
#             (a[0], a[pos[0]]) = (a[pos[0]], a[0])
#             (a[1], a[pos[1]]) = (a[pos[1]], a[1])
#         if a[1] <= a[2]:
#             # a, check = swap_first_non_equal(a, 2, n-1)
#             if a[2] == a[-1]:
#                 # means all elements apart from first two elements are same
#                 if a[1] == a[2]:
#                     # all elements apart from first element are same
#                     if a[0] == a[1]:
#                         # all elements are equal, so no other possible permutation if not the min difference
#                         a = [-1]
#                     else:
#                         # this case should not happen except if n = 3
#                         (a[0], a[1]) = (a[1], a[0])
#                 else:   # a[1] < a[2]
#                     if a[0] != a[1]:
#                         a = [*a[2:], a[0], a[1]]
#                     else:
#                         (a[1], a[2]) = (a[2], a[1])
#             else:
#                 (a[2], a[-1]) = (a[-1], a[2])
#         else:   # a[1] > a[2]
#             if a[0] == a[1]:
#                 # no need to swap, just to check if all elements after index 2 are equal, in which case, swap is needed
#                 if a[2] == a[-1]:
#                     (a[1], a[2]) = (a[2], a[1])
#
#     return a


# still throwing wrong answer for 2 cases

# def func1(n, a):
#     a.sort()
#     min_diff = min([a[i+1] - a[i] for i in range(n-1)])
#     if n == 2 or a[0] == a[-1]:
#         a = [-1]
#     elif a[1] - a[0] == min_diff:
#         if a[2] != a[-1]:
#             (a[2], a[-1]) = (a[-1], a[2])
#         elif a[0] == a[1]:
#             (a[1], a[2]) = (a[2], a[1])
#         else:
#             a = [*a[2:], a[0], a[1]]
#     elif a[1] == a[-1]:
#         (a[0], a[1]) = (a[1], a[0])
#     else:
#         a = [*a[1:], a[0]]
#     print(" ".join(map(str, a)))


t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split(" ")))
    a.sort()
    min_diff = min([a[i+1] - a[i] for i in range(n-1)])
    if n == 2 or a[0] == a[-1]:
        print(-1)
    elif a[1] - a[0] == min_diff:
        if a[2] != a[-1]:
            print(*a[2:], a[0], a[1])
        elif a[0] == a[1]:
            print(*a[1:], a[0])
        else:
            print(a[-1], *a[:-1])
    elif a[1] == a[-1]:
        print(a[-1], *a[:-1])
    else:
        print(*a[1:], a[0])


# import unittest
#
#
# class Testing(unittest.TestCase):
#     def testcase1(self):
#         self.assertEqual(func1(4, [1, 3, 5, 3]), [3, 3, 5, 1])
#         self.assertEqual(func1(4, [4, 3, 2, 1]), [1, 2, 4, 3])
#         self.assertEqual(func1(4, [1, 1, 1, 1]), [-1])
#         self.assertEqual(func1(4, [4, 4, 3, 3]), [3, 4, 3, 4])
#         self.assertEqual(func1(3, [4, 4, 3]), [4, 3, 4])
