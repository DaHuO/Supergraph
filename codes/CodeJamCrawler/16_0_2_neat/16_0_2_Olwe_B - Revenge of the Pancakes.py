numCases = int(input());
for case in range(1, numCases + 1):
	S = input()[::-1];
	prevChar = '+';
	numFlips = 0;
	for nextChar in S:
		if nextChar != prevChar:
			numFlips += 1;
			prevChar = nextChar;
	print("Case #" + str(case) + ":", numFlips);
