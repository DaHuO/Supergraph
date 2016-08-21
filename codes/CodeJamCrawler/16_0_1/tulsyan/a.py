T = int(raw_input())

nums = set([0,1,2,3,4,5,6,7,8,9])

for i in xrange(1, T + 1):
	N = int(raw_input())
	X = N
	if N == 0:
		ans = 'INSOMNIA'
	else:
		st = set()
		while True:
			for x in str(N):
				st.add(int(x))
			if st == nums:
				ans = N
				break
			
			N += X
			
	print 'Case #{0}: {1}'.format(i, ans)
