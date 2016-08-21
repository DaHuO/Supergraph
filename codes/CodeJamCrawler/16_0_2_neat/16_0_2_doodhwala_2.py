for cases in range(1, int(input()) + 1):
	s = input()
	ctr = 0
	lc = '+'
	for c in s[::-1]:
		if(c == lc):
			pass
		else:
			lc = c
			ctr += 1
	
	print('Case #%d:' % (cases,), ctr)
