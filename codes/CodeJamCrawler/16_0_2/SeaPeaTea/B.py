import fileinput

finput = fileinput.input();
numTestCases = int(finput.next());
binPancakes = "";
numFlips = 0;
for i in range(1, numTestCases+1):
	stckPancakes = finput.next().rstrip('\n');
	for j in range(0,len(stckPancakes)):
		binPancakes = "{}{}".format(binPancakes, int(stckPancakes[j] == "+"));
	numPancakes = len(binPancakes);
	happyPancakes = "1"*numPancakes;
	if (binPancakes != happyPancakes):
		for k in range(0,numPancakes):
			if (k == 0): 
				if(binPancakes[k] == "0" and numPancakes == 1):
					numFlips = numFlips + 1;
				else:
					if(binPancakes[k] != binPancakes[k+1]):
						numFlips = numFlips + 1;
			elif (k == (numPancakes - 1)):
				if (binPancakes[k] == "0"):
					numFlips = numFlips + 1;
			else:
				if (binPancakes[k] != binPancakes[k+1]):
					numFlips = numFlips + 1;
	print ("Case #{}: {}".format(i,numFlips));
	numFlips = 0;
	binPancakes = "";
