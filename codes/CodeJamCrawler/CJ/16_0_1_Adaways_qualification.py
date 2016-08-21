
with open('A-large.in') as f:
	lines = f.read().splitlines()
	T = int(lines[0])
	N = lines[1:]
	f.close()

def GetAsleepAt(N):
	if N == 0: return 'INSOMNIA'
	else :
		digits = set([0,1,2,3,4,5,6,7,8,9])
		i = 0
		while(len(digits) != 0):
			i=i+1
			N_digits=set([int(a) for a in str(i*N)])
			digits.difference_update(N_digits)		
		return i*N
with open('output.txt','wb') as output:
	for i in range(T):
		print >> output, 'case #{0}: {1}'.format(i+1,GetAsleepAt(int(N[i])))
	output.close()


