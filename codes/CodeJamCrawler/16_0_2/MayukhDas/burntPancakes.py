for tdx in xrange(int(raw_input())):
	arr = list(raw_input().strip())
	flips = 0
	lArr = len(arr)
	while True:
		if arr == (['+']*lArr):
			break
		first = 0
		ch = 1
		while ch < lArr and arr[first] == arr[ch]:
			ch += 1
		##flip(first, ch-1)
		jdx = ch
		for idx in range(ch):
			if arr[idx] == '+':
				arr[idx] = '-'
			else:
				arr[idx] = '+'
		flips += 1
	print "Case #%d: %d"%(tdx+1, flips)