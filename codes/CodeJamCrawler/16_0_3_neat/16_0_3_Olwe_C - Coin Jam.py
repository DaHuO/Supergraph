import math;

def makeJamcoin(prevJamcoin):
	if prevJamcoin == None:
		newJamcoin = '1' + '0' * (N - 2) + '1';
	else:
		newJamcoin = getBinaryString(int(prevJamcoin, 2) + 2);
	
	while True:
		divisors = getDivisors(newJamcoin);
		if divisors == None:
			newJamcoin = getBinaryString(int(newJamcoin, 2) + 2);
		else:
			return [newJamcoin] + divisors;

def getDivisors(jamcoin):
	divisors = [];
	for base in range(2, 11):
		number = int(jamcoin, base);
		prime = True;
		for i in range(2, math.ceil(math.sqrt(number + 1))):
			if number % i == 0:
				divisors.append(i);
				prime = False;
				break;
		if prime:
			return None;
	return divisors;

def getBinaryString(number):
	result = str(number & 1);
	number >>= 1;
	while number > 0:
		result = str(number & 1) + result;
		number >>= 1;
	return result;

numCases = int(input());
for case in range(1, numCases + 1):
	N, J = input().split(' ');
	N = int(N);
	J = int(J);
	print("Case #" + str(case) + ":");
	jamcoin = None;
	for i in range(J):
		jamcoin, d2, d3, d4, d5, d6, d7, d8, d9, d10 = makeJamcoin(jamcoin);
		print(jamcoin, d2, d3, d4, d5, d6, d7, d8, d9, d10);
