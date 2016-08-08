## Quick Sort Python

from random import shuffle

def quickSort(alist):
	quickSortHelper(alist, 0, len(alist)-1)

def quickSortHelper(alist, first, last):
	if first < last:

		splitpoint = partition(alist, first, last)

		quickSortHelper(alist, first, splitpoint-1)
		quickSortHelper(alist, splitpoint+1, last)

		# print(alist)

def partition(alist, first, last):
	pivotValue = alist[first]

	leftmark = first + 1
	rightmark = last

	done = False

	while not done:

		while leftmark <= rightmark and alist[leftmark] <= pivotValue:
			leftmark = leftmark + 1

		while alist[rightmark] >= pivotValue and rightmark >= leftmark:
			rightmark = rightmark - 1

		if rightmark < leftmark:
			done = True

		else:
			temp = alist[leftmark]
			alist[leftmark] = alist[rightmark]
			alist[rightmark] = temp

	temp = alist[first]
	alist[first] = alist[rightmark]
	alist[rightmark] = temp

	return rightmark

alist = [i for i in range(1000000)]
shuffle(alist)
print(alist)

print "====================================================="
print "====================================================="
print "====================================================="

quickSort(alist)
print(alist)
