
casos = int(input())

for caso in range(1, casos+1):
	
	pilha = []
	flip = 0
	entrada = input()
	
	for i in range(0, len(entrada)):
		pilha += [entrada[i]]
		
		
	#Fix para evitar erro index
	#pilha += ['-']

	#Procura por -
	while( '-' in pilha):
		
		if '+' in pilha:
			for i in range(0, len(pilha)):
				if pilha[i] == '-' and pilha[i+1] == '+':
					aponta = i
					break
					
				if pilha[i] == '+' and pilha[i+1] == '-':
					aponta = i
					break
		else:
			aponta = len(pilha)-1
		
		#print("Pilha",pilha,"Aponta:",aponta)
		#Flip
		flip += 1
		
		while(aponta >= 0):
			if pilha[aponta] == '+':
				pilha[aponta] = '-'
				
			else:
				pilha[aponta] = '+'
			
			aponta -= 1
	
		#print("Nova pilha", pilha)
	
	
	print("Case #%i: %i" % (caso,flip))
