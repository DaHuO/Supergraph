#!/usr/bin/env python

import sys
from string import ascii_uppercase

with open(sys.argv[1]) as f:
	cases = int(f.readline().strip())
	for case in range(1, cases + 1):
		N = int(f.readline().strip())
		senators = [
			[ascii_uppercase[letter]] * int(number)
			for letter, number in enumerate(f.readline().strip().split(' '))
		]
		evacuate = []
		while senators:
			senators.sort(key=len, reverse=True)
			if len(senators) > 2 and len(senators[0]) > len(senators[1]):
				evacuate += [senators[0].pop() + senators[2].pop()]
			elif len(senators) > 2 and len(senators[0]) == len(senators[1]):
				evacuate += [senators[1].pop()]
			elif len(senators) == 2:
				evacuate += [senators[0].pop() + senators[1].pop()]
			senators = [s for s in senators if s]
		print('Case #%s: %s' % (case, ' '.join(evacuate)))

