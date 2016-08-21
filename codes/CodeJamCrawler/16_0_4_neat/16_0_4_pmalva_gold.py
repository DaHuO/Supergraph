T = int(raw_input())

for i in xrange(T):
	line = raw_input()
	line = line.split()
	K = int(line[0])
	C = int(line[1])
	S = int(line[2])

	#just for the small input ;)
	print "Case #"+str(i+1)+":",
	for i in xrange(K-1):
		print i+1,
	print K
