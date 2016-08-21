n = 100
filename = "A-large.in.txt"
t = 0
for n in open(filename).readlines()[1:]:
	t += 1
	n = int(n)
	print "Case #%d:" % t,
	if n == 0:
		print 'INSOMNIA'
		continue
	a = [int(x) for x in str(n)]
	a.reverse()
	b = a[:]
	remain = 0
	digits = set(a)
	while len(digits) < 10:
		for i in range(len(a)):
			a[i] += b[i] + remain
			remain = a[i] / 10
			a[i] %= 10
		if remain > 0:
			a.append(remain)
			b.append(0)
			remain = 0
		digits |= set(a)
	a.reverse()
	print ''.join([str(x) for x in a])
