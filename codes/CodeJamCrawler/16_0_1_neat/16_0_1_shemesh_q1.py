def func(n):
	n_orig = n
	d = {}
	for i in range(1,0x100):
		n = n_orig*i
		n2 = n
		while n2:
			d[n2%10]=1
			n2 /= 10
			if len(d.keys())==10:
				return str(n)
	return 'INSOMNIA'
	
T = int(raw_input())
for i in range(T):
	N = int(raw_input())
	print 'Case #%d: %s' % (i+1, func(N))