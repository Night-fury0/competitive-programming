total = 0

with open('input.txt', 'r') as f:
    for line in f:
        safe = True
        arr = [int(i) for i in line.split(" ")]
        is_increasing = all(((arr[i] < arr[i + 1]) and (arr[i+1] - arr[i] <=3)) for i in range(len(arr) - 1))
        is_decreasing = all(((arr[i] > arr[i + 1]) and (arr[i] - arr[i+1] <=3)) for i in range(len(arr) - 1))
        if is_increasing or is_decreasing:
            total += 1
        else:
            safe = False
            for i in range(len(arr)):
                b = arr[:i] + arr[i+1:]
                is_increasing = all(((b[i] < b[i + 1]) and (b[i+1] - b[i] <=3)) for i in range(len(b) - 1))
                is_decreasing = all(((b[i] > b[i + 1]) and (b[i] - b[i+1] <=3)) for i in range(len(b) - 1))
                if is_increasing or is_decreasing:
                    safe = True
                    break
            if safe:
                total += 1
                    
print(total)

                   
