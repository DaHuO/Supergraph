import itertools

def main():
	f = open('A-large.in', 'r')
	fout = open('outputLarge', 'w')

	numberTestCase = f.readline()

	for i in range(int(numberTestCase)):
		numberPick = int(f.readline())
		print('NumberPick: %d' % numberPick)

		allDigitsFound = False
		infinite = False
		multiplier = 1
		oldNumber = numberPick
		numberToEvaluate = numberPick
		digitsSeen = set()

		while not allDigitsFound and not infinite:
			numberToString = str(numberToEvaluate)
			for ch in numberToString:
				digitsSeen.add(int(ch))
			print(digitsSeen)

			if len(digitsSeen) == 10:
				allDigitsFound = True
			else:
				multiplier += 1
				numberToEvaluate = multiplier * numberPick

				if numberToEvaluate == oldNumber:
					infinite = True
				else:
					oldNumber = numberToEvaluate

		if infinite:
			fout.write('Case #%d: INSOMNIA\n' % (i + 1))
		else:
			fout.write('Case #%d: %d\n' % ((i + 1), numberToEvaluate))


if __name__ == "__main__":
    # execute only if run as a script
    main()

