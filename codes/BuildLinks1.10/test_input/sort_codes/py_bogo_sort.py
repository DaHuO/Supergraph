## Bogo Sort Python
## Bogosort simply shuffles a collection randomly until it is sorted.

import random

def bogoSort(alist):
	while not in_order(alist):
		random.shuffle(alist)
		print alist
	return alist

def in_order(alist):
	if not alist:
		return True

	last = alist[0]
	for x in alist[1:]:
		if x < last:
			return False
		last = x
	return True



alist = [i for i in range(10)]
random.shuffle(alist)

alist = bogoSort(alist)
print(alist)