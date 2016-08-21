#!/usr/bin/env python 

t = int(raw_input())
for i in range(t):
	digits = range(10)
	number = int(raw_input())
	if number == 0:
		print "Case #{}: INSOMNIA".format(i+1)
		continue
	else:
		multiplier = 1
		new_number = number
		while True:
			multiplier+=1
			newlist = [int(a) for a in str(new_number)]
			digits = [x for x in digits if x not in newlist]
			if not len(digits):
				print "Case #{}: {}".format(i+1,new_number)
				break
			else:
				new_number = number*multiplier


	
