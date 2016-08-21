infile = open("prob1infile.txt", "r")
infileText = [x.strip() for x in infile]
infile.close()
caseCount = int(infileText[0])
outfile = open("prob1outfile.txt", "w")
for case in range(caseCount):
	curStr = infileText[case+1]
	begin = "Case #{}: ".format(case+1)
	newStr = curStr[0]
	for letter in curStr[1:]:
		if newStr[0] <= letter:
			newStr = letter + newStr
		else:
			newStr += letter
	newStr += "\n"
	outfile.write(begin + newStr)
outfile.close()
