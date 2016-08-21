import sys

def getDigits(digits,num):
	number = str(num)
	for digit in number:
		if digit not in digits:
			digits.add(digit)

def allDigitsPresent(digits):
	return len(digits) == 10

def solve(lines,index):
	N = lines[index]
	if int(N) == 0:
		print ('Case #' + str(index) + ': ' + 'INSOMNIA')
	else:
		digits = set()
		getDigits(digits,N)
		currentN = N
		i = 2
		while allDigitsPresent(digits) == False:
			currentN = int(N) * i
			i += 1
			getDigits(digits,currentN)

		print('Case #' + str(index) + ': ' + str(currentN))



def main():
	lines = sys.stdin.read().splitlines()
	numberOfTests = int(lines[0])
	for index in xrange(1,numberOfTests+1):
		solve(lines,index)

if __name__ == '__main__':
	main()