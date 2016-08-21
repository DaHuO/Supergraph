import fileinput
import sys
def listaDeDigitoscompleta (lista):
	for numero in lista:
		if (numero == 0):
			return False
	return True

def lector():
	f = open('output','w')
	 # python will convert \n to os.linesep
	contador = 0
	with open('input2.txt') as fp:
		for linea in fp:
			if(contador == 0):
				cantCases = int(linea)
				contador = contador +1
			else:
				contadorStr = str(contador)
				String1  = "Case #"+ contadorStr + ": "
				mensaje = main(int(linea))
				mensajeStr = str(mensaje)
				String2 = String1+mensajeStr+"\n"
				f.write(String2)
				contador = contador +1
	fp.close()
	f.close()
	##inf = sys.stdin
	#contador = 0
	#for linea in inf:
	#	if(contador == 0):
	#		cantCases = int(linea)
	#		contador = contador +1
	#	else:
	#		contadorStr = str(contador)
	#		String1  = "Case #"+ contadorStr + ": "
	#		mensaje = main(int(linea))
	#		mensajeStr = str(mensaje)
	#		String2 = String1+mensajeStr+"\n"
	#		f.write(String2)
	#		contador = contador +1

def main (N):
	if(N==0):
		return "INSOMNIA"
	multiplicador = 1
	listaDeDigitos = [0,0,0,0,0,0,0,0,0,0]
	while(not listaDeDigitoscompleta(listaDeDigitos)):
		numMultiplicado = N*multiplicador
		numero = str(numMultiplicado)
		for caracter in numero:
			listaDeDigitos[int(caracter)] = 1
		multiplicador = multiplicador +1 
	return (numMultiplicado)


lector()