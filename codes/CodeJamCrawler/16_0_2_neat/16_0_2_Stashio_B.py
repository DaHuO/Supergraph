import re

fr = open("input.txt", 'r')
fw = open("output.txt", 'w')

lines = fr.readlines()

numTests = int(lines[0].strip())
curTest = 0
curLine = 1

def getLine():
	global curLine
	global lines
	curLine += 1
	return lines[curLine-1]
	
while curTest < numTests:
	chars = getLine().strip()
	
	flips = 0
	sign = 0 if chars[0] == "+" else 1
	lastChar = chars[0]
	
	for char in chars:
		if char != lastChar:
			flips += 1
			lastChar = char
			sign ^= 1
			
	fw.write("Case #%d: %s\n" % (curTest+1, flips + sign))
	curTest += 1
					
fr.close()
fw.close()