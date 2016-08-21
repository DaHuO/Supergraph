import random, sys

b = int(sys.argv[1])
n = int(sys.argv[2])

s = {}
while len(s) < n:
	x = '1' + ''.join([random.choice(['0', '1']) for _ in xrange(b-2)]) + '1'
	d = []
	for a in xrange(2, 11):
		y = int(x, a)
		if is_prime(y):
			break
		f = list(factor(y))
		d.append(str(f[0][0]))
	else:
		s[x] = ' '.join(d)

print 'Case #1:'
for x in s:
	print x, s[x]


