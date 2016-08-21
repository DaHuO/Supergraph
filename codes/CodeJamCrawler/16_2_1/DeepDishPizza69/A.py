

def checkWord(digit,line):
	exist=True
	for d in digit:
		if d not in line:
			exist=False
			break
		else:
			line=line.replace(d,"",1)

	return exist


def removeDigit(digit,line):
	new_line=""

	for d in digit:
		#index=line.find(d)
		line=line.replace(d,"",1)

	new_line=line



	return new_line



def process(line):
	digits=[]
	digits.append("ZERO")
	digits.append("ONE")
	digits.append("TWO")
	digits.append("THREE")
	digits.append("FOUR")
	digits.append("FIVE")
	digits.append("SIX")
	digits.append("SEVEN")
	digits.append("EIGHT")
	digits.append("NINE")

	remainDigits=[]
	remainDigits.append("ONE")
	remainDigits.append("THREE")
	remainDigits.append("FIVE")
	remainDigits.append("SEVEN")
	remainDigits.append("NINE")

	numbers=[]

	while line!="":
		#for digit in digits:
		if "Z" in line:
			digit="ZERO"
			if checkWord(digit,line):
				#print "there is "+digit+" in the "+line
				line=removeDigit(digit,line)
				no=digits.index(digit)
				numbers.append(no)
		elif "W" in line:
			digit="TWO"
			if checkWord(digit,line):
				#print "there is "+digit+" in the "+line
				line=removeDigit(digit,line)
				no=digits.index(digit)
				numbers.append(no)
		elif "U" in line:
			digit="FOUR"
			if checkWord(digit,line):
				#print "there is "+digit+" in the "+line
				line=removeDigit(digit,line)
				no=digits.index(digit)
				numbers.append(no)
		elif "X" in line:
			digit="SIX"
			if checkWord(digit,line):
				#print "there is "+digit+" in the "+line
				line=removeDigit(digit,line)
				no=digits.index(digit)
				numbers.append(no)
		elif "G" in line:
			digit="EIGHT"
			if checkWord(digit,line):
				#print "there is "+digit+" in the "+line
				line=removeDigit(digit,line)
				no=digits.index(digit)
				numbers.append(no)
		else:
			for digit in remainDigits:
				if checkWord(digit,line):
					#print "there is "+digit+" in the "+line
					line=removeDigit(digit,line)
					no=digits.index(digit)
					numbers.append(no)

		#print "line is now --> "+line


	numbers_str=""
	#sorted(numbers)
	numbers.sort()
	#print numbers
	for no in numbers:
		numbers_str+=str(no)
	#print numbers
	return numbers_str

def main():
	with open("A-small-attempt1.in", "r") as ins:
		numOfTestCases=int(ins.readline())
		#print "#cases "+str(numOfTestCases)
		

		cases=[]
		for i in range(numOfTestCases):
			line=ins.readline().rstrip()
			
			# Case #1: 2 3
			print "Case #"+str(i+1)+": "+process(line)
			




main()