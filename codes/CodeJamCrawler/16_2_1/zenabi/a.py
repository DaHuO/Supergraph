from collections import Counter
from itertools import chain

def subtract_from_counter(c1, str, i):
	c = c1
	for x in str:
		c[x] -= i
	return c

def has_letter(c, str):
	c2 = Counter(str)
	for k in c2.keys():
		if not c.has_key(k):
			return False
		if c2[k] > c[k]:
			return False
	return True

def flatten(container):
	for i in container:
		if isinstance(i, list) or isinstance(i, tuple):
			for j in flatten(i):
				yield j
		else:
			yield i


l = ['ZERO', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT', 'NINE']
verbose = False

def guess_letter(c, current):
	if min(c.values()) < 0:
		print "Something is wrong."
	d = []
	while current < 10:
		if has_letter(c, l[current]):
			new_c = dict(c)
			subtract_from_counter(new_c, l[current], 1)
			if (sum(new_c.values()) == 0):
				return [current]
			if min(new_c.values()) < 0:
				print "Something is already wrong."
			d = guess_letter(new_c, current)
			if len(d) > 0:
				d += [current]
				return d
			current += 1
		else:
			current += 1
	return [];

def verify(s, digits):
	c1 = Counter(s)
	s2 = ""
	for d in digits:
		s2 += l[d]
	c2 = Counter(s2)
	return c1 == c2

in_f = open('A-small-attempt1.in')
T = int(in_f.readline())

out_f = open('a_small.out', 'w')
for t in xrange(T):
	print "------"
	print t
	s = in_f.readline()[:-1]
	c = Counter(s)
	digits = []
	# for i in xrange(c['Z']):
	# 	digits.append(0)
	# c = subtract_from_counter(c, 'ZERO', c['Z'])
	# for i in xrange(c['W']):
	# 	digits.append(2)
	# c = subtract_from_counter(c, 'TWO', c['W'])
	# for i in xrange(c['X']):
	# 	digits.append(6)
	# c = subtract_from_counter(c, 'SIX', c['X'])
	# for i in xrange(c['G']):
	# 	digits.append(8)
	# c = subtract_from_counter(c, 'EIGHT', c['G'])
	print "First:"
	print digits
	for i in xrange(0, 10):
		d = guess_letter(c, i)
		if len(d) > 0:
			print "accepted"
			digits = d
			break
		if len(d) == 0 and i == 9:
			print "problem"
	print "Then:"
	print digits
	verbose = False
	digits.sort()
	if not verify(s, digits):
		print s
		print digits
		exit()
	out_f.write('Case #{0}: '.format(t+1))
	for d in digits:
		out_f.write(str(d))
	out_f.write('\n')
in_f.close()
out_f.close()
