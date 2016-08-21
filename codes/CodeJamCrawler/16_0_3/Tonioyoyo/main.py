import itertools

alreadyKnown = dict()

def isPrime(num):
	if num <= 1:
		return False
	elif num <= 3:
		return True
	else:
		i = 5
		while i*i <= num:
			if num % i == 0 or num % (i+2) == 0:
				return False
			i += 6
		return True

def checkIfJamcoin(str):
	for b in range(2, 11):
		if isPrime(readNumber(str, b)):
			return False
		else:
			pass
	return True

def returnFactor(str,base):
	num = readNumber(str,base)
	for i in range(2, num):
		if (num % i) == 0:
			if i != 1 and i != num and i not in alreadyKnown[str]:
				alreadyKnown[str].append(i)
				return i

def readNumber(str, base):
	return int(str, base)

def main():
	f = open('C-small-attempt0.in', 'r')
	fout = open('outputSmall', 'w')

	numberTestCase = int(f.readline())

	for n in range(numberTestCase):
		fout.write('Case #%d:\n' % (n + 1))
		strLine = f.readline().strip('\n').split(' ')
		numberLength = int(strLine[0])
		numberjamToFind = int(strLine[1])
		numberjamFound = 0

		listPossibilities = ["".join(seq) for seq in itertools.product("01", repeat=numberLength) if seq[0] == '1' and seq[-1] == '1']
		print(listPossibilities)

		while numberjamFound < numberjamToFind:
			jamcoinToTest = listPossibilities.pop()

			print('Testing %s' % jamcoinToTest)

			if checkIfJamcoin(jamcoinToTest):
				alreadyKnown[jamcoinToTest] = list()
				for b in range(2,11):
					returnFactor(jamcoinToTest,b)
				numberjamFound +=1
				print('Factors for %s found' % jamcoinToTest)
				print(alreadyKnown[jamcoinToTest])

		for i in alreadyKnown:
			fout.write('%s ' % i)
			for j in alreadyKnown[i]:
				fout.write('%s ' % j)
			fout.write('\n')


if __name__ == "__main__":
    # execute only if run as a script
    main()

