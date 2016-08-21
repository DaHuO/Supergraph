def isHashComplete(A):
	for a in A:
		if a==0:
			return False
	return True



def putDigits(N, hash_):
	S=str(N)
	for s in S:
		hash_[int(s)]=1
		# print s
	return

def fun(N):
	hash_ = [0 for i in range(0,10)]
	i=1
	M=N
	while not isHashComplete(hash_):
		M=N*i
		putDigits(M, hash_)
		i+=1

	return M
		


for z in range(int(input())):
	N=int(input())
	if N==0:
		print 'Case #1: INSOMNIA'
	else:
		x=fun(N)
		print 'Case #%d: %d'%(z+1,x)
