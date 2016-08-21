# Google CodeJam 2016 - Qualification Round
# Problem A. Counting Sheep
# Author: Mahmoud Aladdin <aladdin3>

import sys
import math

def digitize(x):
	if x == 0: 
		return 1
	dig = 0
	while x > 0:
		r = x % 10
		dig |= 1 << r
		x /= 10
	return dig

def solve(cn):
	n = input()
	print "Case #%d:" % (cn,),
	if n == 0:
		print "INSOMNIA"
	else:
		goal = (1 << 10) - 1
		found = 0
		number = 0
		while found != goal:
			number += n
			found |= digitize(number)
		print number


if __name__ == "__main__":
	tc = input()
	for i in xrange(tc):
		solve(i + 1)
