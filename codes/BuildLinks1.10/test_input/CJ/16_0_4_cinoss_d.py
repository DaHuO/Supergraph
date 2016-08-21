filename = "in.01"
filename = "D-small-attempt0.in.txt"
# filename = "B-large.in.txt"

test = 0
for line in open(filename).readlines()[1:]:
	test += 1
	print "Case #%d:" % test,
	k,c,s = [int(x) for x in line.split()]
	print " ".join([str(x) for x in xrange(1,k ** c + 1, k**(c-1))])
