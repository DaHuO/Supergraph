for tdx in range(int(raw_input())):
	N = raw_input()
	hashTable = [0]*10
	flag = 0
	for idx in xrange(1, 201):
		iCtr = idx
		N1 = str(int(N)*idx)
		##print idx, N1
		for c in N1:
			if hashTable[int(c)] == 0:
				hashTable[int(c)] = 1
		if 0 in hashTable:
			continue
		else:
			print "Case #%d: %s"% (tdx+1, N1)
			flag = 1
			break
	if flag == 0:
		print "Case #%d: INSOMNIA"% (tdx+1)