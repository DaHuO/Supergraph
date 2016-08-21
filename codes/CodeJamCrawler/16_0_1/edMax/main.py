def numbers(aux):
	vec = []
	while aux != 0:
		vec.append(aux%10)
		aux = aux/10
	return vec

f = open('A-large.in')
f = f.read().split()
T = int(f[0])

for z in range(1,len(f)):
	n = int(f[z])
	numbersAlready = []
	numbersMul = []
	i = 1
	while True:
	#while i <= 200:
		number_aux = i * n
		vec = numbers(number_aux)
		for a in vec:
			if numbersAlready.count(a) == 0:
				numbersAlready.append(a)
		#print numbersAlready
		if len(numbersAlready) == 10:
			print 'Case #'+str(z)+':',number_aux
			break
		#print vec
		#break
		i = i + 1
		if i > 500000:
			print 'Case #'+str(z)+':',"INSOMNIA"
			break