import math

def es_primo(numero):
#	print "%"
	i=2
	for i in range(2,int(math.sqrt(numero))):
#		print "		primo: "+str(numero)+" % "+str(i)+" = "+str(numero%i)
		if(numero%i==0):
			return i
	return 0

T=int(raw_input())
for x in range(1,T+1):
	N,J=map(lambda x: int(x),raw_input().split())
	print "Case #"+str(T)+":"
	a=list()
	b=list()
	
	vacios=N-2
	maximo=2**vacios
	actual=0
	
	contador=0
	
	while(contador<J and actual<maximo):
		binario=bin(actual)[2:]
		cu="1"+("0"*(vacios-len(binario)))+binario+"1"
#		print "probando con "+str(actual)+" que es "+cu
#		print "probando con "+cu
		actual=actual+1
		c=""
		j=2
		bandera=1
		while j<11 and bandera!=0:
			ancho=len(cu)-1
			ini=long(0)
			for x in cu:
				aux=int(x)*j**ancho
				ancho-=1
				ini+=aux
#			print "	probando con "+str(ini)+"en base "+str(j)
			bandera=es_primo(ini)
			c+=str(bandera)
			if(j!=10):
				c+=" "
			j+=1
		if bandera!=0:
			print str(cu)+" "+str(c)
			contador+=1
#		print "------------------"
