import math

def readandwritefile(filein, fileout):
	with open(filein) as f:
		lines = f.readlines()
		curline = 0
		numcases = int(lines[curline].rstrip())
		curline += 1
		linestowrite = []
		for i in range(1, (numcases+1)):
			numParties = lines[curline].rstrip()
			curline += 1
			linestowrite.append(solve(numParties, lines[curline].rstrip().split()))
			curline += 1
		writeanswer(linestowrite, fileout)
		f.close()

def writeanswer(lines, file):
	with open(file, 'w+') as f:
		for i in range(0 ,len(lines)):
			line = lines[i]
			f.write("Case #" + str(i+1) + ": " + line)
			if(i+1 < len(lines)):
				f.write("\n")
		f.close()






def solve(numParties, parties):
	entry = ""
	nums = int(numParties)
	partySum = 0
	for part in parties:
		partySum += int(part)
	while partySum > 0:
		if partySum == 3:
			maxIndex = maxIndexOfArray(parties)
			entry += letterForIndex(maxIndex)
			partySum -= 1
			parties[maxIndex] = int(parties[maxIndex])-1
		else:
			maxIndex = maxIndexOfArray(parties)
			entry += letterForIndex(maxIndex)
			partySum -= 1
			parties[maxIndex] = int(parties[maxIndex])-1

			maxIndex = maxIndexOfArray(parties)
			entry += letterForIndex(maxIndex)
			partySum -= 1
			parties[maxIndex] = int(parties[maxIndex])-1
		if partySum > 0:
			entry += " "
	return entry

def maxIndexOfArray(parties):
	if len(parties) == 0:
		return 0
	else:
		highest = int(parties[0])
		highestIndex = 0
		for i in range(0, len(parties)):
			part = int(parties[i])
			if highest < int(part):
				highest = int(part)
				highestIndex = i
		return highestIndex

def letterForIndex(index):
	if index == 0:
		return "A"
	if index == 1:
		return "B"
	if index == 2:
		return "C"
	if index == 3:
		return "D"
	if index == 4:
		return "E"
	if index == 5:
		return "F"
	if index == 6:
		return "G"
	if index == 7:
		return "H"
	if index == 8:
		return "I"
	if index == 9:
		return "J"
	if index == 10:
		return "K"
	if index == 11:
		return "L"
	if index == 12:
		return "M"
	if index == 13:
		return "N"
	if index == 14:
		return "O"
	if index == 15:
		return "P"
	if index == 16:
		return "Q"
	if index == 17:
		return "R"
	if index == 18:
		return "S"
	if index == 19:
		return "T"
	if index == 20:
		return "U"
	if index == 21:
		return "V"
	if index == 22:
		return "W"
	if index == 23:
		return "X"
	if index == 24:
		return "Y"
	if index == 25:
		return "Z"

readandwritefile('file.in', 'file.out')