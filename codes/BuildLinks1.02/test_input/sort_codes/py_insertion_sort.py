# Insertion Sort Python
# O(n^2)

from random import shuffle

def insertionSort(alist):
	for index in range(1, len(alist)):
		currentValue = alist[index]
		position = index

		while position > 0 and alist[position - 1] > currentValue:
			alist[position] = alist[position - 1]
			position = position - 1

		alist[position] = currentValue
		print(alist)


alist = [i for i in range(15)]
shuffle(alist)

insertionSort(alist)
print(alist)