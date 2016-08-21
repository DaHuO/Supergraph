def forever(init=1, step=1):
	it = init
	while True:
		yield it
		it += step

T = int(raw_input())
for t in xrange(1, T + 1):
	n = int(raw_input())
	if not n:
		print 'Case #%d: INSOMNIA' % t
		continue;
	seen = set()
	for i in forever():
		seen.update(str(i * n))
		if len(seen) == 10:
			break
	print 'Case #%d: %d' % (t, i * n)
