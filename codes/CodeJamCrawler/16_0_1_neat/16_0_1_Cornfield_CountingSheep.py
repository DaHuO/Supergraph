def solve(nummerUtdelt):
	i = 2

	nummerSomGjelder = 0

	nummerSett = []

	midlertidigListe = []

	alleNummerSett = False
	splitTall(nummerUtdelt, midlertidigListe)

	for j in range (0, len(midlertidigListe)):
				if (midlertidigListe[j] not in nummerSett):
					nummerSett.append(midlertidigListe[j])

	if (nummerUtdelt == 0):
		return "INSOMNIA"

	while (alleNummerSett == False):
		if (len(nummerSett) == 10):
			alleNummerSett = True
			return nummerSomGjelder
		
		else:
			nummerSomGjelder = nummerUtdelt*i

			splitTall(nummerSomGjelder, midlertidigListe)

			for j in range (0, len(midlertidigListe)):
				if (midlertidigListe[j] not in nummerSett):
					nummerSett.append(midlertidigListe[j])

			i+=1



def splitTall(langtTall, liste):
	for tall in str(langtTall):
		liste.append(int(tall))

	return liste



def main():
	outputFile = open("output.txt", "w")
	inputFile = open("input.in")

	line = inputFile.read().splitlines()
	for i in range(1, len(line)):
		answer = solve(int(line[i]))
		outputFile.write("Case #" + str(i) + ": " + str(answer) + "\n")

	
	outputFile.close()
	inputFile.close()



# print(solve(11))
main()


