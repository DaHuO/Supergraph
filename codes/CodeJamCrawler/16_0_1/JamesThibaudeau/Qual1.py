def CountSheep(number):
	if number <= 0:
		return "Insomnia"
	count = 1
	digits = []
	initial = number
	while len(digits) <10:
		for digit in str(number):
			if digit not in digits:
				digits.append(digit)
		count +=1
		number = count * initial
	return number - initial


infile = "A-large.in"
outfile = "output.txt"

with open(infile, "r") as fin, open(outfile,"w") as fout:
	casevalues = [line.rstrip('\n') for line in open(infile)]
	numcases = casevalues[0]
	print(numcases, "cases")

	for case in range(1, len(casevalues)):
		
		result = CountSheep(int(casevalues[case]))

		outstr = "Case #%d: %s" % (case, result)
		fout.write(outstr + "\n")
		print(outstr)