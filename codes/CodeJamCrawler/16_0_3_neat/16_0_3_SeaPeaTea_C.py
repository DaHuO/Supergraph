import fileinput

def bin2base(x, base):
	representation = 0;
	for i in range(0,len(x)):
		if (x[i] == "1"):
			representation = representation + base**(len(x)-1-i)
	return representation;
	
def getFirstDivisor(baseStr):
	for m in xrange(2,int(baseStr**0.5)+1):

		if (baseStr & 0b1 == 0b0):
			if (m & 0b1 == 0b0):
				return 2;
			else:
				a = int(baseStr/m);
				b = a*m;
				if (baseStr == b):
					return m;
		else:
			a = int(baseStr/m);
			b = a*m;
			if (baseStr == b):
				return m;
	else:
		return "prime";
  
finput = fileinput.input();
numTestCases = int(finput.next()); 
bitCounter = 0b0;
divFactors = "";
numDivisors = 0;
numJamCoin = 0;
jamCoin = "";
jamCoinList = "";
for j in range(1, numTestCases+1):
	inpJN = finput.next().rstrip('\n');
	inpJN = inpJN.split();
	inpN = inpJN[0];
	inpJ = inpJN[1];
	for k in xrange(0, 2**(int(inpN)-2)):
		binStr = "{0:{1:s}b}".format((bitCounter<<1)+ ((0b1 << (int(inpN)-1)) + 0b1),inpN);
		for l in range(2,11):
			baseStr = bin2base(binStr,l);
			firstDiv = getFirstDivisor(baseStr);
			if (firstDiv == "prime"):
				divFactors = "";
				numDivisors = 0;
				break;
			else:
				divFactors = divFactors + str(firstDiv) + " ";
				numDivisors = numDivisors + 1;
		if (numDivisors == 9):
			numJamCoin = numJamCoin + 1;
			jamCoin = binStr + " " + divFactors;
			jamCoinList = jamCoinList + jamCoin + "\n";
			numDivisors = 0;
			jamCoin = "";
			divFactors = "";
			if (numJamCoin == int(inpJ)):
				break;
		bitCounter = bitCounter +0b1;
	print ("Case #{}:\n{}".format(j,jamCoinList));
	jamCoinList = "";
	numJamCoin = 0;
	bitCounter = 0b0;
		
					
				
		
		

	
	

	