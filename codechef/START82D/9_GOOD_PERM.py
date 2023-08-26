# GOOD_PERM
from collections import Counter
from math import factorial
MOD = 1000000007


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(abs, map(int, input().split())))
    a.sort()
    b.sort()

    def possibilities_for_given_value_of_c(c):
        count_B = Counter(b)
        result = 1
        for i in range(len(a)):
            no = abs(c-a[i])
            v1 = count_B.get(no, 0)
            if v1 == 0:
                result = 0
                break
            elif v1 > 0:
                result = (result * v1) % MOD
                count_B[no] -= 1
        return result


    first = a[0]
    possible_c = {a[-1] + b[0], a[0] - b[0], a[0] + b[-1], a[-1] - b[-1]}

    if b[0] == b[-1] and a[0] == a[-1]:
        print(factorial(n) % MOD)
    else:
        result = 0
        for i in possible_c:
            value = possibilities_for_given_value_of_c(i) % MOD
            result = (result + value) % MOD
        print(result)






# Trials

# Timelimit exceeded for all test cases, but approach seems to give correct answer.

    # def possibilities_for_given_value_of_c(c):
    #     feasibility_calculation = dict.fromkeys(range(n), 0)
    #     feasibility = []
    #     for i in range(len(a)):
    #         B = []
    #         for j in range(len(b)):
    #             if a[i] + b[j] == c or a[i] - b[j] == c:
    #                 B = B + [j]
    #         feasibility.append(B)
    #         # result is no. of b[j] that can form c with a[i]
    #         # print(f"For a[i] = {a[i]}, {c} can be formed using: {B}")
    #         # feasibility[i] = B
    #     feasibility.sort(key=len)
    #     # print(feasibility)
    #     result = 1
    #     for i in feasibility:
    #         count = 0
    #         if len(i) == 0:
    #             result = 0
    #             break
    #         sum = 0
    #         for j in i:
    #             sum += feasibility_calculation[j]
    #             feasibility_calculation[j] += (1/len(i))
    #         count += len(i) - floor(sum)
    #         result *= count
    #     # print(f"till a[{i}] = {a[i]}, {c} can be formed: {result}")
    #     return result



# Abandoned as the method to count permutations of (5,7),(6)(7) = 1 is attempted through collections.product which makes the list large, even if not feasibility uses a large size

# def possibilities_for_given_value_of_c(c):
#     feasibility = {k: [] for k in range(n)}
#     for i in range(len(a)):
#         # B = []
#         for j in range(len(b)):
#             if a[i] + b[j] == c or a[i] - b[j] == c:
#                 feasibility[i].append(j)
#                 # B = B + [j]
#         # result is no. of b[j] that can form c with a[i]
#         # print(f"For a[i] = {a[i]}, {c} can be formed using: {B}")
#         # feasibility[i] = B
#     result = sum([True for i in list(product(*feasibility.values())) if len(set(i)) == n])
#     # print(f"till a[{i}] = {a[i]}, {c} can be formed: {result}")
#     return result