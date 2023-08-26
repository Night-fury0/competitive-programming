# https://www.codechef.com/problems/PERMSUBSEQ

def func(n, a):
    b = [int(x) for x in a.split(" ") if int(x) <= n]
    count_dict = {x: b.count(x) for x in range(1, n+1)}
    total_result = 0
    round_result = 1

    for c in count_dict.values():
        round_result *= c
        if round_result == 0:
            break
        total_result += round_result
    return total_result % 1000000007


t = int(input())
for i in range(t):
    n = int(input())
    a = input()
    print(func(n, a))

# import unittest
# class TestFunction(unittest.TestCase):


#     def test_case(self):
#         self.assertEqual(func(10, "1 2 2 2 3 3 2 2 4 1"), 52)
#         self.assertEqual(func(5, "1 2 3 2 4"), 7)
#         self.assertEqual(func(5, "2 2 2 2 2"), 0)
#         self.assertEqual(func(5, "1 1 1 1 1"), 5)
#         self.assertEqual(func(6, "1 3 5 8 9 8"), 1)

# unittest.main()