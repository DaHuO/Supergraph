# Merge Sort implemented with Python

from random import shuffle

def mergeSort(alist):
	print("Splitting", alist)

	if len(alist) > 1:
		mid = len(alist)/2
		lefthalf = alist[:mid]
		righthalf = alist[mid:]

		mergeSort(lefthalf)
		mergeSort(righthalf)

		i = 0
		j = 0
		k = 0

		while i < len(lefthalf) and j < len(righthalf):
			if lefthalf[i] < righthalf[j]:
				alist[k] = lefthalf[i]
				i = i + 1
			else:
				alist[k] = righthalf[j]
				j = j + 1
			k = k +1

		while i < len(lefthalf):
			alist[k] = lefthalf[i]
			i = i + 1
			k = k + 1

		while j < len(righthalf):
			alist[k] = righthalf[j]
			j = j + 1
			k = k + 1

	print("Merging", alist)

# alist = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38.39,40]
alist = [i for i in range(5000000)]
shuffle(alist)


mergeSort(alist)
print(alist)