def allDigitsSeen(table):
	for digit in table:
		if digit == False:
			return False
	return True

def countSheep(N):
	if N == 0:
		return 0
	else: 
		digitsSeen = [False] * 10
		multiplier = 1
		result = N
		while not allDigitsSeen(digitsSeen):
			result = N * multiplier
			digits = [int(x) for x in list(str(result))]
			# print 'DIGITS: ', digits
			for digit in digits:
				digitsSeen[digit] = True
			multiplier += 1
		return result


def main():
	inputFile = open('A-large (1).in', 'r')
	testCases = int(inputFile.readline().strip())
	outputFile = open('output.txt', 'w')
	for i in range(testCases):
		N = int(inputFile.readline().strip())
		sheepCounted = countSheep(N)
		outputFile.write('Case #' + str(i + 1) + ': ')
		if sheepCounted == 0:
			outputFile.write('INSOMNIA')
		else:
			outputFile.write(str(sheepCounted))
		outputFile.write('\n')


main()