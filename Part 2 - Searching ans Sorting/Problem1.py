def find_min_and_max(arr):
    min_val = arr[0]
    max_val = arr[0]
    min_index = 0
    max_index = 0
    for i in range(1, len(arr)):
        if arr[i] < min_val:
            min_val = arr[i]
            min_index = i
        if arr[i] > max_val:
            max_val = arr[i]
            max_index = i
    return f"min: {min_val}, index: {min_index} max: {max_val}, index: {max_index}"

print(find_min_and_max([5, 7, 4, -2, -1, 8]))
print(find_min_and_max([2, -5, -4, 22, 7, 7]))
print(find_min_and_max([4, 3, 9, 4, -21, 7]))
print(find_min_and_max([-1, 5, 6, 4, 2, 18]))
print(find_min_and_max([-2, 5, 7, 4, 7, -20]))
