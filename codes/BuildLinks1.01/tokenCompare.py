#!/usr/bin/env python
# -*- coding: utf-8 -*-

def tokenCompare(target, compared):
	threshold = 0.75
	target = map(lambda st:st.lower(), target)
	compared = map(lambda st:st.lower(), compared)
	lent = len(target)
	lenc = len(compared)

	if lent > lenc:
		return False
	for i in range(lenc - lent + 1):
		count = 0.0
		for j in range(lent):
			if target[j] == compared[i+j]:
				count += 1
		ratio = count/lent
		if ratio >= threshold:
			return True
	return False


if __name__ == '__main__':
	target = ['elif', 'len','(', 'arRay', ')', '<=', 'insertsize', ':']
	compared = ['1', '2', 'Elif', 'array','(', 'arraY', ')', '<=', 'insertsize', ':', ',']
	print tokenCompare(target, compared)





