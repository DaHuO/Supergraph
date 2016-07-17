## Shell Sort Python

from random import shuffle

def shellSort(alist):
	sublistcount = len(alist)//2

	while sublistcount > 0:
		for startposition in range(sublistcount):
			gapInsertionSort(alist, startposition, sublistcount)

		print("After increments of size", sublistcount, "The list is", alist)

		sublistcount = sublistcount // 2

def gapInsertionSort(alist, start, gap):
	for i in range(start+gap, len(alist), gap):

		currentvalue = alist[i]
		position = i

		while position >= gap and alist[position - gap] > currentvalue:
			alist[position] = alist[position - gap]
			position = position - gap

		alist[position] = currentvalue


alist = [i for i in range(1000000)]
shuffle(alist)

shellSort(alist)
print(alist)