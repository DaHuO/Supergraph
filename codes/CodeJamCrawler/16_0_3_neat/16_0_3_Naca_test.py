import math

def convertFromBaseAToBase10(A, x) :
	xBase10 = 0;
	power = 0;

	while (x > 0) :
		xBase10 += (x % 10) * int(math.pow(A, power));
		x //= 10;
		power += 1;

	return xBase10;

def isPrime(x) :
	limit = int(math.sqrt(x));

	for i in range(2, limit + 1) :
		if (x % i == 0) :
			return False;

	return True;

def divisorNonTrivial(x) :
	limit = int(math.sqrt(x));

	for i in range(2, limit + 1) :
		if (x % i == 0) :
			return i;
	return 0;

def generateJamcoin(N) :
	output = [];

	for i in range(int(math.pow(2, N - 2))) :
		tmp = i + int(math.pow(2, N - 2));
		tmp *= 2;
		tmp += 1;

		output.append(convertToBinaryRepresentation(tmp));

	return output;

def convertToBinaryRepresentation(x) :
	power = 0;
	while (x // int(math.pow(2, power)) > 0) :
		power += 1;

	tmp = 0;
	for i in range(power, -1, -1) :
		tmp += int(math.pow(10, i)) * (x // int(math.pow(2, i)));
		x = x % int(math.pow(2, i));

	return tmp;

T = int(input());
data = [];
for i in range(T) :
	dataToParse = input().split(" ");
	data.append([int(dataToParse[0]), int(dataToParse[1])]);

for i in range(T) :
	count = 0;
	print("Case #" + str(i + 1) + ":");

	potentialJamcoin = generateJamcoin(data[i][0]);

	for j in range(len(potentialJamcoin)) :
		prime = False;

		for a in range(2, 11) :
			if (isPrime(convertFromBaseAToBase10(a, potentialJamcoin[j]))) :
				prime = True;
				break;

		if (not prime) :
			divisor = [];
			for a in range(2, 11) :
				divisor.append(divisorNonTrivial(convertFromBaseAToBase10(a, potentialJamcoin[j])));

			print(str(potentialJamcoin[j]) + " " + \
				  str(divisor[0]) + " " + \
				  str(divisor[1]) + " " + \
				  str(divisor[2]) + " " + \
				  str(divisor[3]) + " " + \
				  str(divisor[4]) + " " + \
				  str(divisor[5]) + " " + \
				  str(divisor[6]) + " " + \
				  str(divisor[7]) + " " + \
				  str(divisor[8]) + " ");

			count += 1;

			if (count == data[i][1]) :
				break;


