import random

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
	n = int(raw_input()) # read a list of integers, 2 in this case
	res = ''
	if n == 0:
		res = "INSOMNIA"
	else:
		# print "N = %s" % n
		j = 1
		chif = set()
		last = -1
		work = n
		while len(chif) != 10:
			work = j * n
			# print "J = %s" % j
			# print "CHIF = %s" % chif
			# print "N = %s" % n
			chif = chif.union(set(map(int,str(work))))
			last = work
			j += 1
		res = str(last)
	print "Case #{}: {}".format(i, res)