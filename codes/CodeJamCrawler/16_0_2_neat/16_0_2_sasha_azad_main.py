import sys

INPUT_FILE_NAME = sys.argv[-1]

input_file = open(INPUT_FILE_NAME, 'r')
output_file = open('output.txt', 'w')

numLines = int(input_file.readline())

for x in xrange(0,numLines):
	ostr = "Case #%d: " % (x+1) 
	inputStr = input_file.readline().split()[::-1][0]
	counter = 0

	if "-" not in inputStr:
		counter = 0

	elif len(inputStr) == 1:
		counter = 1

	else:
		while "-" in inputStr:
			counter += 1
			first = inputStr[:1]
			newStr = ""

			if first == "-":
				change = 0
				try: 
					change = inputStr.index("+")
				except: 
					change = len(inputStr)
				newStr = "+" * change
				newStr += inputStr[change:]

			else:
				change = 0
				try: 
					change = inputStr.index("-")
				except: 
					change = len(inputStr)
				newStr = "-" * change
				newStr += inputStr[change:]

			inputStr = newStr
	ostr += str(counter)

	print ostr

	output_file.write(ostr.strip())
	if (x+1) != numLines:
		output_file.write("\n")
	





