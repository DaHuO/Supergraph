
def digitComplete(l):
	for k in l:
		if k==0: return False;
	return True

T = int(raw_input())

for i in xrange(T):
	mult = 1
	N = int(raw_input())
	l = [0 for k in range(10)]
	number = str(N)
	
	while not digitComplete(l) and N!=0:
		number = str(N * mult)
		for j in number:
			l[int(j)] = 1
		mult = mult + 1

		
	print 'Case #' + str(i+1) + ':',
	if N==0:
		print 'INSOMNIA'
	else:
		print number
