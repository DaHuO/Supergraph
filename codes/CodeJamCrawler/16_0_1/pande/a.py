fh = open("A.in")
a1=0
f = open ("A.txt", "a")
for line in fh:
	a=line.strip()
	if a1>0:
		cont=0
		numeros=list()
		numero=int(line.strip())
		aux=numero
		if numero==0:
			f.write("Case #"+str(a1)+": "+"INSOMNIA\n")
			print "Case #"+str(a1)+": "+"INSOMNIA"
		else:
			k=str(numero)
			for l in k:
				if not l in numeros:
					numeros.append(l)
			while len(numeros)<10:
				cont=cont+1
				k=str(numero)
				for l in k:
					if not l in numeros:
						numeros.append(l)
				numero=numero+aux
			print numero-aux	
			f.write("Case #"+str(a1)+": "+str(numero-aux)+"\n")
	a1=a1+1
f.close()
	
