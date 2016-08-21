from sys import stdin

def answer(K):
	c='1'
	for i in range(2,K+1):
		c=c+' '+str(i)
	return c




T=int(stdin.readline())
for case in range(1,T+1):
	L=list(map(int,stdin.readline().split()))
	K=L[0]
	print('Case #%i: %s' % (case,answer(K)))
