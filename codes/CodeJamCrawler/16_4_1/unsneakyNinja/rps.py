#!/usr/bin/python
import sys
from collections import Counter

def readFile(inputfilename):
    inputfile = open(sys.argv[1])
    numtestcases = int(inputfile.readline())
    for i in range(numtestcases):
        N, R, P, S = (int(num) for num in inputfile.readline().split())
        print "Case #" + str(i+1) + ": " + str(rps(N, R, P, S))

def getMatch(winner):
	if (winner == 'P'):
		return "PR"
	if (winner == 'R'):
		return "RS"
	if (winner == 'S'):
		return "PS"
		
def getWinningString(winnerStr, N):
	newStr = ''
	for i in range(N):
		newStr = ''
		for char in winnerStr:
			newStr += getMatch(char)
		winnerStr = newStr
	return newStr

def checkCounter(s, R, P, S):
	c = Counter(s)
	if c['P'] == P and c['R'] == R:
		return 1
	return 0

def fixans(s):
	if (len(s) == 1):
		return s

	first = fixans(s[:len(s)/2])
	second = fixans(s[-len(s)/2:])
	if (first < second):
		return first + second
	return second + first

def rps(N, R, P, S):
	if (abs(R-P) > 1 or abs (R-S) > 1 or abs(P-S) >1):
		return "IMPOSSIBLE"
	if (P == 0):
		return "RS"
	else:
		ans1 = getWinningString('P', N)
		ans2 = getWinningString('R', N)
		ans3 = getWinningString('S', N)
		if (checkCounter(ans1, R, P, S)):
			return fixans(ans1)
		if (checkCounter(ans3, R, P, S)):
			return fixans(ans3)
		return fixans(ans2)




readFile(sys.argv[1])