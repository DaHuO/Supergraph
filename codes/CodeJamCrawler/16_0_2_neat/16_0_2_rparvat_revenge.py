cache = {}
thisRound = {}

def isSolved(s):
	for char in s:
		if char == "-":
			return False
	return True

def getReverse(s):
	reverse = ""
	for char in s[::-1]:
		if char == "+":
			reverse += "-"
		else:
			reverse += "+"
	return reverse

def generateNext(s):
	#first truncate lagging +
	lastMinus = -1
	for i in range(len(s)):
		if s[i] == "-":
			lastMinus = i
	if lastMinus == -1:
		return []
	s = s[:lastMinus+1]
	possible = []
	for i in range(1,len(s)):
		if s[i-1] != s[i]:
			#flip this part and keep rest
			this = getReverse(s[:i]) + s[i:]
			possible.append(this)
	possible.append(getReverse(s))
	return possible


def solve(s):
	cache = {}
	thisRound = {s:True}
	numMoves = 0
	while True:
		print numMoves
		newRound = {}
		for s in thisRound:
			if isSolved(s):
				return str(numMoves)
			for each in generateNext(s):
				if each not in cache:
					newRound[each] = True
					cache[each] = True
		thisRound = newRound
		numMoves+=1


fileIn = "B-small-attempt0.in"
fileOut = "b_sm_0_out.txt"
with open(fileIn, "r") as f:
	with open(fileOut, "w") as w:
		t = int(f.readline())
		for i in range(1,t+1):
			s = f.readline()
			w.write("Case #" + str(i)+": " + solve(s)+"\n")

