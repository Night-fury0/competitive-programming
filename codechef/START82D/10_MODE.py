# MODE
from bisect import bisect_left, bisect

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    frequency_list = []
    i = 0
    while(i<n):
        no = bisect(a,a[i]) - bisect_left(a,a[i])
        frequency_list.append(no)
        i += no
    frequency_list.sort(reverse=True)
    no_freq = len(frequency_list)
    sum = 0
    freq_sum = []
    for i in frequency_list:
        sum += i
        freq_sum.append(sum)
    mf = frequency_list[0]
    nm = frequency_list.count(mf)


    def min_moves_to_increase_modes_to_i(i):
        # only if no_modes < i <= n/2
        # to give minimum no. of operations to make i modes
        # reducing mode frequency from int(n/i) to 2, finding minimum no. of operations required to obtain i modes 
        result = 1000000

        for k in range(min(int(n/i), mf), 1, -1):
            index = no_freq - bisect_left(frequency_list[::-1], k)
            if index < i:
                positive_sum = freq_sum[index-1] - index*k
                negative_sum = (i-index)* k - ((freq_sum[i-1] if i<=no_freq else freq_sum[-1]) - freq_sum[index-1])
                # equal mode anomaly does not come here

            elif index >= i:
                positive_sum = freq_sum[i-1] - i*k
                negative_sum = 0
                # equal mode anomaly comes in this case
                # need to find no. of elements equal to 'k' between 'i' and 'index' elements
                if index > i and frequency_list[i] >= k:
                    positive_sum += freq_sum[index-1] - freq_sum[i-1] - (index-i)*(k-1)

            if positive_sum >= negative_sum:
                result = min(result, positive_sum)
            else:
                result = min(result, positive_sum + (negative_sum - positive_sum))
        if result == 1000000:
            result = -1
        return result

    result_arr = [-1] * n
    for i in range(1, int(n/2) + 1):
        if i == nm:
            result_arr[i-1] = 0
        elif i < nm:
            result_arr[i-1] = min(i, nm - i)
        elif i > nm:
            result_arr[i-1] = min_moves_to_increase_modes_to_i(i)
    result_arr[n-1] = n - no_freq
    print(*result_arr)


# print(min_moves_to_increase_modes_to_i(4))


# input

# 5
# 1 2 3 1 2

# Trials


# replaced by a common loop for method 1 and method 2 from int(n/i) to 2

# method 1: to form the no. of modes with same mode frequency
# value = 0
# required_nm = i - nm
# j = nm
# while j < len(frequency_list):
#     value += mf - frequency_list[j]
#     required_nm -= 1
#     j += 1
#     if required_nm == 0:
#         break
#
# if required_nm == 0 and n - (nm * mf) - (j - nm) >= value:
#     result = value
# else:
#     result = 100000

# method 2: to form the modes by reducing mode frequency (highest mode frequency less than current mode frequency)
# for k in range(i, n):
#     avg = floor(sum(frequency_list[:k]) / i)  # avg is the mode frequency we are working to achieve
#     positive_sum = 0
#     negative_sum = 0
#     for j in frequency_list[:k]:
#         if j > avg:
#             positive_sum += j - avg
#         elif j < avg:
#             negative_sum += avg - j
#     if positive_sum > negative_sum:
#         result = min(result, positive_sum)
#     elif n - avg * i >= negative_sum - positive_sum:
#         result = min(result, positive_sum + (negative_sum - positive_sum))


# frequency_counter = Counter(frequency_list)

# becoming so complicated

# def min_moves_to_make_i_modes(i, expected_mode_frequency):
#     result = -1
#     X = i - no_of_modes
#     if expected_mode_frequency > n/i:
#         result = -1
#     elif expected_mode_frequency == mode_frequency:
#         if n - (no_of_modes * mode_frequency) >= X * mode_frequency:
#             # result can be obtained with same mode_frequency
#             closest_to_mode_frequency = list(frequency_counter.keys())[1:]
#             j = 0
#             result = 0
#             while X > 0:
#                 if j < len(closest_to_mode_frequency):
#                     result += closest_to_mode_frequency[j]
#                     if frequency_counter[closest_to_mode_frequency[j]] >= X:
#                         result += X * (mode_frequency - closest_to_mode_frequency[j])
#                         break
#                     else:
#                         result += frequency_counter[closest_to_mode_frequency[j]] * (mode_frequency - closest_to_mode_frequency[j])
#                         X -= frequency_counter[closest_to_mode_frequency[j]]
#                         j += 1
#                 else:
#                     result = -1
#                     break
#         elif mode_frequency > 1:
#             result = min_moves_to_make_i_modes(i, mode_frequency-1)
#         else:
#             result = -1
#     else:  # EXPECTED MODE FREQUENCY < MODE FREQUENCY
#         if expected_mode_frequency > (mode_frequency - expected_mode_frequency):
#             result = expected_mode_frequency - mode_frequency
#         else:
#
#     return result