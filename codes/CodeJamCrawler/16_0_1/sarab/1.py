T=int(input())
for t in range (T):
	n = int (input())
	if n == 0:
		print ('Case #%d: %s' %(t+1,'INSOMNIA'))
	else: 
		m = n
		digit = {}
		while len(digit) != 10:
			for d in str(n):
				digit[d] = 1
			n += m
		print ('Case #%d: %d' %(t+1,n-m))
	
