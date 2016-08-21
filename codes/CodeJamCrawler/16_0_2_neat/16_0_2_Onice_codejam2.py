import sys

T = 0
caseNum = 1

def other(symbol):
	if symbol == "-":
		return "+"
	else:
		return "-"


def doFlip(pancakes):
	while pancakes[-1:] == "+":
		pancakes = pancakes[:-1]
	newCakes = ""
	if pancakes[0] == "-":
		rCakes = pancakes[::-1]
		for cake in rCakes:
			newCakes += other(cake)
	else:
		rCakes = pancakes[:pancakes.rindex('+')+1][::-1]
		newCakes2 = pancakes[pancakes.rindex('+')+1:]
		for cake in rCakes:
			newCakes += other(cake)
		newCakes += newCakes2
	return newCakes


for line in sys.stdin:
	if T == 0:
		T = int(line)
	else:
		pancakes = line.strip()
		flips = 0
		while "-" in pancakes:
			pancakes = doFlip(pancakes)
			flips += 1

		print "Case #" + str(caseNum) + ": " + str(flips)
		caseNum += 1
