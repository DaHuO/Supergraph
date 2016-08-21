def ok(S):
	for s in S:
		if s=='-':
			return False
	return True



for t in range(int(input())):
	S=list(raw_input())
	ans=0
	while not ok(S):
		i=1
		ans+=1
		while i<len(S) and S[i]==S[i-1]:
			i+=1

		for x in range(0,i):
			if S[x]=='-':
				S[x]='+'
			else:
				S[x]='-'

	print 'Case #%d: %d'%(t+1, ans)
