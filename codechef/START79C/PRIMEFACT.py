# PRIMEFACT: https://www.codechef.com/problems/PRIMEFACT

from math import sqrt, floor, ceil
t = int(input())


def get_lowest_prime_factor(n, original=False):
    if original:
        lowest_prime_factor = original
        limit_no = original + 1
    else:
        lowest_prime_factor = n
        limit_no = floor(sqrt(n))+1
    for i in range(3, limit_no, 2):
        if n % i == 0:
            lowest_prime_factor = i
            break

    return lowest_prime_factor


for i in range(t):
    x, y = [int(x) for x in input().split(" ")]
    num = x
    count = 0
    if x % 2 == 0:
        count = ceil((y-x)/2)
    else:
        original_lpf = get_lowest_prime_factor(num)
        while num < y:
            if num % 2 == 0:
                count += ceil((y-num)/2)
                num += ceil(y-num)
                break
            else:
                lpf = get_lowest_prime_factor(num, original_lpf)
                num += lpf
                count += 1
    print(count)

