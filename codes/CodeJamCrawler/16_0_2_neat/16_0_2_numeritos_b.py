T=int(raw_input())
for X in range(1,T+1):
	pila=raw_input()
	altura=len(pila)
	actual=pila[0]
	if(pila[-1]=='-'):
		giros=1
	else:
		giros=0
	for Y in pila:
		if(Y!=actual):
			giros+=1
			actual=Y
	print "Case #"+str(X)+": "+str(giros)
		
