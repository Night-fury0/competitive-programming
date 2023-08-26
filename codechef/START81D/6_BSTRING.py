# BSTRING

MOD = 1000000007

def func(n, s):
    result = 0
    cur_zero = 0
    cur_one = 0
    for i in range(len(s)):
        if s[i] == '0':
            result += cur_zero % MOD
            cur_zero = ((cur_zero*2) + 1) % MOD
            cur_one = (cur_one * 2) % MOD
        elif s[i] == '1':
            result += cur_one % MOD
            cur_one = ((cur_one*2) + 1) % MOD
            cur_zero = (cur_zero * 2) % MOD

    return int((result + n) % MOD)


t = int(input())

for i in range(t):
    n = int(input())
    s = input()
    print(func(n, s))

#
# import unittest
#
#
# class TestCases(unittest.TestCase):
#     def test_case(self):
#         self.assertEqual(func(2, "10"), 2)
#         self.assertEqual(func(3, "110"), 4)
#         self.assertEqual(func(5, "11111"), 31)
#         self.assertEqual(func(8, "10100110"), 122)
#         self.assertEqual(func(6, "000000"), 63)
