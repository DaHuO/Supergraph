#!/usr/bin/python

import sys

tracked_numbers = []
def naming(number, times):
	if number == 0:
		return 'INSOMNIA'
	if (len(tracked_numbers) == 10):
		return number * (times - 1)
	else:
		track(number * times)
		return naming(number, times + 1)


def track(number):
	for n in str(number):
		if (n not in tracked_numbers):
			tracked_numbers.append(n)



#t = int(raw_input('# Test Cases : '))
t = int(sys.argv[1])
for i in range(t):
	#case = int(raw_input('Case # %d : ' % (i+1)))
	case = int(sys.argv[i+2])
	result = naming(case, 1)
	tracked_numbers = []
	print 'Case #%d: %s' % (i+1, result)
