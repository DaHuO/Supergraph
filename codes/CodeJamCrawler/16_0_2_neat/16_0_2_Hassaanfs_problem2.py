def giveInvertedStack(string):
	s = list(string)
	s.reverse()
	return s

def allUp(arr):
	count = 0
	for i in arr:
		if(i == '+'):
			count += 1
	if(count == len(arr)):
		return True
	else:
		return False

def flip(invStack):
	stLen = len(invStack)
	for i in range(stLen):
		if(invStack[i] == '-'):
			for j in range(stLen-i):
				if(invStack[j+i] == '-'):
					invStack[j+i] = '+'
				else:
					invStack[j+i] = '-'
			break

def totalFlips(string):
	invStack = giveInvertedStack(string)
	flips = 0
	while(not allUp(invStack)):
		flip(invStack)
		flips += 1
	return flips


if __name__ == "__main__":
	lines = [line.rstrip('\n') for line in open('B-large.in')]
	count = 0
	f = open('output.txt', 'w')
	for string in lines:
		if(count != 0):
			f.write("Case #"+str(count)+": "+str(totalFlips(string))+"\n")
			print "Case #", count, ": ", totalFlips(string)
		count += 1
	f.close()