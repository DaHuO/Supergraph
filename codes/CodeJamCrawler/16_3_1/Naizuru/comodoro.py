import sys

primera_linea = sys.stdin.readline() # Se saltea la primer linea
contador = 0
patron = 3

for line in sys.stdin:

	patron = (patron - 1) % 2
	
	if not patron: continue

	lista = [ int(char) for char in  line[0:-1].split(' ') ]

	res = False
	salidas = []
	
	while not res: 

	#	print lista

		m = max(lista)
		maximos = [i for i, j in enumerate(lista) if j == m]
		salidas.append(maximos[0])
		lista[maximos[0]] -= 1
		

		if float(max(lista))/float(sum(lista)) > .5:
#			print (max(lista)/sum(lista))
			maximos = [i for i, j in enumerate(lista) if j == m]
			salidas[-1] = [salidas[-1], maximos[0]]
			lista[maximos[0]] -= 1

		evaluar = [k==0 for k in lista]
		res = True
		for estado in evaluar:
			res = res and estado
#	print lista
#	print salidas
	#print line,
	#print lista

	estring = []

	for elemento in salidas:
		if type(elemento) is list:
			mitemp = ''.join([ chr(65 + lauty) for lauty in elemento])	

			estring.append(mitemp)

		else:
			estring.append(chr(65 + elemento))

	chileno = ' '.join(estring)
	#print chileno

	contador += 1
	sss =  "Case #" + str(contador) +  ": " +  chileno
	print sss
