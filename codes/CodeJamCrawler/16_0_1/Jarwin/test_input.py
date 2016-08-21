#!/usr/bin/env python
import math
index = 0
while True:
	try:
		c=1;s = set();N = int(raw_input())
		if index == 0:
			index += 1
			continue
		if N==0:
			print 'Case #%d: INSOMNIA'%(index)
			index = index+1	
			continue
		while True:
			new_number = c*N
			c = c+1
			digits = [new_number / 10 ** i % 10 for i in range(int(math.log(new_number, 10)), -1, -1)]
			s.update(digits)
			if sorted(s) == [0,1,2,3,4,5,6,7,8,9]:
				print 'Case #%d: %d'%(index,new_number)
				break
		index = index+1
	except EOFError:
		exit()
  		