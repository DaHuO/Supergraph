N=int(raw_input())
M=N+1
for i in range (1,M):
	sequence=raw_input()+'+'
	nbr=len(sequence.split('+-'))+len(sequence.split('-+'))-2
	print 'Case #%d: %d'%(i,nbr)
