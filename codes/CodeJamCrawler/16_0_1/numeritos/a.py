T=int(raw_input())
for X in range(1,T+1):
	numeros=[0,0,0,0,0,0,0,0,0,0]
	carac=raw_input()
	M=long(carac)
	if M==0:
		print "Case #"+str(X)+": INSOMNIA"
	else:
		longitud=len(carac)	
		multipli=1
		while numeros!=[1,1,1,1,1,1,1,1,1,1]:
			N=M*multipli
			resp=N		
			longitud=len(str(resp))
			while(longitud!=0):
				ultimo=N%10
				numeros[ultimo]=1
				N=N/10
				longitud=longitud-1
			multipli=multipli+1
		print "Case #"+str(X)+": "+str(resp)
