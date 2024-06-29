def remove_duplicates(arr):
    if not arr:
        return 0
    unique_index = 1
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i - 1]:
            arr[unique_index] = arr[i]
            unique_index += 1
    
    return unique_index

# Test cases
print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))  
print(remove_duplicates([2, 3, 4, 5, 6, 9, 9]))  
print(remove_duplicates([2, 2, 2, 11]))  
print(remove_duplicates([2, 2, 2, 11]))  
print(remove_duplicates([1, 2, 3, 11, 11])) 
