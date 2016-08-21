def flipPancakes(S):
	numFlips = 0
	numPancakes = len(S)
	for i in range(numPancakes):
		currentPancake = S[numPancakes - i - 1]
		if currentPancake == '-' and numFlips % 2 == 0:
			numFlips += 1
		if currentPancake == '+' and numFlips % 2 == 1:
			numFlips += 1
	return numFlips




def main():
	fileName = raw_input()
	with open(fileName) as f:
		rawFile = f.read()
	info = rawFile.split()
	numTests = int(info[0])
	for i in range(numTests):
		print "Case #"+str(i+1)+': '+ str(flipPancakes(info[i+1]))


if __name__ == "__main__":
    main()