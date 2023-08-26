# BINANDTER
# from math import floor

# def power_of_k_in_n(n, k):
#     # finds no. of times power k can be fit into n
#     q = n
#     count = 0
#     while q not in range(k):
#         q = floor(q/k)
#         count += 1
#     return count

# print(power_of_k_in_n(100000000, 2))
# print(power_of_k_in_n(100000000, 3))
#
# power_two = [pow(2, i) for i in range(27)]
# power_three = [pow(3, i) for i in range(17)]
# power = ([pow(2, i) for i in range(27)] + [pow(3, i) for i in range(17)]).sort()[::-1]



# def find_minimum_count(n):
#     c1, r1 = power_remainder(n, 2)
#     c2, r2 = power_remainder(n, 3)
#     if r1 == 0:
#         return 1
#     elif r2 == 0:
#         return 1
#     else:
#         return min(power_)

# power_remainder(100000000, 2)
# power_remainder(100000000, 3)


power = [67108864, 43046721, 33554432, 16777216, 14348907, 8388608, 4782969, 4194304, 2097152, 1594323, 1048576,
         531441, 524288, 262144, 177147, 131072, 65536, 59049, 32768, 19683, 16384, 8192, 6561, 4096, 2187, 2048,
         1024, 729, 512, 256, 243, 128, 81, 64, 32, 27, 16, 9, 8, 4, 3, 2, 1, 1]

sum_power = [198787808, 131678944, 88632223, 55077791, 38300575, 23951668, 15563060, 10780091, 6585787, 4488635,
             2894312, 1845736, 1314295, 790007, 527863, 350716, 219644, 154108, 95059, 62291, 42608, 26224, 18032,
             11471, 7375, 5188, 3140, 2116, 1387, 875, 619, 376, 248, 167, 103, 71, 44, 28, 19, 11, 7, 4, 2, 1]

# https://www.codechef.com/problems/BINANDTER
# https://www.codechef.com/viewsolution/92605554

def min_count(n, power, sum_power):
    if n in power:
        return 1
    else:
        lower = 0
        lower_flag = True
        upper = 0
        upper_flag = True
        for i in range(len(power)):
            if power[i] < n and lower_flag:
                lower = i
                lower_flag = False
            if sum_power[i] <= n and upper_flag:
                upper = i
                upper_flag = False
        q = 1000
#         print(f" n: {n} # lower: {power[lower]} # upper: {power[upper-1]}")
        for i in range(lower, upper):
            q = min(q, 1 + min_count(n - power[i], power[i+1:], sum_power[i+1:]))
        return q


t = int(input())
for i in range(t):
    n = int(input())
    print(min_count(n, power, sum_power))
