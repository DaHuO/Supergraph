
#Case #1: INSOMNIA

casos = int(input())

for caso in range(1, casos+1):
	
	Nc = int(input())
	i = 0
	N = Nc * i 
	
	if( Nc == 0 ):
		print("Case #%i: INSOMNIA" % (caso))
		continue
	
	ovelhas = []
	
	
	while(len(ovelhas) < 10):
		
		i += 1
		N = Nc * i
		Ns = str(N)
		
		for numero in range(0, len(Ns)): 
			if Ns[numero] not in ovelhas:
				ovelhas += [Ns[numero]]
		

				
	print("Case #%i: %i" % (caso,N))
		
		
