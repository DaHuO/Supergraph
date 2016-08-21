#Author: Stephen Pryor
#Date: September 26, 2012

def sort_selection(lst):
  length = len(lst)
  for i in range(length):
    min_val = lst[i]
    min_index = i
    for j in range(i, length): 
      if lst[j] < min_val:
        min_val = lst[j]
        min_index = j
    if lst[i] > min_val:
      lst[i], lst[min_index] = min_val, lst[i]
  return lst