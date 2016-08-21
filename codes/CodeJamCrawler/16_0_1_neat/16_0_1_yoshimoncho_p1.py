infile = open('A-large.in', 'r')
outfile = open('A-large.out', 'w')
top = int(infile.readline())

for i in range(1,top+1):

	text = infile.readline()
	number = int(text)
	print "numero"+ str(number)


	#Algoritmo de suma
	#lista = infile.readline()
	#lista.replace("\n","")
	#lista = lista.split(" ")
	lista = []
	counter = 1
	conseguido = 0
	while True:
		aux = []
		actual = counter * number

		if number == 0:
			outfile.write("Case #"+ str(i) + ": "+ "INSOMNIA")
			break
		if counter == 1:
			lista = list(map(int, str(actual)))
		else:
			aux = list(map(int, str(actual)))
			aux = list(set(aux))


		lista = lista + aux
		lista = list(set(lista))

		if len(lista) == 10:
			break;

		counter += 1

	if number != 0:
		outfile.write("Case #"+ str(i) + ": "+ str(actual))

	if i != top: 
		outfile.write("\n")

infile.close()
outfile.close()