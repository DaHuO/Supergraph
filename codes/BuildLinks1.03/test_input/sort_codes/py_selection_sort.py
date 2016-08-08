# SelectionSort Python

from random import shuffle

def selectionSort(alist):
	for fillslot in range(len(alist)-1,0,-1):
		positionOfMax = 0
		for location in range(1, fillslot+1):
			if alist[location] > alist[positionOfMax]:
				positionOfMax = location

		temp = alist[fillslot]
		alist[fillslot] = alist[positionOfMax]
		alist[positionOfMax] = temp
		print(alist)


alist = [i for i in range(10)]
shuffle(alist)

selectionSort(alist)
print(alist)