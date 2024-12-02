total = 0

with open('input.txt', 'r') as f:
    for line in f:
        safe = True
        arr = [int(i) for i in line.split(" ")]
        is_increasing = all(((arr[i] < arr[i + 1]) and (arr[i+1] - arr[i] <=3)) for i in range(len(arr) - 1))
        is_decreasing = all(((arr[i] > arr[i + 1]) and (arr[i] - arr[i+1] <=3)) for i in range(len(arr) - 1))
        if is_increasing or is_decreasing:
            total += 1
print(total)

                   
