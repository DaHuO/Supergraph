#import time
#start = time.time()

def printResult(tcn, result):
	print("Case #{}: {}".format(tcn,result))

def printInsomnia(tcn):
	print("Case #{}: INSOMNIA".format(tcn))

#printResult(testCaseNum, testCaseVal)
def process(testCaseNum, testCaseVal, testCaseBaseVal, digits):
	valCopy = testCaseVal
	# process the number for all the digits
	digits.add(valCopy % 10)
	while valCopy > 9:
		valCopy = int(valCopy / 10)
		digits.add(valCopy % 10)

	# if all the digits print result
	if len(digits) == 10 : printResult(testCaseNum, testCaseVal)
	else : process(testCaseNum, testCaseVal + testCaseBaseVal, testCaseBaseVal, digits )

with open('Input_L.txt') as f:
#with open('Input_S.txt') as f:
#with open('Input_VS.txt') as f:
	numTestCases = int(f.readline())
	for testCase in range (0,numTestCases):

		testCaseNum = testCase + 1
		testCaseBaseVal = int(f.readline())

		if testCaseBaseVal == 0: printInsomnia(testCaseNum)
		else:
			empty = set([]) 
			process(testCaseNum, testCaseBaseVal, testCaseBaseVal, empty)

#print('Time:', time.time() - start)

#Input 
#5
#0
#1
#2
#11
#1692
#
#Output 
#Case #1: INSOMNIA
#Case #2: 10
#Case #3: 90
#Case #4: 110
#Case #5: 5076