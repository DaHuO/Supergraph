#!/usr/bin/python3

def score(input):
	score = 0
	last = ''
	for index in range(0, len(str(input))):
		c = input[index]
		if c == '-':
			if last == '+':
				score += 2
			if last == '':
				score += 1
		last = c
	return score				

file = open('input1.txt', 'r')
caseNumber = file.readline()
caseArray = []
text_file = open("output.txt", "w")
for index in range(0, int(caseNumber)) :
	case = str(file.readline())
	count = index+1
	caseArray.append("Case #%d: %s" % (count, score(case)))
	text_file.write("Case #%d: %s\n" % (count, score(case)))
text_file.close()	
print caseArray
