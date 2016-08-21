import sys
BRUTE_FORCE = 1000000
with open("A-large.in", 'r') as input:
	numOfTests = int(input.readline().strip())
	for testCase in xrange(numOfTests):
		sleepList = [0,1,2,3,4,5,6,7,8,9]
		N = int(input.readline())
		for itr in xrange(0,BRUTE_FORCE):
			N2 = (itr + 1) * N
			stringN = str(N2)
			for stringItr in stringN:
				if int(stringItr) in sleepList:
					sleepList.remove(int(stringItr))
			if len(sleepList) == 0:
				print "Case #%i: %i" % (testCase + 1, N2)
				break
			if itr == BRUTE_FORCE - 1:
				print "Case #%i: INSOMNIA" % (testCase + 1)
				break
