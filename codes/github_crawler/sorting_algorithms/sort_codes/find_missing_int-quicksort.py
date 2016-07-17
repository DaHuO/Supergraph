#!/usr/bin/env python

# Lightbox Programming Challenge
# Devan Rehunathan May 2011

import sys
import time
import heapq
#-------------------------------------------------------

import random

def _doquicksort(values, left, right):
    """Quick sort"""
    def partition(values, left, right, pivotidx):
        """In place paritioning from left to right using the element at
        pivotidx as the pivot. Returns the new pivot position."""
 
        pivot = values[pivotidx]
        # swap pivot and the last element
        values[right], values[pivotidx] = values[pivotidx], values[right]
 
        storeidx = left
        for idx in range(left, right):
            if values[idx] < pivot:
                values[idx], values[storeidx] = values[storeidx], values[idx]
                storeidx += 1
 
        # move pivot to the proper place
        values[storeidx], values[right] = values[right], values[storeidx]
        return storeidx
 
    if right > left:
        # random pivot
        pivotidx = random.randint(left, right)
        pivotidx = partition(values, left, right, pivotidx)
        _doquicksort(values, left, pivotidx)
        _doquicksort(values, pivotidx + 1, right)
 
    return values
 
def quicksort(mylist):
    return _doquicksort(mylist, 0, len(mylist) - 1)

#-------------------------------------------------------

from guppy import hpy
h = hpy()

if len(sys.argv) != 2:
	    sys.exit("usage: find_missing_int filename")

infile =  open(sys.argv[1])
lines = infile.readlines()
list = list()

#-------------------------------------------------------

t = time.clock()

for l in lines:
	number = l.split()
	list.append(int(number[0]))
	
t = time.clock() - t
print "Time taken to build list:", t, " seconds"

list_length = len(list)
max_int = list_length + 1
test_value = max_int + 1

#-------------------------------------------------------
t = time.clock()

quicksort(list)
#print list

t = time.clock() - t
print "Time taken to sort list:" , t, " seconds"

#-------------------------------------------------------
t = time.clock()

pointer_position = 0

if (list_length%2 == 0):
	tries = list_length/2
else:
	tries = (list_length-1)/2

# print "Number of tries: ", tries

for item in xrange(tries):
	if (list[item] + list[-(item+1)] > test_value):
		missing_value = 1 + item
		break
	elif (list[item] + list[-(item+1)] < test_value):
		missing_value = max_int - item
		break
	else:
		missing_value = (max_int + 1)/2

t = time.clock() - t
print "Time taken to find missing number:" , missing_value, "is", t, " seconds."
print h.heap()
#-------------------------------------------------------

infile.close()
