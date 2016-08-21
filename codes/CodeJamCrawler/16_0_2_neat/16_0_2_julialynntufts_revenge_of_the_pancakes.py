#Google Code Jam - Qualification Round 2016

inputfile = open('B-large.in')
outputfile = open('output.txt', 'w')
caseNum = 1

numCases = int(inputfile.readline())

def calculate_num_flips( pancake_string ):
	num_flips = 0
	last_p = pancake_string[0]
	
	for p in pancake_string:
		if p != last_p:
			num_flips += 1
			last_p = p

	if last_p == '-':
		num_flips += 1

	return str(num_flips)

# Read each pancake string and determine the number of flips
for line in inputfile:
	outputfile.write('Case #' + str(caseNum) + ': ' + calculate_num_flips(line.strip()) + '\n')
	caseNum += 1