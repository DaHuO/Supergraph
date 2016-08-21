import sys

firstNum = 0
digits = range(0,10)

def solveCase(num, caseNum):
	initialNum = num
	if num == 0:
		print "Case #" + str(caseNum) + ": INSOMNIA"
	else:
		while digits:
			for digit in str(num):
				if int(digit) in digits:
					digits.remove(int(digit))
			num += initialNum
		print "Case #" + str(caseNum) + ": " + str(num - initialNum)


caseNumber = 1
for line in sys.stdin:
	if firstNum == 0:
		firstNum = int(line)
	else:
		solveCase(int(line), caseNumber)
		caseNumber += 1
		digits = range(0,10)