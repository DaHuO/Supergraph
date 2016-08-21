T = input()
for cas in xrange(1,T+1):
	mk = [0] * 10
	# print mk
	print 'Case #'+str(cas)+":",
	N = input()
	if N == 0:
		print 'INSOMNIA'
		continue	
	now = N
	ans = 1
	cnt = 0
	while 1:		
		# print now
		w = str(now)		
		for c in w:
			q = ord(c) - ord('0')			
			if mk[q] == 0:
				mk[q] = 1
				cnt += 1
		if cnt == 10:
			break;
		now += N		
	print now

