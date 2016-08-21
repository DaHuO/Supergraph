import fileinput

finput = fileinput.input();
numTestCases = int(finput.next());
seenNumbers = 0b0000000000;
for i in range(1, numTestCases+1):
	varN = finput.next().rstrip('\n');
	strN = varN;
	k = 1;
	count = 0;
	if (varN == "0"):
		lastNum = "INSOMNIA";
	else:
		while seenNumbers != 0b1111111111:
			for j in range(0, len(strN)):
				seenNumbers = 2**(int(strN[j])) | seenNumbers;
				lastNum = strN;
			intN = int(varN) * (k + 1);
			strN = str(intN);
			k = k + 1;
			count = count + 1;
	print ("Case #{}: {}".format(i,lastNum));
	seenNumbers = 0b0000000000;
	k = 1;
	count = 0;
	
	

