t = int(raw_input())

for i in xrange(1, t + 1):
	K, C, S = [int(s) for s in raw_input().split(" ")]
	tiles_cleaned = ''
	
	for j in xrange(1, K+1):
		tiles_cleaned += str(j) + ' '
		
	print "Case #{}: {}".format(i, tiles_cleaned[:-1])
