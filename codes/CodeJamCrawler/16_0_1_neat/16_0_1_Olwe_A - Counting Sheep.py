def getDigits(i):
	result = set();
	while i > 0:
		result |= {i % 10};
		i //= 10;
	return result;

numCases = int(input());
for case in range(1, numCases + 1):
	digitsFound = set();
	N = int(input());
	if N == 0:
		print("Case #" + str(case) + ": INSOMNIA");
	else:
		i = 0;
		while len(digitsFound) < 10:
			i += N;
			digitsFound |= getDigits(i);
		print("Case #" + str(case) + ":", i);
