#!/usr/bin/python
#
# Problem: Counting Sheep
# Language: Python
# Author: VictoriaMengqiLIU
# Usage: python A.py <a.in> a.out

try:
	case = int(raw_input())
	
	for each in range(case):
		s = int(raw_input())
		tmp = s
		n = 1
		d = []
		for i in range(10):
			d.append(str(i))
		
		if s == 0:
			print 'Case #{}: INSOMNIA'.format(each + 1)

		while len(d) > 0 and s != 0:

			for ss in str(s):
				if ss in d:
					d.remove(ss)
			
			if len(d) == 0:
				print "Case #{}: {}".format(each + 1, s)

			s += tmp


except EOFError:
	exit(1)

