#0123456789

import sys

#lines = [line.strip() for line in sys.stdin.readlines()]
with open("A-small-attempt2.in", "r") as fin:
	lines = fin.read().splitlines()
n = int(lines.pop(0))

for x in xrange(1,n+1):
	num = int(lines.pop(0))
	check = [False] * 10

	if num == 0 :
		print 'Case #%s: INSOMNIA' % x

	else:
		lnum = []
		for c in str(num):
			lnum.append(int(c))

		for y in xrange(len(lnum)):
			check[lnum[y]] = True

		count = 1
		while check.count(True) != 10:
			newnum = num*count
			
			nlnum = []
			for c in str(newnum):
				nlnum.append(int(c))
			#nlnum = map(int,str(newnum))

			for y in xrange(len(nlnum)):
				check[nlnum[y]] = True
			count += 1
		print 'Case #%s: %s' % (x, newnum)
