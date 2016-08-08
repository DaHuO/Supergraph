# quick sort algorithm with the first element as pivot

def quick_sort(a, l, r):
	
	if l < r:
		global comparisons
		comparisons = comparisons + (r - l - 1)
		divider = partition(a, l, r)

		quick_sort(a, l, divider)
		quick_sort(a, divider + 1, r)


def partition(a, l, r):
	pivot = a[l]
	i = l + 1
	for j in xrange(l + 1, r):
		if a[j] < pivot:
			a[j], a[i] = a[i], a[j]
			i += 1

	a[l], a[i - 1] = a[i - 1], a[l]
	return i - 1


if __name__ == '__main__':
	f = open('QuickSort.txt', 'r')
	a = f.read().splitlines()
	a = [int(i) for i in a]
	comparisons = 0

	#a = [2, 8, 9, 3, 7, 5, 10, 1, 6, 4]

	quick_sort(a, 0, len(a))
	print a
	print "Number of comparisons : ", comparisons