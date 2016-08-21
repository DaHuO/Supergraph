#Python Pancakes Problem
#Code Jam Round 1

#Inputs: T, S (string of +/- pancakes)


def findFlipPosition(pancakes):
	lastPosition = -1
	idx = 0
	for p in pancakes:
		if p == False:
			lastPosition = idx
		idx += 1
	return lastPosition
			


def flipPancakes(S):
	#Build array
	pancakes = []
	for c in S:
		if c == '+':
			pancakes.append(True)
		else:
			pancakes.append(False)
	nFlips = 0
	flipPosition = findFlipPosition(pancakes)
	#while stack isn't all == 1
	while flipPosition != -1:
		#Do flip from this pancake
		for i in range(0,flipPosition+1):
			pancakes[i] = not pancakes[i]
		nFlips += 1
		#Find next flip position
		flipPosition = findFlipPosition(pancakes)
	return nFlips

T = int(raw_input())
for i in range(0,T):
	S = raw_input()
	print "Case #{0}: {1}".format(i+1,flipPancakes(S))
