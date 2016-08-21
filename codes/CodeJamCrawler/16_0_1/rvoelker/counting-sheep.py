import gcjbase

def countSheep(inFile):
	n = int(inFile.readline())

	if n == 0:
		return "INSOMNIA"
	else:
		numberOfDigitsSeen = 0
		lastNumber = "0"
		digitsSeen = [
			False, False,
			False, False,
			False, False,
			False, False,
			False, False
		]
		
		multiplier = 1

		while numberOfDigitsSeen < 10:
			lastNumber = str(multiplier * n)

			for digitAsString in lastNumber:
				digit = int(digitAsString)

				if not digitsSeen[digit]:
					digitsSeen[digit] = True
					numberOfDigitsSeen += 1

			multiplier += 1

		return lastNumber

gcjbase.run(countSheep)
