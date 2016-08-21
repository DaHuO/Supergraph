# Google CodeJam 2016 - Qualification Round
# Problem D. Fractiles
# Author: Mahmoud Aladdin <aladdin3>

import sys

def solve(cn):
	k, c, s = map(int, raw_input().strip().split(' '))

	print "Case #%d:" % (cn,),	
	if s < (k - 1):
		print "IMPOSSIBLE"
	else:
		if c == 1:
			if s == (k - 1):
				print "IMPOSSIBLE"
			else:
				print " ".join(map(str, range(1, k + 1)))
		else:
			if s == 1:
				print "1"
			else:
				print " ".join(map(str, range(2, k + 1)))
	
	

	


if __name__ == "__main__":
	tc = input()
	for i in xrange(tc):
		solve(i + 1)
