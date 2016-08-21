import os

def isDone(digits):
	for num in range(0,10):
		if digits[num] != True:
			return False
	return True

def getLastNum(num):
	if num == 0:
		return 'INSOMNIA'
	multiplier = 1
	listedDigits = [False] * 10
	while(True):
		testNum = num * multiplier
		strNum = str(testNum)
		for digit in strNum:
			listedDigits[int(digit)] = True
		if isDone(listedDigits):
			return testNum
		multiplier+=1

with open('input.txt') as input_file:
    testCases = input_file.readlines()
numTestCases = testCases[0]
testCases.remove(numTestCases)
output_filename= 'output.txt'
if os.path.exists(output_filename):
	os.remove(output_filename)
for i in range(0, len(testCases)):
 	lastNum = getLastNum(int(testCases[i]))
	
	
	with open(output_filename, 'a') as output_file:
		output_file.write('Case #' + str(i+1) + ': ' + str(lastNum) + '\n')









