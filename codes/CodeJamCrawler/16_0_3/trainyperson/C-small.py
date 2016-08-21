outfile = open("C-small.out", "w")

def generateAttempts(n,j):
	for x in range(0,2**(n-1)):
		binary = dec_to_bin(x)
		binary = str(binary).zfill(n-2)
		binary = '1' + binary + '1'
		binary = int(binary)
		divisors = []
		for y in range (2,11):
			divisor = findDivisor(convertBase(binary, y))	
			if divisor == 0:
				break
			divisors.append(divisor)
		if len(divisors) != 9:
			continue
		outfile.write(str(binary))
		for y in divisors:
			outfile.write(" ")
			outfile.write(str(y))
		outfile.write("\n")
		j += -1
		if j == 0:
			return

def findDivisor(number):
	for x in range (2, int(number**0.5)):
		if number%x == 0:
			return x
	return 0

def convertBase(number, base):
	result = 0
	digits = str(number)
	length = len(digits)
	for x in range (0, length):
		if digits[length - 1 - x] == '1' :	
			result += base**x
	return result

def dec_to_bin(number):
    return int(bin(number)[2:])

outfile.write("Case #1:\n")
generateAttempts(16,50)
