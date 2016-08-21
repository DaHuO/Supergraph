import sys
from itertools import izip
from collections import deque

# f = sys.stdin
f = open('D-large.in')
# f = open('test')
o = open('MYASS.out', 'w')
# o = sys.stdout

import operator


def get(k, c, s):

	if c * s < k:
		return 'IMPOSSIBLE'

	result = []

	start = 0
	
	for dive in range(int(k / c) + (k % c > 0)):
		total = k ** c
		rslt = 0

		for i in range(c):
			total /= k
			rslt += total * (start % k)
			start += 1
		result.append(rslt)

	# print k, c, s, 'ASS', len(result)
	return ' '.join(map(lambda x : str(1 + x), result)) 


if __name__ == "__main__":
	total = f.readline()
	
	for i in range(int(total)):
		k, c, s = map(int, f.readline().strip().split())
		ans = get(k, c, s)
		o.write('Case #%s: %s\n' % (i + 1, ans))