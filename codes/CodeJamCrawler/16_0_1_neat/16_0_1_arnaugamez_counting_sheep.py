t = int(raw_input())
for i in xrange(1, t+1):
	N = int(raw_input())
	copy_N = N
	
	if N == 0:
		result = 'INSOMNIA'
	
	else:
		current_viewed = set([x for x in str(N)])
		j = 2
		
		while len(current_viewed) < 10:
			N = copy_N
			N *= j
			for e in str(N): current_viewed.add(e)
			j += 1
		
		result = str(N)

	print "Case #{}: {}".format(i, result)
