t = int(raw_input())
for i in xrange(t):
	x = int(raw_input())
	z = '';
	if x == 0:
		print 'Case #' + str(i+1) + ': INSOMNIA'
		continue
	for y in xrange(1, 100):
		z += str(x*y)
		z = ''.join(sorted(set(z)))
		if z == '0123456789':
			print 'Case #'+str(i+1)+': '+str(x*y)
			break
