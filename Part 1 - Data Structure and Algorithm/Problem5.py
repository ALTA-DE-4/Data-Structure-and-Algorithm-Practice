def max_sequence (arr):
  n = len(arr)
  max_so_far = 0
  current_max = 0
  for i in range(n):
    current_max += arr[i]
    if current_max < 0:
      current_max = 0
    if max_so_far < current_max:
      max_so_far = current_max
  return max_so_far

print (max_sequence ([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print (max_sequence ([-2, -5, 6, -2, -3, 1, 5, -6])) 
print (max_sequence ([-2, -3, 4, -1, -2, 1, 5, -3]))
print (max_sequence ([-2, -5, 6, -2, -3, 1, 6, -6]))
print (max_sequence ([-2, -5, 6, 2, -3, 1, 6, -6])) 