t = int(raw_input())
for i in range(1, t+1):
	n = int(raw_input())
	if n == 0:
		print 'Case #%d: INSOMNIA' % i
		continue 
	x = n
	s = set()
	for y in list(str(x)):
		s.add(y)
	cur = 0
	while len(s) < 10:
		x += n
		for y in list(str(x)):
			s.add(y)
		cur += 1
	print 'Case #%d: %d' % (i, x)