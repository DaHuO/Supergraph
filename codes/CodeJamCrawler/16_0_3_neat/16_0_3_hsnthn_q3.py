import math

nontirivial_divisor = {}

def first_nontrivial_divisor(n):
	if n in nontirivial_divisor:
		return nontirivial_divisor[n]
	
	if (n % 2) == 0 and n > 2: 
		return "2"

	res = -1
	for i in xrange(3, int(math.sqrt(n)) + 1, 2):
		if (n % i) == 0:
			res = str(i)
			nontirivial_divisor[n] = res
			break

	return res

def is_jam_coin(n):
	dl = []
	for i in xrange(2, 10 + 1):
		bn = int(n, i)
		d = first_nontrivial_divisor(bn)
		dl.append(d)

		if d == -1:
			return []

	return dl

def solve(l):
	ls = l.split(' ')
	n = int(ls[0])
	j = int(ls[1])
	c = 0

	"""
	100001
	1 0000 1 0*2
	1 0001 1 1*2
	1 0010 1 2*2
	1 0011 1 3*2
	2 ** 5
	"""

	jl = []

	for i in xrange(0, 2 ** (n-2)):
		if len(jl) == j:
			break

		jam = "{0:b}".format(2 ** (n-1) + (i*2) + 1)
		dl = is_jam_coin(jam)
		
		print jam, dl

		if len(dl) != 0:
			jl.append("%s %s" % (jam, ' '.join(dl)))

	return jl

inf = open("input.txt", "r")
outf = open("output.txt", "wr")

t = inf.readline().rstrip()

for i in xrange(1, int(t)+1):
	l = inf.readline().rstrip()
	r = solve(l)
	print l, r
	outf.write("Case #%d:\n%s" % (i, '\n'.join(r)))

inf.close()
outf.close()