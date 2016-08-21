#!/usr/bin/python

cases = int(raw_input())
for case in xrange(1, cases+1): 
	number = int(raw_input())
	if number == 0: 
		print "Case #%d: INSOMNIA" % case
		continue
	current = number
	digits = set(str(number))
	while len(digits) != 10: 
		current = current + number
		digits.update(set(str(current)))
	print "Case #%d: %d" % (case, current)
