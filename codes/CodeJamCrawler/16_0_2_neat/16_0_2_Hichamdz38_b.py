for t in xrange(1,input()+1):
	sm=0
	S=raw_input()
	while len(S)>0:
		while(S[-1]=='+'):
			S=S[:-1]
			if S=='':
				break
		if S=='':
				break
		if S[0]=='-':
			S=S[::-1]
			S=S.replace('-','_')
			S=S.replace('+','-')
			S=S.replace('_','+')
			sm+=1
		else:
			i=0
			bb=''
			while(S[i]=='+'):
				bb+='-'
				S=S[1:]
			sm+=1
			S=bb+S
	print "Case #%d: %d"%(t,sm)