## Bubble Sort Python

from random import shuffle


def bubbleSort(alist):
	for passnum in range(len(alist)-1, 0, -1):
		for i in range(passnum):
			if alist[i] > alist[i+1]:
				temp = alist[i]
				alist[i] = alist[i+1]
				alist[i+1] = temp


alist = [i for i in range(10000)]
shuffle(alist)

bubbleSort(alist)
print(alist)