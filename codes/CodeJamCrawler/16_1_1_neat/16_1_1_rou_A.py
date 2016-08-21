#!/usr/bin/python

cases = int(raw_input())
for case in xrange(1, cases+1): 
	s = list(raw_input())
	s.reverse()
	result = [s.pop()]
	while s != []: 
		letter = s.pop()
		if letter >= result[0]: 
			result.insert(0,letter)
		else: 
			result.append(letter)
	result = ''.join(result)
	print "Case #%d: %s" % (case, result)
