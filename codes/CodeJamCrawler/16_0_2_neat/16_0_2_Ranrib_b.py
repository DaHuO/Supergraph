import sys

def flip(pans):
	out = ''
	for i in xrange(len(pans)-1,-1,-1):
		if pans[i] == '+':
			out += '-'
		else:
			out += '+'
	return out

def solve(pans):
	if '-' not in pans:
		return 0

	if '+' not in pans:
		return 1

	# choose what to flip
	if pans[0] == '+':
		flip_ind = pans.index('-')
	else:
		flip_ind = pans.index('+')
	pans = flip(pans[:flip_ind]) + pans[flip_ind:]
	print pans
	return 1 + solve(pans)
		

lines = [x for x in open(sys.argv[1], 'rt').readlines()]
count = int(lines.pop(0))
with open('out.txt', 'wt') as outfile:
	for i in xrange(count):
		pans = lines.pop(0).strip()
		print 'Case #%d: %s' % (i + 1, solve(pans))
		outfile.write('Case #%d: %s\n' % (i + 1, solve(pans)))