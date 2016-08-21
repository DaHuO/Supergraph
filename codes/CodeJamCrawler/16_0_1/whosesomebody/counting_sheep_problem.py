#!/usr/bin/env python
nc = int(raw_input())

for i in xrange(1, nc + 1):
	control_array = []
	num = int(raw_input())
	if num != 0:
		for ind in xrange(1, 10000):
			if len(control_array) < 10:
				n = num*ind
				
				num_list = map(int, str(n))
				for el in num_list:

					if bool(control_array.count(el)) == False:
						control_array.append(el)
			else:
				print "Case #{}: {}".format(i, n)
				break
	else:
		print "Case #{}: INSOMNIA".format(i)

