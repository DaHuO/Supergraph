## Gnome Sort Python
## Gnome sort is a sorting algorithm which is similar to Insertion sort, 
## except that moving an element to its proper place is accomplished by a 
## series of swaps, as in Bubble Sort.

from random import shuffle

def gnomeSort(alist):
	i, j, size = 1, 2, len(alist)
	
	while i < size:
		if alist[i-1] <= alist[i]:
			i, j = j, j+1
		else:
			alist[i-1], alist[i] = alist[i], alist[i-1]
			i -= 1
			if i == 0:
				i, j = j, j+1
	return alist


alist = [i for i in range(100000)]
shuffle(alist)

sortedL = gnomeSort(alist)
print sortedL