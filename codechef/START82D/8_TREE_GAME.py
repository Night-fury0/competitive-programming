# TREE_GAME

# def max_potential_population(E, P, v, exclude, no_of_tiles):
#     q = -1
#     j = 0
#     exclude1 = []
#     if (no_of_tiles == 0) or (not set(E[v]) - set(E[v]).intersection(exclude)):
#         return P[v-1], exclude + [v]
#     else:
#         for i in E[v]:
#             if i not in exclude:
#                 if no_of_tiles > 1:
#                     no_of_tiles -= 1
#                     q1, e = max_potential_population(E, P, i, exclude + [v], no_of_tiles)
#                     if P[v-1] + q1 > q:
#                         q = q1
#                         exclude1 = e
#                 else:  # no_of_tiles == 1:
#                     if P[v-1] + P[i-1] > q:
#                         q = P[v-1] + P[i-1]
#                         j = i
#     if no_of_tiles == 1:
#         exclude = exclude + [v, j]
#     elif no_of_tiles > 1:
#         exclude = exclude1
#     return q, exclude
#
#
# def find_minimum_tiles_to_exit(E, v, exclude):
#     q = 100000000
#     exclude1 = []
#     if not set(E[v]) - set(E[v]).intersection(exclude):
#         return 0, exclude + [v]
#     else:
#         for i in E[v]:
#             if i not in exclude:
#                 q1, e = find_minimum_tiles_to_exit(E, i, exclude+[v])
#                 if 1 + q1 < q:
#                     q = 1 + q1
#                     exclude1 = e
#     return q, exclude1
# #
#
# def calculate_score(A, B):
#     pop_a = 0
#     pop_b = 0
#     score = 0
#     for i in range(len(B)):
#         pop_a += P[A[i]-1]
#         pop_b += P[B[i]-1]
#         if pop_a > pop_b:
#             score += 1
#     return score

# n, a, b = map(int, input().split())
# P = list(map(int, input().split()))
# E = {}
# for i in range(1, n+1):
#     E[i] = []
# for i in range(n-1):
#     u, v = map(int, input().split())
#     E[u].append(v)
#     E[v].append(u)


# def max_score_for_given_path_of_B(v, exclude, no_of_tiles, pop_a, sum_B):
#     q = -10000
#     result = 1 if pop_a + P[v-1] > sum_B[0] else 0
#     if (no_of_tiles == 0) or (not set(E[v]) - set(E[v]).intersection(exclude)):
#         return result
#     else:
#         for i in E[v]:
#             if i not in exclude:
#                 if no_of_tiles > 1:
#                     no_of_tiles -= 1
#                     sum_B = sum_B[1:]
#                     q = max(q, result + max_score_for_given_path_of_B(i, exclude + [v], no_of_tiles, pop_a + P[v-1], sum_B))
#                 else:  # no_of_tiles == 1:
#                     q = max(q, result + (1 if pop_a + P[v-1] + P[i-1] > sum_B[-1] else 0) )
#     return q
#
# B = find_minimum_tiles_to_exit(E, b, [])[1]
# sum_B = [sum(B[:i+1]) for i in range(len(B))]
# print(B)
# print(max_score_for_given_path_of_B(a, [], len(B), 0, sum_B))


# def max_score(E, P, a, b, pop_a, pop_b, exclude_a, exclude_b):
#     q = -1
#     if (not set(E[a]) - set(E[a]).intersection(exclude_a)) or (not set(E[b]) - set(E[b]).intersection(exclude_b)):
#         return 1 if P[a-1] + pop_a > P[b-1] + pop_b else 0
#     else:
#         for ai in E[a]:
#             if ai not in exclude_a:
#                 for bi in E[b]:
#                     if bi not in exclude_b:
#                             q = max(q,
#                                      (1 if P[a-1] + pop_a > P[b-1] + pop_b else 0) + max_score(E, P, ai, bi, pop_a + P[a-1], pop_b + P[b-1], exclude_a + [v], exclude_b + [v]))
#     return q


# t = int(input())
# for _ in range(t):
#     n, a, b = map(int, input().split())
#     P = list(map(int, input().split()))
#     E = {}
#     for i in range(1, n+1):
#         E[i] = []
#     for i in range(n-1):
#         u, v = map(int, input().split())
#         E[u].append(v)
#         E[v].append(u)

    # print(max_score(E, P, a, b, 0, 0, [], []))



    # b_exit = find_minimum_tiles_to_exit(E, b, [])
    # a_potential = max_potential_population(E, P, a, [], b_exit[0])
    # print(calculate_score(a_potential[1], b_exit[1]))



# print("B closest to node in: ", b_exit[0])
# print("A's population potential: ", a_potential[0])
# print("B's path: ", b_exit[1])
# print("A's path: ", a_potential[1])
# print("max score", score)


# A will never try to end, A will take the longest path with largest numbers
# B will try to end as soon as possible, so score of A remains less.

# find distance from nearest end vertex for both A & B
# if max_potential for A in dA is greater


# def optimize_a_b(E, P, a, b, pop_a, pop_b, exclude_a, exclude_b):
#     score = 0
#     for i in E[b]:
#         if i not in exclude_b:


# pop_a = 0
# pop_b = 0

# what B wants?
# shortest path to end the game with minimum score of A. To cut out the game as soon as possible with minimum score of A.

# what A wants?
# highest score of A, only has eye on increasing score, so doesn't look to end the game unless it is the highest possible score it can have.


t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    P = list(map(int, input().split()))
    E = dict()
    for i in range(1, n+1):
        E[i] = set()
    for i in range(n-1):
        u, v = map(int, input().split())
        E[u].add(v)
        E[v].add(u)


    def optimal_score(a, b, pop_a, pop_b, exclude_a, exclude_b):
        result = int(P[a-1] + pop_a > P[b-1] + pop_b)
        q = result
        for ai in E[a].difference(exclude_a):
            q_min = 10000
            # for a given move of A, B will choose such that it leads to minimum score
            for bi in E[b].difference(exclude_b):
                q_min = min(q_min, result + optimal_score(ai, bi, pop_a + P[a-1], pop_b + P[b-1], exclude_a[:] + [a], exclude_b[:] + [b]))
            # out of optimal moves chosen by B for each move of A, A will choose the one which led to maximum score
            if q_min < 10000:
                q = max(q, q_min)
        return q

    print(optimal_score(a, b, 0, 0, [], []))


