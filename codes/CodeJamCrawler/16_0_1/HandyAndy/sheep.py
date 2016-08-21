

T = int(raw_input())
for t in range(T):
	N = int(raw_input())
	if N == 0:
		print 'Case #%d: INSOMNIA' %(t+1)
		continue
	unseen_digits = set(["1","2","3","4","5","6","7", "8", "9", "0"])
	i = 0
	while len(unseen_digits) > 0: 
		i += 1
		for ch in str(N*i):
			unseen_digits.discard(ch)
		
				
	print 'Case #%d: %d' %(t+1, N*i)
