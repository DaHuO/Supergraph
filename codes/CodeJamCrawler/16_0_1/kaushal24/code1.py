C=int(raw_input())
for i in range(1,C+1):
	L=[0,0,0,0,0,0,0,0,0,0]
	NN=int(raw_input())
	j=0
	N=NN
	if N!=0:
		while (0 in L):
			j+=1
			n=NN*j
			while n:
				L[n%10]=1
				n=n/10
		print "Case #"+str(i)+":",NN*j
	else:
		print "Case #"+str(i)+": INSOMNIA"
