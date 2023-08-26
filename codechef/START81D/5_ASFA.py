# ASFA
from math import ceil


def func(n,a):
    if n % 2 != 0:
        return -1
    else:
        no_one = sum(a)
        no_zero = n - no_one
        if no_zero == no_one:
            return 0
        else:
            if no_one == 0 or n == 2:
                return -1
            elif no_zero > no_one:
                return int(n/2 - no_one)
            else:
                if (n/2 - no_zero) % 2 == 0:
                    return int((n/2 - no_zero)/2)
                else:
                    return int(ceil((n/2 - no_zero)/2 + 1))


t = int(input())
for i in range(t):
    n = int(input())
    a = [int(x) for x in input().split(" ")]
    print(func(n,a))


# import unittest
# class TestFunction(unittest.TestCase):
#     def testcase(self):
#         self.assertEqual(func(4, [0, 0, 0, 0]), -1)
#         self.assertEqual(func(6, [0, 0, 0, 0, 0, 0]), -1)
#         self.assertEqual(func(4, [1, 1, 1, 1]), 1)
#         self.assertEqual(func(6, [1, 1, 1, 1, 1, 1]), 3)
#         self.assertEqual(func(6, [1, 1, 1, 1, 0, 0]), 2)
#         self.assertEqual(func(6, [0, 0, 0, 0, 1, 1]), 1)
#         self.assertEqual(func(8, [0, 0, 0, 0, 0, 1, 1, 1]), 1)
#         self.assertEqual(func(8, [1, 1, 1, 1, 1, 0, 0, 0]), 2)
#         self.assertEqual(func(2, [1, 1]), -1)
#         self.assertEqual(func(2, [0, 0]), -1)
