#MAM, Google Code Jam - 2016 Qualification Round, Problem B
#Revenge of the Ihop

def convertToBool(st):
	myList = list()

	for ch in st:
		if ch == "-":
			myList.append(0)
		elif ch == "+":
			myList.append(1)

	return myList

def isSolved(st):
	if 0 in st: return False
	return True

#00011,5 --> 00111
def flip(st, n):
	backPart = st[n:]

	frontPart = st[:n]
	newFrontPart = list()

	for ch in reversed(frontPart):
		if ch == 0:
			newFrontPart.append(1)
		elif ch == 1:
			newFrontPart.append(0)

	return newFrontPart + backPart

def chooseAndDoFlip(st):

	answer = 0

	if st[0] == 0:
		x = 0
		for ch in reversed(st):
			if ch == 0: break
			x = x + 1
		answer = flip(st, len(st) - x)

	else:
		x = 0
		for ch in st:
			if ch == 0: break
			x = x + 1
		answer = flip(st, x)

	return answer

def solve(c):
	
	pancakes = c.rstrip()
	pancakes = convertToBool(pancakes)

	iterations = 0

	while not isSolved(pancakes):
		iterations = iterations + 1
		pancakes = chooseAndDoFlip(pancakes)

	return iterations

def main():
	with open('B-large.in', 'r') as infile, open('output.txt', 'w') as outfile:
		
		T = int(infile.readline())
		for x in xrange(T):
			line = infile.readline()
			outfile.write("Case #" + str(x + 1) + ": " + str(solve(line)) + "\n")

if __name__ == "__main__":
	main()