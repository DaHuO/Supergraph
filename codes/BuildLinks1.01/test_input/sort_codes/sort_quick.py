#Author: Stephen Pryor
#Date: September 26, 2012

import random

def partition(arr, p, r):
  x = arr[r]
  i = p - 1
  for j in range(p, r):
    if arr[j] <= x:
      i = i + 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i + 1], arr[r] = arr[r], arr[i + 1]
  return i + 1

def randomPartition(arr, p, r):
  i = random.randrange(p, r)
  arr[r], arr[i] = arr[i], arr[r]
  return partition(arr, p, r)

def randomQuickSort(arr, p, r):
  if p < r:
    q = randomPartition(arr, p, r)
    randomQuickSort(arr, p, q - 1)
    randomQuickSort(arr, q + 1, r)
