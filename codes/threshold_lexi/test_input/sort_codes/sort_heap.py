#Author: Stephen Pryor
#Date: September 26, 2012
#Implemented based on http://en.wikipedia.org/wiki/Heapsort

def sort_heap(lst):
  lst = heapify(lst)
  end = len(lst)-1
  while end > 0:
    lst[end], lst[0] = lst[0], lst[end]
    end = end - 1
    lst = siftDown(lst, 0, end)
  return lst

def heapify(lst):
  cnt = len(lst)
  start = (cnt-2)/2
  while start >= 0:
    lst = siftDown(lst, start, cnt-1)
    start = start - 1
  return lst
  
def siftDown(lst, start, end):
  root = start
  while root * 2 + 1 <= end:
    child = root * 2 + 1
    swap = root
    if lst[swap] < lst[child]:
      swap = child
    if child+1 <= end and lst[swap] < lst[child+1]:
      swap = child + 1
    if swap != root:
      lst[root], lst[swap] = lst[swap], lst[root]
      root = swap
    else:
      break
  return lst