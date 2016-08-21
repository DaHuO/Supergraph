with open('fractiles.small') as file:
	cases = int(file.next())
	for case in xrange(cases):
		K, C, S = map(int, file.next().split())
		#print K, C, S
		tiles = []
		for k in xrange(K):
			tile = k
			for _ in xrange(C - 1):
				tile = tile * K + k
			tiles.append(tile + 1)
		print "Case #%d: %s" % (case + 1, ' '.join(map(str, tiles)))