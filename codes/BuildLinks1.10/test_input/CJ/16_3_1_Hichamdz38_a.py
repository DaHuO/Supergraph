alf='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for i in xrange(1,input()+1):
	N=input()
	P=map(int,raw_input().split())
	S=sum(P)
	T=''
	while sum(P)>0:
		S=''
		d=max(P)
		S+=alf[P.index(d)]
		P[P.index(d)]-=1
		T+=S
	TT=''
	for j in xrange(0,len(T),2):
		TT+=T[j:j+2]+' '
	if len(TT)%3!=0:
		TT=TT[:-4]+' '+TT[-4]+TT[-2]
	print "Case #%d: %s"%(i,TT)
	