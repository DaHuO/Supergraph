import os




if __name__ == '__main__':

	file = open('IN', 'r')
	dati = file.read().split('\n')
	
	T = int(dati[0])
	
	dati = dati[1:-1]
	#print dati
	
	#just for test
	#dati = []
	#for i in range(10000000):
	#	dati.append(i)
	#T = len(dati)
	
	for i in range(T):
		
		N = int(dati[i])
		
		if N == 0:
			print "Case #%i: INSOMNIA"%((i+1))
			continue
		
		chars = "0123456789"
		n = 0
		
		while len(chars) > 0:
			n = n + N
			num = str(n)
	
			for cifra in num:
				chars = chars.replace(cifra,"")


		
		print "Case #%i: %i"%((i+1),n)
		
		
		
