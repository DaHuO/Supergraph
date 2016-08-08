# quick sort algorithm with the midian-of-three element as pivot

def quick_sort(a, l, r):
	
	if l < r:
		global comparisons
		comparisons = comparisons + (r - l - 1)
		divider = partition(a, l, r)

		quick_sort(a, l, divider)
		quick_sort(a, divider + 1, r)


def partition(a, l, r):
	
	array_length = r - l

	if array_length % 2 == 0:
		median = (array_length / 2) - 1
	else:
		median = array_length / 2

	median = l + median
	mid_element = sorted([a[l], a[r - 1], a[median]])[1]
	index = a.index(mid_element)
	a[l], a[index] = a[index], a[l]

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
	#a = [8, 2, 7, 5, 4, 13, 9, 11, 1]
	#a = [1, 3, 5, 2, 4, 6]

	quick_sort(a, 0, len(a))
	print a
	print "Number of comparisons : ", comparisons