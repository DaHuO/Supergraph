from os import system
from functools import reduce
import operator
from random import choice
print "Case #1:"

s = set()
n = (1<<(32-1)) + 1
cnt = 500
while True:
	ok = True
	div = []
	if n % 2 != 1: 
		n += 1
		continue
	num = "{0:32b}".format(n)
	for base in xrange(2,11):
		num_base = sum([ int(d) * (base**i) for i, d in enumerate(num[::-1]) ])
		system('gfactor {0} > tmp'.format(num_base))
		with open('tmp', 'r') as inp:
			line = inp.read().split()
			# print line
			divs = map(int,line[1:])
		if len(divs) == 1:
			ok = False
			break
		else:
			div.append(reduce(operator.mul,divs,1)/choice(divs))

	if ok:	
		t = " ".join(map(str,div))
		if not t in s:
			s.add(t)
			print num, t
			cnt -= 1
		else:
			continue
	if cnt <= 0: break
	n += 1
