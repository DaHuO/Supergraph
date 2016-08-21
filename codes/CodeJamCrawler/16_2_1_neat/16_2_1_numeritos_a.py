a=["Z","G","X","W","H","U","O","S","F","N"]
b=[0,8,6,2,3,4,1,7,5,9]
c=[["E","R","O"],["E","I","H","T"],["S","I"],["T","O"],["T","R","E","E"],["F","O","R"],["N","E"],["E","V","E","N"],["I","V","E"],["I","N","E"]]

T=int(raw_input())
for i in range(1,T+1):
	cadena=list()
	cadena2=raw_input()
	numeros=list()
	for j in cadena2:
		cadena.append(j)
	for j in range(len(b)):
		nohay=0
		while nohay==0:
			try:
				resul=cadena.index(a[j])
				cadena.pop(resul)
				for k in c[j]:
					resul=cadena.index(k)
					cadena.pop(resul)
				numeros.append(str(b[j]))	
			except ValueError:
				nohay=1
	numeros.sort()
	resultado=''.join(numeros)
	print "Case #"+str(i)+": "+resultado
