## Cocktail Shaker Sort Python
## Improvemnet on Bubble Sort


from random import shuffle

def cocktailSort(alist):
	up = range(len(alist)-1)

	while True:
		for indices in (up, reversed(up)):
			swapped = False
			for i in indices:
				if alist[i] > alist[i+1]:
					alist[i], alist[i+1] = alist[i+1], alist[i]
					swapped = True
			if not swapped:
				return

alist = [i for i in range(100000)]
shuffle(alist)

cocktailSort(alist)
print alist